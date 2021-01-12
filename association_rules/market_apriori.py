# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:38:54 2021

@author: TOP Artes
"""

#%%
import pandas as pd
from pack.apyori import apriori

#%%
data = pd.read_csv('CSVs/mercado.csv', header = None)
 
#%%
transactions = []
for i in range(0, data.shape[0]):
    transactions.append([str(data.values[i, j]) for j in range(0, data.shape[1])])
    
#%%
rules = apriori(transactions,
                min_support = 0.3,
                min_confidence = 0.8,
                min_lift = 2,
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