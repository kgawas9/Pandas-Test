import pandas as pd


data_one_columns = ['Ship to City/State', 'Universal product description', 'Universal Product Code', 'Current Price']
data_two_columns = ['City / State name', 'product description', 'Product Code', 'Cur Price']
df1 = pd.read_excel(f'data_one.xlsx', index_col=None, sheet_name='Sheet1', usecols=data_one_columns, skiprows=3 )

df2 = pd.read_excel(f'data_two.xlsx', index_col=None, sheet_name='Sheet1', usecols=data_two_columns, skiprows=3 )

df_all_records = pd.concat([df1, df2.rename(columns={'City / State name':'Ship to City/State', 'product description':'Universal product description',
'Product Code':'Universal Product Code', 'Cur Price':'Current Price'})], axis=0, ignore_index=True)
print(df_all_records)

df_all_records.to_excel('concatenated_file.xlsx', header=True, sheet_name='merged_values', index=False)
print("Task completed")