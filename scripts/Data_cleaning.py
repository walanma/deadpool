# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 20:57:48 2017

@author: water
"""
#grabbing pharmacy name from csv data -- usually first value line 2
import csv
with open('test.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    value = []
    for line in readCSV:
        value.append(line)
    for v in value[1]:
        if v != "":
            pharmacy_name = v

#Cleaning data
import pandas as pd
import numpy as np
df = pd.read_csv('c:\Github\dp\internal\deadpool\data\merge_raw.csv', \
#           skiprows=9, \
           names=['Pharmacode', 'Product', 'Pack Size', 'SOH', 'W/S Price', 'SOH Value'],\
                )
#inserting a column
df.insert(0, "Store Name", pharmacy_name)
#rearrange columns
df = df[['Store Name','Product', 'Pharmacode', 'Pack Size', 'SOH', 'W/S Price', 'SOH Value']]
#dropping unneeded rows from multiple pages
df2 = df[pd.notnull(df['SOH'])]
df3 = df2[df.Pharmacode != 'PCode']
df4 = df3[df.Product != 'Unnamed: 1']
df4.to_csv('c:\Github\dp\internal\deadpool\data\DeadStockData.csv', index=False)

#getting number of unique pharmacies
unique_pharmacies = df4['Store Name'].nunique()
#getting Total SOH Value for all pharmacies
print(unique_pharmacies)
Total_SOH_Value = df4['SOH Value'].astype(float)
TSH = Total_SOH_Value.sum()
rounded_total = round(TSH,2)

#Reading index.html and editing html to replace phrases
import urllib.request
page = urllib.request.urlopen("file:///Github/dp/internal/local_index.html")
text = page.read().decode("utf8")
x = str(unique_pharmacies)
y = "$" + str(rounded_total)
z = text.replace("Blurb", x + " Pharmacies: " + y + " Dead stock") 
with open("c:\Github\dp\internal\deadpool\index.html", "w") as output:
    output.write(z)