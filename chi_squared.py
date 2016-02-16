# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:58:32 2016

@author: Erin
"""

from scipy import stats
import collections

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()
chi, p = stats.chisquare(freq.values())
print "chi-square value is:"
print chi
print "p value is:"
print p
print "if the p value is less than the significance level of 0.05, we reject the null hypothesis and conclude that the data follows the chi-square distribution"
