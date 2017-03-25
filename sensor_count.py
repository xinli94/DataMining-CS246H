#!/usr/bin/env python
import numpy as np
import pickle

city = 'Providence, RI'

with open ('major_cities_data', 'rb') as f1:
    city_dict = pickle.load(f1)
with open('sensor_data', 'rb') as f2:
    sensor_dict = pickle.load(f2)

cnt = 0
(lat1, lon1) = city_dict[city]
for sensor in sensor_dict:
##    print sensor, sensor_dict[sensor]
    (lat2, lon2) = sensor_dict[sensor]
    cos_dist = np.arccos( np.sin(lat1)*np.sin(lat2)+np.cos(lat1)*np.cos(lat2)\
                          *np.cos(lon2-lon1) )*3961
    if cos_dist < 50:
        cnt += 1

print city ,': ',cnt                
