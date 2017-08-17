
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 21:35:22 2017
@author: water
"""
import pandas as pd
df1 = pd.read_csv(r'C:\Github\dp\internal\firebase\stock\DeadStockData.csv')
df2 = pd.read_csv(r'C:\Github\dp\internal\firebase\stock\Input.csv')
cols = ['Store Name','Product','Pharmacode','Pack Size','SOH', 'W/S Price', 'SOH Value']
d2 = df2.set_index(cols).Expiry.dropna()

#print(d2)
df3 = df1.fillna(df1.drop('Expiry', 1).join(d2, on=cols))
df4 = df3[pd.notnull(df3['SOH Value'])]
df4.insert(8, "Comments", "")
#
##print(df4)
df4.to_csv(r'C:\Github\dp\internal\firebase\stock\DeadStockData.csv', index=False)
df4.to_csv(r'C:\Github\dp\internal\firebase\stock\Input.csv', index=False)

#print(df3)