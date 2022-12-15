import os

import pandas as pd
from google.cloud import bigquery

GCP_AUTH = 'application_default_credentials.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=GCP_AUTH
project_name = 'my-project'

client = bigquery.Client(project=project_name)
datasets = list(client.list_datasets())

output_file = 'C:\\Gitprojects\\{}_tablesizes.csv'.format(project_name)
main_df = pd.DataFrame(columns=['Dataset', 'Table', 'Size'])

if datasets:
    for dataset in datasets:  # API request(s)

        query_job = client.query("select table_id, sum(size_bytes)/pow(1024,3) as size from `"+dataset.dataset_id+"`.__TABLES__ group by 1")

        results = query_job.result()
        for row in results:
            temp_df = pd.DataFrame({'Dataset': dataset.dataset_id, 'Table': row.table_id, 'Size': row.size}, index=[0])
            main_df = main_df.append(temp_df)

else:
    print('{} project does not contain any datasets.'.format(project_name))

main_df.to_csv(output_file, index=False)
