#!/usr/bin/env python
import numpy as np
import pickle

tr = np.pi/180
city_dict = {}
with open('major_cities.tsv','r') as f1:
    for line in f1:
        w = line.split()
        location = (float(w[-2])*tr, float(w[-1])*tr)
        city_dict[' '.join(w[:-2])] = location
with open('major_cities_data', 'wb') as g1:
    pickle.dump(city_dict, g1)


sensor_dict = {}
with open('sensor.tsv','r') as f2:
    for line in f2:
        w = line.split()
        location = (float(w[-2])*tr, float(w[-1])*tr)
        sensor_dict[' '.join(w[0:2])] = location
with open('sensor_data', 'wb') as g2:
    pickle.dump(sensor_dict,g2)
