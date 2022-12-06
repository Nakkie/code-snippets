import pandas as pd

input_file_name = 'file.csv'
input_file_path = 'C:\myfolder'

df = pd.read_csv(input_file_path+'\\'+input_file_name, sep=',', low_memory=False, header=None)
del df[df.columns[0]]

columns = len(df.columns)
cnt = 0

replace_list = (
" ",
"#",
"/",
"(",
")",
"'",
"-",
"&",
"\n"
)

while cnt < columns:
    new_col = str((df.iloc[0, cnt])) +'_'+str((df.iloc[1, cnt])) +'_'+str((df.iloc[2, cnt]))
    cnt+=1

    for i in replace_list:
        new_col = new_col.replace(i, "")

    df.rename(columns = {cnt:new_col}, inplace = True)

df = df.drop(range(0,3))

df.to_csv(input_file_path+'\\file_cleaned.csv', index=False)
