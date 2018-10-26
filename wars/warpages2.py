from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

time_groups = ["before_1000", "1000-1499", "1500-1799", "1800-99","1900-44", "1945-89",
"1990-2002", "2003-10", "2011-present"]
page_no = 0
while page_no < 9:
    print("Page: ", page_no)
    prefix = "https://en.wikipedia.org/wiki/List_of_wars_"
    this_page = time_groups[page_no]
    url = prefix + this_page
    with urlopen(url) as f:
        sp = BeautifulSoup(f, 'lxml') 
        tb = sp.find('table', {"class":"wikitable"})
        """ shouldn't need the below since all pages do use a wikitable class
        if not page_no == 3 | 6:
            tb = sp.find('table', {"class":"wikitable"})
        else:
            tb = sp.find('table', {"class":"wikitable sortable jquery-tablesorter"})
        """
        print("tables found: ", len(tb))
        r = pd.read_html(str(tb), encoding='utf-8', header=0)
        df = pd.concat(r, ignore_index=True)
        print(df.head(5))
        # need to iterate through 
        link_list=[]
        for tables in tb:
            for row in table.find_All('tr')[1:]:
                my_link =  row.find_All('href')[2]
                link_list.append(my_link.text)
        # df['href'] = [np.where(tag.has_attr('href'),tag.get('href'),"no link") for tag in tb.find('a')]
        df['href'] = link_list
        writer = pd.ExcelWriter(this_page + '.xlsx')
        df.to_excel(writer)
        writer.save()
    page_no+=1