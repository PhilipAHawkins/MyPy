# -*- coding: utf-8 -*-
"""
Reads a XLS with start & end coordinates on one row and 
turns it into a new file with Great Arc midpoints.

Take the output right to Tableau.

Alteryx is for suckers.
"""

import math
import pandas as pd

file = r'C:\Users\phhawkins\Documents\My Tableau Repository\Datasources\curv plz.xlsx'
df = pd.read_excel(file)

"""
format of the csv read in is as follows:
    
Lat	          Long	   Trip	 EndLat	    EndLong
36.802832	-90.70462	4	31.62577	65.71448
-17.49797	-42.02926	3	-35.012977	138.58624
-18.53424	46.792609	1	40.843372	-2.399087
-11.6	      15.1	    2	38.540481	42.203735

Starting & ending coords are on the same line in this run.
Next task will be to work in data where they're on separate lines.
"""

Lat1 = df.Lat
Lon1 = df.Long
Lat2 = df.EndLat
Lon2 = df.EndLong
ThisTrip = df.Trip
pointLat = []
pointLon = []
trip = []

m = 6 # (it's actually one plus this)
for t in range(len(df)):
    for f in range(m + 1):         
        d = math.acos(
                math.sin(math.radians(Lat1[t]))*math.sin(
                        math.radians(Lat2[t]))+math.cos(
                                math.radians(Lat1[t]))*math.cos(
                                        math.radians(Lat2[t]))*math.cos(
                                                math.radians(Lon1[t])-math.radians(Lon2[t])))
        # For every midpoint, 
        a = math.sin((1-f/m)*d)/math.sin(d)
        b = math.sin((f/m)*d)/math.sin(d)
        x = a*math.cos(
                math.radians(Lat1[t]))*math.cos(
                        math.radians(Lon1[t]))+b*math.cos(
                                math.radians(Lat2[t]))*math.cos(
                                        math.radians(Lon2[t]))
        y = a*math.cos(
                math.radians(Lat1[t]))*math.sin(
                        math.radians(Lon1[t]))+b*math.cos(
                                math.radians(Lat2[t]))*math.sin(
                                        math.radians(Lon2[t]))
        z = a*math.sin(math.radians(Lat1[t])) + b*math.sin(math.radians(Lat2[t]))
        # and therefore:
        pointLat.append(
                math.degrees(
                    math.atan2(
                            z, math.sqrt(
                                    math.pow(x,2)+math.pow(y,2)))))
        pointLon.append(math.degrees(math.atan2(y,x)))
        trip.append(ThisTrip[t])

df_out=pd.DataFrame({"Trip":trip,"Lats":pointLat,"Lons":pointLon})

# write
writer = pd.ExcelWriter('great arc out.xlsx')
df_out.to_excel(writer)
writer.save()
