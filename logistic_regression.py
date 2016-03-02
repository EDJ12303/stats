# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:36:16 2016

@author: Erin
"""
import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData['Interest.Rate'][0:5] 
loansData['Loan.Length'][0:5]
loansData['FICO.Range'][0:5]

#remove % from interest rate
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
type(cleanInterestRate)

cleanInterestRate[0:5]

loansData['Interest.Rate'] = cleanInterestRate
loansData['Interest.Rate'][0:5]


# Loan.Length and FICO.Range
loansData['Loan.Length'][0:5]

cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
cleanLoanLength[0:5]

loansData['Loan.Length'] = cleanLoanLength
loansData['Loan.Length'][0:5]

 # FICO.Range
loansData['FICO.Range'][0:5]


cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFICORange[0:5]

cleanFICORange[0:5].values[0]
['735', '739']
type(cleanFICORange[0:5].values[0])

cleanFICORange[0:5].values[0][0]

type(cleanFICORange[0:5].values[0][0])

cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])
cleanFICORange[0:5]

type(cleanFICORange[0:5].values[0])

loansData['FICO.Score'] = cleanFICORange.values[0][0]
loansData['FICO.Score'][0:5]
loansData['FICO.Score'][0:5]


import numpy as np
import pandas as pd
import statsmodels.api as sm

#load data to dataframe
df = pd.read_csv('loansData_clean.csv')
df['Interest.Rate']
print df['Interest.Rate'][0:5]

#create column IN_TF that indicates whether or not Interest.Rate is greater or equal to 0.12
loansData['IN_TF'] = loansData['Interest.Rate'].map(lambda x: [bool(x >= 0.12)])
print loansData['IN_TF'][0:5]

#add intercept column
intercept = [1] * len(loansData)
loansData['Intercept'] = intercept

#list of column names of independent variables (including intercept)
ind_vars = ['FICO.Score', 'Amount.Requested', 'Intercept']

df=loansData

#logistic function
#define model
logit = sm.Logit(df['IN_TF'].tolist(), df[ind_vars])

#fit the model
result = logit.fit(maxiter=100)


#get the fitted coefficient from the results
coeff = result.params
print "coefficients are:"
print "coeff[0]="
print (coeff.values[0])
print "coeff[1]="
print (coeff.values[1])
print "coeff[2]="
print (coeff.values[2])

#Coefficients example: interest_rate = −60.125 + 0.087423(FicoScore) − 0.000174(LoanAmount)
#logistic function p(x) = 1/(1 + e^(intercept + 0.087423(FicoScore) − 0.000174(LoanAmount))
#Write a function called logistic_function that will take a FICO Score and a Loan Amount of this linear predictor, and return p. (Try not to hardcode any values if you can! Hint: pass the coefficients object to the function as an argument.)
def logistic_function(FicoScore, LoanAmount, coeff):
    prob = 1/(1 + np.exp(coeff[0] + coeff[1]*FicoScore - coeff[2]*LoanAmount))
    if prob > 0.7:
        p = 1
        print "we predict that the sub-12% loan will be approved"
    else:
        p = 0
        print "we predict that the sub-12% loan will not be approved"
        
    return prob, p

prob = logistic_function(720, 10000, coeff)[0]
print "probability is:"
print prob


    
    

        