import pandas as pandas
import re
df = pd.read_excel('c:\\Users\\me\\PATHTOEXCEL\\data.xlsx')
directory = "\\\\NetworlDrive\\PATH\\To\\Connectors.py"
os.chdir(directory)
from Connectors import df_to_sql

# manipulate your dataframe as needed

# make a primary key
df['key'] = df.index.format()

#name a new table to import to
new_table = 'ThisIsMyTableName'.lower().replace(' - ','').replace(' ','')

# regex prep of table
df.columns = [re.sub('[\(\)\/\- ]','_',col)+'_' for col in list(df.keys()))]
df_to_sql(df, new_table, pkey="key_")
