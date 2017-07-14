# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 10:19:28 2017

@author: water
"""

#Reading index.html and editing html to replace phrases
import urllib.request
page = urllib.request.urlopen("file:///Github/dp/internal/deadpool/index.html")
text = page.read().decode("utf8")
x = str(unique_pharmacies)
y = "$" + str(rounded_total)
z = text.replace("Blurb", x + " Pharmacies. " + y + " Dead stock.") 
with open("c:\Github\dp\internal\deadpool\index.html", "w") as output:
    output.write(z)