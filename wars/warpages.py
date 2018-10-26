import string
import pandas as pd

time_groups = ["before_1000", "1000-1499", "1500-1799", "1800-99","1900-44", "1945-89",
"1990-2002", "2003-10", "2011-present"]
page_no = 0
df_out = pd.DataFrame() 
df=pd.DataFrame()
while page_no < 9:
    print(page_no)
    url = "https://en.wikipedia.org/wiki/List_of_wars_"
    letter = time_groups[page_no]
    r = pd.read_html(url + letter)
    df = pd.concat(r, ignore_index=True)
    writer = pd.ExcelWriter(letter + '.xlsx')
    df.to_excel(writer)
    writer.save()
    page_no+=1
