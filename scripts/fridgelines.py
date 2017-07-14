# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:57:29 2017

@author: water
"""

#Exclude CD
#List of CDs = external .XLSx file
xls = pd.read_excel('List_of_fridge_lines.xlsx', index_col=0).to_dict()
fridges = {}
fridges = xls['Brand Name']

combined_df = pd.read_csv('C:\Github\dp\internal\deadpool\data\DeadStockData.csv')
counter = -1
highlighted_list = []
for a in combined_df['Pharmacode']: 
    counter += 1
    for b in fridges:        
        if a == b:
            print("Match found")
            combined_df.loc[counter, 'Product'] = (combined_df.loc[counter]['Product'] + " [Fridge Line]")
#print(excluded_list)       
#fo = open("C:\Github\dp\internal\deadpool\data\Excluded_CDs.txt", "w+")  
#line = fo.writelines(excluded_list)
#fo.close()
#no_df = combined_df[~combined_df['Pharmacode'].isin(CDs)]
##default sort
#sorted_df = no_df.sort_values('SOH Value', ascending=False)
combined_df.to_csv('text.csv', index = False)