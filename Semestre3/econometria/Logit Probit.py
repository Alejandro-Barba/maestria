# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:21:36 2021

@author: USER
"""

# Modelo Logit
import statsmodels.api as sm
from pandas import read_csv
series = read_csv('./MAXVERO_base.csv', header=0, index_col=0)
Y = series [['Y']]
X = series [['X1', 'X2', 'X3']]
XC = sm.add_constant(X)
logit_mod = sm.Logit(Y, XC)
logit_res = logit_mod.fit()
print(logit_res.summary())


# Modelo probit
Probit_mod = sm.Probit(Y, XC)
Probit_res = Probit_mod.fit()
print(Probit_res.summary())

mfx = Probit_res.get_margeff(atexog=XC)
print(mfx.summary())


import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
support = np.linspace(-6, 6, 1000)
ax.plot(support, stats.logistic.cdf(support), "r-", label="Logistic")
ax.plot(support, stats.norm.cdf(support), label="Probit")
ax.legend()


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
support = np.linspace(-6, 6, 1000)
ax.plot(support, stats.logistic.pdf(support), "r-", label="Logistic")
ax.plot(support, stats.norm.pdf(support), label="Probit")
ax.legend()