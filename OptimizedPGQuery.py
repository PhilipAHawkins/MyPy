import datetime
import pandas as pd
import psycopg2
from sqlalchemy Import create_engine
 
start = datetime. Datetime.now()
engine = create_engine(‘postgres+psycopg2://’username + ‘:’ + password + “@” + host+ ‘:5432’ + db_name + use_bath_mode=True)
 
con=engine.raw_connection()
cur = con.cursor()
 
sql1 = “””select * from schema.table order by fid asc limit 1”””
cols =  pd.read_sql(sql1, engine).columns
 
sql = “”” COPY (SELECT * FROM schema.table ORDER BY FID ASC LIMIT 1000000) TO STDOUT WITH CSV DELIMITER ‘,’; “””
 
with open(‘data.csv’, ‘w’) as f:
  For x in cols:
    If x!= ‘Date’:
      f.write(str(x) + “,”)
    else:
      f.write(str(x))
  f.write(“\n”) # this may ne indented wrong because Outlook added lines.

with open(‘data.csv’,’w’) as f:
  cur.copy_expert(sql,f)
 
print(datetime. Datetime.now() – Start)
