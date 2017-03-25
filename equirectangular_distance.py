#!/usr/bin/env python
import numpy as np
import pickle

inputs = 'Ames, IA and Kansas City, MO'

cities = inputs.split()
city1 = ' '.join(cities[:cities.index('and')])
city2 = ' '.join(cities[cities.index('and')-len(cities)+1:])
print city1
print city2

with open ('major_cities_data', 'rb') as f1:
    city_dict = pickle.load(f1)

(lat1, long1) = city_dict[city1]
(lat2, long2) = city_dict[city2]
##print lat1,lat2,long1,long2
tmp = np.absolute(long1-long2) * np.cos((lat1+lat2)/2)
equirectangular_distance = 3961 * np.sqrt(np.square(tmp) + np.square(lat1-lat2))
print equirectangular_distance
