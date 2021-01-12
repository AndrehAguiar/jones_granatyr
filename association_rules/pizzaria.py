# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:25:35 2021

@author: TOP Artes
"""

#%%
import pandas as pd
from pack.apyori import apriori

#%%
data = pd.read_csv('CSVs/base_pizzaria.csv', header = None)
 
#%%
del data[3] # Delete borda
del data[4] # Delete refrigerante

#%%
transactions = []
for i in range(0, data.shape[0]):
    transactions.append([str(data.values[i, j]) for j in range(0, data.shape[1])])
    
#%%
rules = apriori(transactions,
                min_support = 0.062,
                min_confidence = 0.2,
                min_lift = 1.2,
                min_lenght = 2)
results = list(rules)

#%%
result = [list(x) for x in results]

#%%

formatted_result = []
for j in range(0, 3):
    formatted_result.append([list(x) for x in result[j][2]])
    
    
"""forzenset({item_1, ..., item_n}, support, lift)"""
    
print(*formatted_result, sep='\n\n')
#%%