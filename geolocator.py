# -*- coding: utf-8 -*-
"""
read file and add coordinates
the service times out a lot, so this will attempt chunks.

Update: can't o more than 1000 before getting rejected by server.
Also has trouble matching up df indices.
"""
import pandas as pd
from geopy.geocoders import Nominatim
import time

df_start =8210 # just change these two.
df_fin = 8966
out_path = r'C:\Users\phhawkins\Documents\code\Py\airport_out'
in_path = r'C:\Users\phhawkins\Documents\code\Py\airport_in'
my_filename='\Airport_'+str(df_start)+"_"+str(df_fin)+'.xlsx'
df = pd.read_excel(in_path + my_filename)

geolocator = Nominatim()
def my_geo(str1, str2):
    a = ''
    try:
        a = geolocator.geocode(str1, timeout=5)
    except:
        try:
            a = geolocator.geocode(str2, timeout=5)
        except:
            a = None
    if a == None:
        try:
            a = geolocator.geocode(str2, timeout=5)
        except:
            a = None
    if a != None:
        return a
    else: 
        return None
        

Latitude = []
Longitude=[]
for x in range(0,len(df)):
    if my_geo(df['Location\xa0served'][x],df['Airport\xa0name'][x]) != None:
        try:
            Latitude.append(geolocator.geocode(df['Location\xa0served'][x], timeout=10).latitude)
            Longitude.append(geolocator.geocode(df['Location\xa0served'][x], timeout=10).longitude)
        except:
            Latitude.append(geolocator.geocode(df['Airport\xa0name'][x], timeout=10).latitude)
            Longitude.append(geolocator.geocode(df['Airport\xa0name'][x], timeout=10).longitude)
    else:
        Latitude.append('null')
        Longitude.append('null')
    if x % 10 == 0:
        print(x," sleeping...")
        time.sleep(10)
df_latlong = pd.DataFrame({"Latitude":Latitude,
                           "Longitude":Longitude})
df_out = pd.concat([df, df_latlong], axis =1)
writer = pd.ExcelWriter(out_path + my_filename)
df_out.to_excel(writer)
writer.save()