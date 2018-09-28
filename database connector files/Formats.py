"""
works with Connectors.py
"""

import pandas as pd

class Row_To_Obj():
    def __init__(self,row):
        for key in list(row.keys()):
            setattr(self,key,"Null")
            try: setattr(self,key,row[key])
            except: pass

def df_to_objs(df):
    obj_list = [Row_To_Obj(row) for i, row in df.iterrows()]
    return obj_list

def df_to_rows(df, keys):
    rows=[]
    for i, row in df.iterrows():
        rows.append([str(str(row[key])) for key in keys])
    return rows

def obj_to_row(df, keys):
    # rewrites a singular oject as a row
    row=[]
    for column in columns():
        row.append(getattr(obj, column))
    return row

def objs_to_df(obj, columns):
    # rewrites a singular oject as a row
    rows=[obj_to_row(obj, columns) for obj in objs]
    df = pd.DataFrame(rows, columns=columns)
    return df

def out_to_excel(df, output_path, wksht_name, columns):
    # writes a df to Excel file (.xlsx)
    writer = pd.ExcelWriter(output_path,engine='xlsxwriter')
    df.to_excel(writer,wksht_name)
    worksheet = writer.sheets[wksht_name]
    # dynamically set col widths
    column_widths = []
    for column in columns:
        column_widths.append(len(column)+1)
    df_column_list = ['B:B','C:C','D:D','E:E','F:F','G:G','H:H','I:I',
                    'J:J','K:K','L:L','M:M','N:N','O:O','P:P','Q:Q','R:R',
                    'S:S','T:T','U:U','V:V','W:W','X:X','Y:Y','Z:Z','AA:AA',
                    'AB:AB','AC:AC','AD:AD','AE:AE','AF:AF','AG:AG','AH:AH',
                    'AI:AI','AJ:AJ','AK:AK','AL:AL','AM:AM','AN:AN','AO:AO',
                    'AP:AP','AQ:AQ','AR:AR','AS:AS','AT:AT','AU:AU','AV:AV',
                    'AW:AW','AX:AX','AY:AY','AZ:AZ','BA:BA','BB:BB','BC:BC',
                    'BD:BD','BE:BE','BF:BF','BG:BG','BH:BH','BI:BI']
    for column in range(len(columns)):
        worksheet.set_column(df_column_list[column], len(columns[column])+1)
    writer.save()

def objs_to_excel(objs, columns, output_path, tab_name='Data'):
    # writes a lost of objects to xlsx
    df = objs_to_df(objs, columns)
    out_to_excel(df, output_path, tab_name, columns)
    return df


