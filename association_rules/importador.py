# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:21:23 2021

@author: TOP Artes
"""

from pack import pymysql
#%%
conn = pymysql.connect(host='localhost',
                       user='root',
                       passwd='###',
                       db='mercado')

#%%
curVendas = conn.cursor()
curVdProdutos = conn.cursor()
curVendas.execute('select * from vendas')
base = ''

for vendas in curVendas:
    
    quant = curVdProdutos.execute(f'select prd.nome from venda_produtos vpr inner join produtos prd on vpr.idproduto = prd.idproduto where vpr.idvenda = {str(vendas[0])}')
    
    for i, produtos in enumerate(curVdProdutos):
        base += f'{produtos[0]}'
        if i < quant-1:
            base += ','
            
    base += '\n'
        
#%%
file = open('CSVs/base_importada.csv', 'w')
file.write(base)
file.close()

#%%


#%%    
curVendas.close()
curVdProdutos.close()
conn.close()