# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 07:46:17 2018

@author: phhawkins
"""

import string
import pandas as pd

page_no = 0
df_out = None
print("df")
master_list = []
while page_no < 26:
    url = "https://en.wikipedia.org/wiki/List_of_airports_by_IATA_code:_"
    letter = string.ascii_uppercase[page_no]
    r = pd.read_html(url + letter)[0]
    master_list.append(r)
    page_no+=1
df_out = pd.concat(master_list, ignore_index = True)
writer = pd.ExcelWriter('Wiki tables of IATA Code.xlsx')
df_out.to_excel(writer)
writer.save()