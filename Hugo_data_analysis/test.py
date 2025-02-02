# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:53:08 2019

@author: hkohli
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('..\Bidirectional_interface\Assets\Logs')
d = os.listdir('.')
data = pd.read_csv('2_08_47__Visual.csv')
t = data['time']

plt.plot(t, data['position_x'])
plt.plot(t, data['position_y'])
plt.plot(t, data['position_z'])

plt.plot(data['time'])

for x in list(data):
    plt.figure()
    plt.plot(data[x])
    plt.title(x)