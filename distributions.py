# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:17:33 2016

@author: Erin
"""

import collections

testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)

print(c)

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))
  
  import matplotlib.pyplot as plt
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.show()
plt.hist(x, histtype='bar')
plt.show()