from __future__ import print_function
import pickle
import os.path

from googleAPI.credential import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account

import pandas as pd

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
AUTH_TOKEN = os.getenv("AUTH_JSON")
GCP_AUTH = os.getenv("BQ_AUTH")
GCP_PROJECT = "example-project"


def generate_auth():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                AUTH_TOKEN, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def call_api(service, month):
    # Call the Calendar API
    monthe = month + 1
    if monthe > 12 :
        monthe = 12

    if len(str(month)) == 1:
        month = "0"+str(month)
    if len(str(monthe)) == 1:
        monthe = "0"+str(monthe)


    # startdate = f"2022-01-01T00:00:00.000000Z"
    # enddate = f"2022-02-01T00:00:00.000000Z"
    print('Getting the events')
    events_result = service.events().list(calendarId='primary', timeMin=startdate,
                                          timeMax=enddate, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    df = pd.DataFrame(columns=['StartTime', 'EndTime', 'Event'])
    print('Events got')

    if not events:
        print('No upcoming events found.')
    for event in events:
        print('Set Start Date')
        start = event['start'].get('dateTime', event['start'].get('date'))
        print('Set End Date')
        end = event['end'].get('dateTime', event['end'].get('date'))

        print('Set Summary')
        if 'summary' in event:
            summary = event['summary']
        else:
            summary = 'No title'

        print('Updating DF')
        df2 = pd.DataFrame(data={'StartTime': start, 'EndTime': end, 'Event': summary}, index=[0])
        df = df.append(df2)

    print('Returning events')
    return df, month


def upload_to_bq(GCP_PROJECT, GCP_AUTH, upload_data, month):

    print('GCP Auth')
    gcp_credentials = service_account.Credentials.from_service_account_file(GCP_AUTH)

    print('Uploading data')
    upload_data.to_gbq(f"staging.meets_Jan22", project_id=GCP_PROJECT, if_exists='replace', credentials=gcp_credentials)


if __name__ == '__main__':

    # months = [01]
    #
    # for month in months:
        client = generate_auth()
        diary_table, runmonth = call_api(client, 1)
        upload_to_bq(GCP_PROJECT, GCP_AUTH, diary_table, 1)

