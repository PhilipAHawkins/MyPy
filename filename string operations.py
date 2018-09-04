# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:49:33 2018

@author: phhawkins
"""

import pandas as pd

double_quotes = "C:\\Users\phhawkins\Documents\Python Scripts\Crimes.csv"
r_single_quotes = r'C:\Users\phhawkins\Documents\Python Scripts\Crimes.csv' 
forwards = "C:/Users/phhawkins/Documents/Python Scripts/Crimes.csv"

df1 = pd.read_csv(forwards)
temp = pd.DataFrame(df1)
df2 = temp[['primary type','date']]
print(temp.head)