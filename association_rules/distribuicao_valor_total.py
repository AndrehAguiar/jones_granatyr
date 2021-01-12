# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:15:21 2021

@author: TOP Artes
"""


import matplotlib.pyplot as plt
from numpy import genfromtxt

#%%
data = genfromtxt('CSVs/valor_total.csv')

#%%
histogram = plt.hist(data, bins='sturges')

#%%
histogram = plt.hist(data, bins='scott')

#%%
histogram = plt.hist(data, bins='fd')

#%%
histogram = plt.hist(data, bins=5)
#%%
histogram = plt.hist(data)

#%%
data = genfromtxt('CSVs/tempo_decorrido.csv')

#%%
histogram = plt.hist(data, bins='sturges')

#%%
histogram = plt.hist(data, bins=4)