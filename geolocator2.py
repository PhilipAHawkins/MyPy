# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:44:32 2018

@author: phhawkins
"""

import pandas as pd
from geopy.geocoders import Nominatim
# import time
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



my_list = ['Al Hamra, Oman', 'Al Nakhil, united arab emirates',
           'al tji, iraq', 'amman, jordan', 'amundsen-scott south pole station, antarctica',
           'azraq, jordan', 'bald, iraq', 'british indian ocean territory', 'diffa, niger',
           'doha, qatar', 'duqm, oman', 'eureka springs, arkansas', 'hawaii', 'iwakuni, honshu',
           'iwo jima, usa', 'kuwait city', 'mcmurdo station, ross islands, cocos islands', 
           'menzel abderrahmen, tunisia', 'misurata, libya', 'qayyarah west, iraq',
           'riyadh', 'roberts massif, antarctica', 'semarang, indonesia', 'siple coast, antarctica',
           'sitrah, bahrain', 'waku kungo, angola', 'waynesboro, virginia']
latitude = []
longitude = []
for x in my_list:
    print(x)
    if my_geo(x,'') != None:
        try:
            latitude.append(geolocator.geocode(x, timeout=10).latitude)
            longitude.append(geolocator.geocode(x, timeout=10).longitude)
        except:
            latitude.append('')
            longitude.append('')
            
df = pd.DataFrame({"list":my_list,
                   "Latitude":latitude,
                   "Longitude":longitude})
