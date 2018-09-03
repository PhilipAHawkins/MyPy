# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:46:17 2018

@author: phhawkins
Read a list of starting and ending points on a trip and generate midpoints
to be manually adjusted in Excel as the user sees fit.
"""

import pandas as pd

def increment (w,x,y):
    return ((w-x)/y)

# read
file = r'C:\Users\phhawkins\Documents\My Tableau Repository\Datasources\curv plz.xlsx'
df = pd.read_excel(file)
midpoints = 6

# lists
Latitudes = []
Longitudes= []
Trip = []
Point = []

# construct
for x in range(0,len(df)):
    i_lat = increment(
            df.EndLat[x], 
            df.Lat[x], 
            midpoints)
    i_long = increment(
            df.EndLong[x], 
            df.Long[x], 
            midpoints)
    print(i_lat,", ",i_long)
    for i in range(0,midpoints+1):
        Trip.append(df.Trip[x])
        Point.append(i+1)
        if i == 0:
            Latitudes.append(df.Lat[x])
            Longitudes.append(df.Long[x])
        else:
            Latitudes.append(Latitudes[len(Latitudes)-1] + i_lat)
            Longitudes.append(Longitudes[len(Longitudes)-1] + i_long)

# table
df_out = pd.DataFrame({"Trip":Trip,
                       "Point":Point,
                       "Latitudes":Latitudes,
                       "Longitudes":Longitudes})
# write
writer = pd.ExcelWriter('out.xlsx')
df_out.to_excel(writer)
writer.save()
