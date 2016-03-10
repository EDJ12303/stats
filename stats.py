# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 18:36:59 2016

@author: Erin
"""

import pandas as pd

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

from scipy import stats

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print ("The mean values for the Alcohol and Tobacco dataset are:" )
print (df['Alcohol'].mean())
print ("and")
print (df['Tobacco'].mean())
     

print ("The median values for the Alcohol and Tobacco dataset are:")
print (df['Alcohol'].median())
print ("and")
print (df['Tobacco'].median())

modeAlcohol = stats.mode(df['Alcohol'])
modeTobacco = stats.mode(df['Tobacco'])

print ("The mode values for the Alcohol and Tobacco dataset are:")
print modeAlcohol[0]
print ("and")
print modeTobacco[0]

print ("The range values for the Alcohol and Tobacco dataset are:")
print max(df['Alcohol'])- min(df['Alcohol'])
print ("and")
print max(df['Tobacco'])- min(df['Tobacco'])

print ("The variance values for the Alcohol and Tobacco dataset are:")
print (df['Alcohol'].var())
print "and"
print (df['Tobacco'].var())

print ("The standard deviation values for the Alcohol and Tobacco dataset are:")
print (df['Alcohol'].std())
print "and"
print (df['Tobacco'].std())

