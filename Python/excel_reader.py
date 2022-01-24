import pandas as pd

file = '/Users/Nakkie/Downloads/Some_file.xlsx'
sheet = 'DATA'
headers = 1

df = pd.read_excel(io=file,sheet_name=sheet,header=headers)
# df3 = pd.DataFrame()
df3 = pd.DataFrame(columns=['country', 'values', 'source'])

for column in df.columns:
    if column == 'country' or column == 'id':
        ''
    else:
        df2 = pd.DataFrame(columns=['country','values'])
        df2['country'] = df['country']
        df2['values'] = df[column]
        df2['source'] = column

        filename = '/Users/NAkkie/Downloads/'+column+'.csv'

        df2.to_csv(path_or_buf=filename)
