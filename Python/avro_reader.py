
in_avro = 'C:\Projects_Folder\index_view_output000000000001'
int = 0

with open(in_avro, 'rb') as f:
    for i in f:
        i.decode("utf-8") 
        int += i.count('index_id')

        # if int == 1:
        #     break

print(int)
