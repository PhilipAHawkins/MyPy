from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

"""
Why bother dumping one dataframe after another into a big one and lose all the links in the process?
Why not just yank out the HTML, cast it to str, and write it as XML to be touched up in Excel?


Issue: 1000-1499 NS 1500-1799
"""

prefix = "https://en.wikipedia.org/wiki/List_of_wars_"
time_groups = ["before_1000", "1000-1499", "1500-1799", "1800-99","1900-44", "1945-89",
"1990-2002", "2003-10", "2011-present"]
page_no = 0
my_xml_file=""
while page_no < 9:
    prefix = "https://en.wikipedia.org/wiki/List_of_wars_"
    this_page = time_groups[page_no]
    url = prefix + this_page
    with urlopen(url) as f:
        sp = BeautifulSoup(f, 'lxml') 
        #tb = sp.find('table', {"class":"wikitable"})
        tb = sp.find_all('table', {"class":"wikitable"})
        my_xml_file+=str(tb)
    page_no+=1
dump_file=open('war_list.xml', 'w', encoding='utf-8')
dump_file.write(my_xml_file)
