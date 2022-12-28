import os
from os import listdir
from os.path import isfile, join
import pprint
import time

from google.cloud import storage
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

# GOOGLE AUTH
GCS_SERVICE_ACCOUNT_FILE='C:\mykey.json'
storage_client = storage.Client.from_service_account_json(GCS_SERVICE_ACCOUNT_FILE)

# LOCAL FILE UPLOADER (to GCS)
bucket_name = 'mybucket'
bucket = storage_client.bucket(bucket_name)

blob = bucket.blob(outputfile)
blob.upload_from_filename(mypath+outputfile)

# SQL IMPORT (from GCS)
credentials = GoogleCredentials.get_application_default()

service = discovery.build('sqladmin', 'v1beta4', credentials=credentials)

project = 'myproject'
instance = 'myinstance'

instances_import_request_body = {
  "importContext": {
    "database": "mydb",
    "fileType": "SQL",
    "importUser": "adminuser",
    "uri": "gs://mybucket/dump.sql"
  }
}

request = service.instances().import_(project=project, instance=instance, body=instances_import_request_body)

response = request.execute()

# CHECK STATUS
operation = response['name']
op_request = service.operations().get(project=project, operation=operation)
op_response = op_request.execute()

while op_response['status'] in ['PENDING','RUNNING']:
    op_request = service.operations().get(project=project, operation=operation)
    op_response = op_request.execute()
    
    if op_response['status'] != 'DONE':
        time.sleep(5)

print(op_response)
