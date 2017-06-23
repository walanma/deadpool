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
initial_frame = pd.DataFrame()
list_ = []
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
#Cleaning data from here    
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
    df3 = df2[df2.Product != ' Product']   
    list_.append(df3)
initial_frame = pd.concat(list_)
initial_frame.to_csv('C:\Github\dp\internal\deadpool\data\DeadStockData.csv', index = False)

#Exclude CDs
cd = [2294524, 2452715, 2383926, 2194767, 2452715]
combined_df = pd.read_csv('C:\Github\dp\internal\deadpool\data\DeadStockData.csv')
no_df = combined_df[~combined_df['Pharmacode'].isin(cd)]
#default sort
sorted_df = no_df.sort_values('SOH Value', ascending=False)
sorted_df.to_csv('C:\Github\dp\internal\deadpool\data\DeadStockData.csv', index = False)


#getting number of unique pharmacies
unique_pharmacies = sorted_df['Store Name'].nunique()
#getting Total SOH Value for all pharmacies
#print(unique_pharmacies)
Total_SOH_Value = sorted_df['SOH Value'].astype(float)
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
