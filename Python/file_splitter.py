import pandas as pd

import_csv = '/Users/Nakkie/Downloads/demodata.csv'
import_df = pd.read_csv(import_csv, low_memory=False)

file_end = int(len(import_df.index))
batches = [[0,500000], [500001,510000], [510001,515000], [515001,520000], [520001,file_end]]
reit = 0

for item in batches:
    reit += 1

    export_df = import_df.iloc[item[0]:item[1]]
    export_df = export_df.convert_dtypes()

    export_path = '/Users/Nakkie/Downloads/demo_'+str(reit)+'.csv'
    export_df.to_csv(export_path, index=False)
