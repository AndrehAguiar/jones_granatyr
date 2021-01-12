# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:48:24 2021

@author: TOP Artes
"""

#%%
import pandas as pd
from pack.apyori import apriori

#%%
data = pd.read_csv('CSVs/mercado2.csv', header = None)
 
#%%
transactions = []
for i in range(0, data.shape[0]):
    transactions.append([str(data.values[i, j]) for j in range(0, data.shape[1])])
    
#%%
rules = apriori(transactions,
                min_support = 0.003,
                min_confidence = 0.2,
                min_lift = 3.0,
                min_lenght = 2)
results = list(rules)

#%%
result = [list(x) for x in results]

#%%
formatted_result = []
for j in range(0, 3):
    formatted_result.append([list(x) for x in result[j][2]])
    
print(formatted_result)
#%%
