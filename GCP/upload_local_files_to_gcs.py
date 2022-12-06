from google.cloud import storage
import os

GCS_SERVICE_ACCOUNT_FILE='C:\service_account_key.json'
storage_client = storage.Client.from_service_account_json(GCS_SERVICE_ACCOUNT_FILE)

basepath = 'C:\\upload_files_dir'
loblist = os.listdir(basepath)

for file in loblist:

    bucket_name = 'my_bucket'
    bucket = storage_client.bucket(bucket_name)
    stats = storage.Blob(bucket=bucket, name=file).exists(storage_client)

    if stats == False:
        blob = bucket.blob(file)
        blob.upload_from_filename(basepath+"\\"+file)

        print("File uploaded ",file)

    else:
        print("File exists ",file)
