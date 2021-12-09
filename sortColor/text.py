#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 11:09:25 2021

@author: pol
./TextColor-Map.xlsx
"""

from pandas import *


color_df = pandas.read_excel('./TextColor-Map.xlsx')
values = color_df.to_dict('records')

#print(cities[1]['TextColor'])

myDict = {}

#print(len(cities))

for i in range(len(values)):
    myDict[values[i]['TextColor']] = values[i]['Value']
    
print(myDict)