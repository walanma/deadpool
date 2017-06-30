# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 21:35:22 2017

@author: water
"""
import pandas as pd
df1 = pd.read_csv('C:\Github\dp\internal\deadpool\data\DeadStockData.csv')
df2 = pd.read_csv('C:\Github\dp\internal\deadpool\data\Input.csv')
cols = ['Store Name','Product','Pharmacode','Pack Size','SOH', 'W/S Price', 'SOH Value']
d2 = df2.set_index(cols).Expiry.dropna()
#print(d2)
df3 = df1.fillna(df1.drop('Expiry', 1).join(d2, on=cols))
d4 = df2.set_index(cols).Comments.dropna()
df4 = df3.fillna(df3.drop('Comments', 1).join(d4, on=cols))
#print(df4)
df4.to_csv('C:\Github\dp\internal\deadpool\data\DeadStockData.csv', index=False)
df4.to_csv('C:\Github\dp\internal\deadpool\data\Input.csv', index=False)

#print(df3)