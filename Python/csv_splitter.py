import pandas as pd

in_csv = 'C:\GitProjects\Local\demodata.csv'
csv_df = pd.read_csv(in_csv, low_memory=False)

row_cnt = len(csv_df.index)
batch_start = 0
batch_size = 100000

while batch_start <= row_cnt:
      batch_end = batch_start + batch_size

      if batch_start == 0:
         batch_start
      else:
          batch_start += 1

      print("Batch starting record ",batch_start)
      print("Batch end record ",batch_end)

      export_df = csv_df.iloc[batch_start:batch_end]

      export_df = export_df.convert_dtypes()

      export_csv = "C:\GitProjects\Local\demo_data_"+str(int(batch_end/100000))+".csv"
      export_df.to_csv(export_csv, index=False)

      if batch_start == 0:
         batch_start
      else:
          batch_start -= 1

      batch_start += batch_size
      