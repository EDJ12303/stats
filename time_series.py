# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 21:21:32 2016

@author: Erin
"""

import pandas as pd
import numpy as np 
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

df = pd.read_csv('LoanStats3b.csv', header=1, low_memory=False)
print df.head()
print df['issue_d'][0:10]

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

#plot loan_count_summary to see if it's stationary series
loan_count_summary.plot()

#output indicates non-stationary series because there is an upward trend
#need to transform it into a stationary series through differencing
loan_count_log_diff = loan_count_summary - loan_count_summary.shift()
loan_count_log_diff.plot()

#plot the ACF of the transformed series
sm.graphics.tsa.plot_acf(loan_count_log_diff, alpha=0.05)

#plot the PACF of the transformed series
sm.graphics.tsa.plot_acf(loan_count_log_diff, alpha=0.05)

#no autocorrelation structures or trends are observed