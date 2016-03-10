# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:30:52 2016

@author: Erin
"""

import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()
loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()
