# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 15:51:41 2016

@author: Erin
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import csv

#load Loan Statistics
df_loan= pd.read_csv('LoanStats3d.csv', low_memory=False)

#Create Intercept 
df_loan['Intercept'] = float(1.0)

#remove % from interest rate
df_loan['int_rate'] = df_loan['int_rate'].str.rstrip('%').astype(float).round(4)/100
print df_loan['int_rate'][0:10]

#use annual_inc to model int_rate
#extract columns
X =df_loan[['Intercept','annual_inc']]
y =df_loan['int_rate']

df_loan.head()
print "df_loan.head"
print df_loan.head()

#create model
X = sm.add_constant(X)
model = sm.OLS(y,X)
f = model.fit()
# output results summary
print "f.summary"
print f.summary()

#add home ownership to the model
#home ownership categorical
#encode home_ownership as a numeric via pd.Factor
df_loan['home_ownership_ord'] = pd.Categorical(df_loan.home_ownership,categories={'OWN':1,'MORTGAGE':2,'RENT':3}).codes
df_loan.dropna(subset=['home_ownership_ord'])
print df_loan['home_ownership_ord'][0:20]


X1= df_loan[['Intercept','annual_inc','home_ownership_ord']]
y = df_loan['int_rate']

## fit a OLS model with intercept on annual_inc and home_ownership
X2= sm.add_constant(X1)
model = sm.OLS(y, X2, missing='drop')
est = model.fit()
print "est.summary"
print est.summary()

#add the interaction of home ownership and incomes as a term
df_loan['Interaction'] = df_loan['annual_inc'] * df_loan['home_ownership_ord']

X3 = df_loan[['Intercept', 'annual_inc', 'home_ownership_ord', 'Interaction']]
model2 = sm.OLS(y, X3, missing='drop')
est2 = model2.fit()
print "est2.summary"
print est2.summary()
