# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:21:15 2017

@author: water
"""
import pandas as pd
import glob
#dropping duplicates
data = pd.concat([pd.DataFrame.from_csv(file, index_col=None) for
                  file in glob.glob("c:\Github\dp\internal\deadpooldata\*.csv")]).drop_duplicates()
data.to_csv('c:\Github\dp\internal\deadpool\data\merge_raw.csv', index=False)
