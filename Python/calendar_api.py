from __future__ import print_function

import datetime
import os.path

import pandas as pd

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def pull_cal(then, now):
    """Shows basic usage of the Google Calendar API."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:\\my-oath-key.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        print('Getting events')
        events_result = service.events().list(calendarId='primary', 
                                              timeMin=then,
                                              timeMax=now,
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No events found')
        else:
            return events

    except HttpError as error:
        print('An error occurred: %s' % error)
    

def events_to_df(events):

    df_columns = ['event_name', 'event_type', 'creator', 'organizer', 'event_start', 'event_end']
    event_df = pd.DataFrame(columns=df_columns)

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        creator = event['creator'].get('email')
        organizer = event['organizer'].get('email')
        eventtype = event['eventType']
        eventname = event['summary']

        new_row = {'event_name':eventname, 'event_type':eventtype, 'creator':creator, 'organizer':organizer, 'event_start':start, 'event_end':end}

        event_df = event_df.append(new_row, ignore_index=True)

    return event_df


def df_to_bq(df, year, month):
    # Set up authentication with Google Cloud
    bq_creds = service_account.Credentials.from_service_account_file('C:\\mykeyfile.json')

    # Define the destination table in BigQuery
    project_id = 'my-project'
    dataset_id = 'my-data-set'
    table_name = 'my-table'
    if len(str(month)) < 2:
        month = '0'+str(month)

    # Push the DataFrame to BigQuery
    # Table created per month
    df.to_gbq(destination_table=f'{dataset_id}.{table_name}_{year}{month}',
          project_id=project_id,
          credentials=bq_creds,
          if_exists='replace')

# Cycle through each month of the given years
years = [2022,2023]

for year in years:
    month = 1
    while month <= 12:

        start_of_month = datetime.datetime(year, month, 1)
        start_of_month = start_of_month.isoformat()+'Z'

        if month == 12:
            end_of_month = datetime.datetime(year + 1, 1, 1) - datetime.timedelta(days=1) + datetime.timedelta(hours=23)

        else:
            end_of_month = datetime.datetime(year, month + 1, 1) - datetime.timedelta(days=1) + datetime.timedelta(hours=23)

        end_of_month = end_of_month.isoformat()+'Z'

        try:
            events = pull_cal(start_of_month, end_of_month)
            print(f'Creating dataframe for {year} and {month}')
            df = events_to_df(events)
            print(f'Uploading dataframe for {year} and {month}')
            df_to_bq(df, year, month)
        except:
            print(f'Could not load for {year} and {month}')

        month+=1