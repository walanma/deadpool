# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 20:57:48 2017

@author: Alan Ma
"""

import glob
import csv
import pandas as pd
import numpy as np
path =r'C:\Github\dp\internal\deadpooldata'
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
#Cleaning data
for file_ in allFiles:
    
    #grabbing pharmacy name from csv data -- usually first value line 2
    with open(file_) as csvfile:
        readCSV = csv.reader(csvfile)
        value = []
        for line in readCSV:
            value.append(line)
        for v in value[1]:
            if v != "":
                pharmacy_name = v
            
                print(pharmacy_name)
    
    df = pd.read_csv(file_, \
                     skiprows=9, \
                     names=['Pharmacode', 'Product', 'Locn','Pack Size','Manf', 'SO', 'SOH', 'Adj','W/S Price', 'SOH Value'],\
                )
#dropping unneccessary columns
    del df['Locn']
    del df['Manf']
    del df['Adj']
    del df['SO']

#inserting a column
    df.insert(0, "Store Name", pharmacy_name)
#rearrange columns
    df = df[['Store Name','Product', 'Pharmacode', 'Pack Size', 'SOH', 'W/S Price', 'SOH Value']]
#dropping unneeded rows from multiple pages
    df2 = df[pd.notnull(df['SOH'])]
    df3 = df2[df.Product != ' Product']
#default sort
    df4 = df3.sort_values('SOH Value', ascending=False)
    list_.append(df4)
frame = pd.concat(list_)
frame.to_csv('C:\Github\dp\internal\deadpool\data\DeadStockData.csv', index = False)

#getting number of unique pharmacies
unique_pharmacies = frame['Store Name'].nunique()
#getting Total SOH Value for all pharmacies
#print(unique_pharmacies)
Total_SOH_Value = frame['SOH Value'].astype(float)
TSH = Total_SOH_Value.sum()
rounded_total = round(TSH,2)
#print(rounded_total)
#Reading index.html and editing html to replace phrases
import urllib.request
page = urllib.request.urlopen("file:///Github/dp/internal/local_index.html")
text = page.read().decode("utf8")
x = str(unique_pharmacies)
y = "$" + str(rounded_total)
z = text.replace("Blurb", x + " Pharmacies: " + y + " Dead stock") 
with open("c:\Github\dp\internal\deadpool\index.html", "w") as output:
    output.write(z)
