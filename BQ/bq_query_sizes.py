import os

import pandas as pd
from google.cloud import bigquery

GCP_AUTH = 'application_default_credentials.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=GCP_AUTH
project_name = 'my-project'

client = bigquery.Client(project=project_name)
regions = ['region-eu','region-us']

output_file = 'C:\\Gitprojects\\{}_querysizes.csv'.format(project_name)
main_df = pd.DataFrame(columns=['region', 'creation_time', 'user_email', 'job_id', 'job_type', 'statement_type', 'query', 'total_bytes_processed', 'total_slot_ms', 'cache_hit', 'total_bytes_billed'])

if regions:
    for region in regions:  # API request(s)

        query_job = client.query("select creation_time, user_email, job_id, job_type, statement_type, query, total_bytes_processed, total_slot_ms, cache_hit, total_bytes_billed/pow(1024,3) as total_gb_billed from "+region+".INFORMATION_SCHEMA.JOBS")

        results = query_job.result()
        for row in results:
            temp_df = pd.DataFrame({'region': region,
                                    'creation_time': row.creation_time,
                                    'user_email': row.user_email, 
                                    'job_type': row.job_type, 
                                    'statement_type': row.statement_type, 
                                    'total_bytes_processed': row.total_bytes_processed, 
                                    'total_slot_ms': row.total_slot_ms, 
                                    'cache_hit': row.cache_hit, 
                                    'total_gb_billed': row.total_gb_billed
                                    }, index=[0])
            main_df = main_df.append(temp_df)

else:
    print('Incorrect region for {}.'.format(project_name))

main_df.to_csv(output_file, index=False)
