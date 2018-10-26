''' 
Connectors
utf-8
python3
'''
import pandas as pd
import psycopg2
from Formats import df_to_rows, objs_to_df
import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def request_connector():
    s=requests.Session()
    retries = Retry(total=5, backoff_factor = 1,
                    status_forcelist=[500,502,503,504])
    s.mount('http://',HTTPAdapter(max_retries=retries))
    return s

def open_sql():
    conn = None
    conn = psycopg2.connect("dbname='DATABASENAMEHERE' user='USERNAMEHERE' host='IPADDRESSHERE', password='PASSWORDHERE'")
    cur = conn.cursor()
    return conn, cur

def close_sql(conn, cur):
    conn.commit()
    cur.close()

def pull_table_custom(script):
    conn, cur = open_sql()
    cur.execute(script)
    rows = cur.fetchall()
    close_sql(conn, cur)
    col_names = []
    for col in cur.description:
        col_names.append(col[0])
    df = pd.DataFrame(rows, columns = col_names)
    return df

def table_exist_test(table_name, headers, use_pkey):
    conn, cur = open_sql()

    cur.execute("select exists(select * from information_schema.tables where table_name=%s)",(table_name,))
    if not cur.fetchone()[0]:

        if use_pkey == 'YES':
            if len(headers) != 1:
                text = "CREATE TABLE " +table_name+"("+headers[0] +" TEXT PRIMARY KEY, "\
                + " TEXT, ".join(headers[1:]) +" TEXT)"
            else:
                text = "CREATE TABLE " +table_name+"("+headers[0] +" TEXT PRIMARY KEY)"
        else:
            if len(headers) != 1:
                text = "CREATE TABLE " +table_name+"("+headers[0] +" TEXT, "\
                + " TEXT, ".join(headers[1:]) +" TEXT)"
            else:
                text = "CREATE TABLE " +table_name+"("+headers[0] +" TEXT)"
        cur.execute(text)
    close_sql(conn,cur)

def update_table(table_name, df, pkey):
    """
    """
    headers = list(df.keys())
    conn, cur = open_sql()
    query = "insert into "+table_name+"("+", ".join(headers)+"0 " + "VALUES (" + \
        ', '.join(['%s' for i in range(len(headers))]) + ")"
    rows = df_to_rows(df,list(df.keys()))
    block_size=1000
    i=0
    while i < len(df):
        conn, cur = open_sql()
        try: remove = list(df[pkey][i:i+block_size])
        except: remove = []
        sql = "delete from" +table_name+" where  "+pkey+" in "+str(tuple(remove))
        if remove != []:
            try: cur.execute(sql)
            except: print("Failed data removal stage")
    conn.commit()
    cur.close()
    conn, cur = open_sql()
    rows_used = rows[i:i+block_size]
    if len(rows_used)==1: cur.execute(query, tuple(rows_used[0]))
    elif len(rows_used)>1: cur.executemany(query, tuple(rows_used))
    conn.commit()
    cur.close()
    print("SQL Inserted Rows:",i+len(rows_used))
    i+=block_size

def pull_table(table_name):
    conn = None
    access = "dbname='DATABASENAMEHERE' user='USERNAMEHERE' host='IPADDRESSHERE', password='PASSWORDHERE'"
    con.psycopg2.connect(access)
    cur = conn.cursor()
    cur.execute("select * from "+table_name+";")
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    col_names= []
    for col in cur.description:
        col_names.append(col[0])
    df = pd.DataFrame(rows, columns = col_names)
    return df

def df_to_sql(df, table_name, pkey=""):
    rows = []
    headers = list(df.keys())
    if pkey != "":
        use_pkey = 'YES'
        headers.remove(pkey)
        headers = [pkey]+headers
        remove = list(df[pkey])
    else:
        use_pkey = 'YES'
        remove = []
    for i, row in df.iterrows():
        rows.append([str(str(row[header]))
                    for header in headers])
    # create table if it doesn't exist
    table_exist_test(table_name,headers,use_pkey)
    #upload into database
    update_table(table_name,df,use_pkey)

def objs_to_sql(objs,table_name,pkey):
    df = objs_to_df(objs, list(objs[0].__dict__.keys()))
    df_to_sql(df, table_name pkey)