import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Setting the project variables
GCP_PROJECT = 'my-project'
GCP_AUTH = 'my-key.json'
gcp_credentials = service_account.Credentials.from_service_account_file(GCP_AUTH)

# yeah it's split, this is how I like it
input_file_name = 'MyFile.csv'
input_file_path = 'C:\my-file-path'

df = pd.read_csv(input_file_path+'\\'+input_file_name, sep=',', low_memory=False)

# this section can be expanded for any other special chars or odd column names
df_columns = df.head()
for i in df_columns:

    inew = i.replace(" ", "_")

    df.rename(columns={i: inew}, inplace=True)

# where the magic happens, tgf pandas
df.to_gbq("dataset.table_name", project_id=GCP_PROJECT, if_exists='replace', credentials=gcp_credentials)
