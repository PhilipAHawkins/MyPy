"""
sample for extracting data from a PG database and dropping into a dataframe
"""

import psycopg2
import pandas as pd
import numpy as np

conn = None
access = "dbname='DATABASENAMEHERE' user='USERNAMEHERE' host='IPADDRESSHERE', password='PASSWORDHERE'"
conn = psycopg2.connect(access)
cur = conn.cursor()

dashboard_query = """Select * from my_table"""
cur.execute(dashboard_query)
rows = cur.fetchall()
conn.commit()
cur.close()
col_names=[]
for col in cur.description:
    col_names.append(col[0])
df = pd.DataFrame(rows, columns=col_names)
# do things to the df here as needed
save_path = '//PATH/folder'
writer = pd.ExcelWriter(save_path + '/FILE.xlsx')
df.to_excel(writer)
writer.save()