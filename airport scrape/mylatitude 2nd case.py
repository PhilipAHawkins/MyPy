# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 23:40:27 2018

@author: phhawkins
Receives a workbook of trips with multiple legs- one leg per row with the destination as the next leg
Returns Great Arc midpoints on the path between each leg to then visualize in Tableau.
Performs (for free) the same work that Alteryx would do (for a license cost)
Lat	          Long	   Trip	leg
36.802832	   -90.70462	   4	1
-17.49797	   -42.02926	   3	1
-18.53424	   46.792609	   1	1
-11.6	      15.1	          2	1
31.62577	   65.71448	   4	2
-35.012977   138.58624	   3	2
40.843372	   -2.399087	   1	2
38.540481	   42.203735	   2	2
"""

import math
import pandas as pd

file = r'C:\Users\phhawkins\Documents\My Tableau Repository\Datasources\Data.xlsx'
df = pd.read_excel(file)
pointLat = []
pointLon = []
trip = []
path = []
m = 400 # Change to your desired midpoint output

for t in range(1, len(df)):
    this_trip = df[df.Trip == t].reset_index(0) # subset df of our trip to manipulate
    if len(this_trip) > 0:
        for i in range(0,len(this_trip)-1):
            Lat1 = this_trip.Lat[i] 
            Lon1 = this_trip.Long[i]
            Lat2 = this_trip.Lat[i+1]
            Lon2 = this_trip.Long[i+1]
            # determine a distance between the two points on an arc cosine.
            d = math.acos(
                    math.sin(math.radians(Lat1))*math.sin(
                            math.radians(Lat2))+math.cos(
                                    math.radians(Lat1))*math.cos(
                                            math.radians(Lat2))*math.cos(
                                                    math.radians(Lon1)-math.radians(Lon2)))
            # For every midpoint, calculate the following:
            for f in range(m + 1):
                a = math.sin((1-f/m)*d)/math.sin(d)
                b = math.sin((f/m)*d)/math.sin(d)
                x = a*math.cos(
                        math.radians(Lat1))*math.cos(
                                math.radians(Lon1))+b*math.cos(
                                        math.radians(Lat2))*math.cos(
                                                math.radians(Lon2))
                y = a*math.cos(
                        math.radians(Lat1))*math.sin(
                                math.radians(Lon1))+b*math.cos(
                                        math.radians(Lat2))*math.sin(
                                                math.radians(Lon2))
                z = a*math.sin(math.radians(Lat1)) + b*math.sin(math.radians(Lat2))
                # and therefore:
                pointLat.append(
                        math.degrees(
                            math.atan2(
                                    z, math.sqrt(
                                            math.pow(x,2)+math.pow(y,2)))))
                pointLon.append(math.degrees(math.atan2(y,x)))
                trip.append(df.Trip[t])
                path.append(f)

df_out=pd.DataFrame({"Trip":trip,"Lats":pointLat,"Lons":pointLon, "Path":path})
# write
writer = pd.ExcelWriter('great arc out version 2.xlsx')
df_out.to_excel(writer)
writer.save()
"""
In Tableau, do the following:
    Use the Lats and Lons generated here instead of Tableau's provided ones
    Set Trip to Detail, mark type to Line, and Path to line Path
"""

            