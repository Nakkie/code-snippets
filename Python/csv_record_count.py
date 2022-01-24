import pandas as pd

import_csv = '/Users/hardusmodusbps.com/Downloads/customer_6.csv'

import_df = pd.read_csv(import_csv, low_memory=False)

print(len(import_df.index))