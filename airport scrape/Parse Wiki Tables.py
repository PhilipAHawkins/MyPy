# geopy times out but otherwise this works.
import string
import pandas as pd
import requests
from bs4 import BeautifulSoup

def parse_html_table(table):
    n_columns = 0
    n_rows=0
    column_names = []

    # Find number of rows and columns
    # we also find the column titles if we can
    for row in table.find_all('tr'):
        
        # Determine the number of rows in the table
        td_tags = row.find_all('td')
        if len(td_tags) > 0:
            n_rows+=1
            if n_columns == 0:
                # Set the number of columns for our table
                n_columns = len(td_tags)
                
        # Handle column names if we find them
        th_tags = row.find_all('th') 
        if len(th_tags) > 0 and len(column_names) == 0:
            for th in th_tags:
                column_names.append(th.get_text())

    # Safeguard on Column Titles
    if len(column_names) > 0 and len(column_names) != n_columns:
        raise Exception("Column titles do not match the number of columns")

    columns = column_names if len(column_names) > 0 else range(0,n_columns)
    df = pd.DataFrame(columns = columns,
                      index= range(0,n_rows))
    row_marker = 0
    for row in table.find_all('tr'):
        column_marker = 0
        columns = row.find_all('td')
        for column in columns:
            df.iat[row_marker,column_marker] = column.get_text()
            column_marker += 1
        if len(columns) > 0:
            row_marker += 1 
            
    # Convert to float if possible
    for col in df:
        try:
            df[col] = df[col].astype(float)
        except ValueError:
            pass
    
    return df

page_no = 0
df_out = None
print("df")
master_list = []
while page_no < 26:
    url = "https://en.wikipedia.org/wiki/List_of_airports_by_IATA_code:_"
    letter = string.ascii_uppercase[page_no]
    r = requests.get(url + letter)
    soup = BeautifulSoup(r.text, 'html.parser') # Parse the HTML as a string
    my_table = soup.find("table", {"class" : 'wikitable'})
    master_list.append(parse_html_table(my_table))
    page_no+=1
df_out = pd.concat(master_list, ignore_index = True)
writer = pd.ExcelWriter('out.xlsx')
df_out.to_excel(writer)
writer.save()