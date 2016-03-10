# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:17:33 2016

@author: Erin
"""

import collections

import matplotlib.pyplot as plt
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
c = collections.Counter(x)

print(c)
count_sum = sum(c.values())
#frequencies
for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))
#boxplot
plt.boxplot(x)
plt.savefig("boxplot.png")

#qq
plt.figure()
test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("qq.png") 
#histogram
plt.hist(x, histtype='bar')
plt.savefig("histogram.png")