# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:33:18 2016

@author: yiyuezhuo
"""

import pandas as pd
import matplotlib.pyplot as plt
import powerlaw
import scipy.stats as stats
import numpy as np

data=pd.read_csv("data.csv",encoding="gbk")

col1=data[u'2013年GDP(亿元)']
col2=data[u'较2012年实际增长率'].dropna().map(lambda x:float(x[:-1]))
sc=(col2-np.mean(col2))/np.std(col2)

# powerlaw test

fit=powerlaw.Fit(col1)
R, p = fit.distribution_compare('power_law', 'lognormal')
print 'R',R,'p',p
print "power_law fit is wrong than to lognormal!"

fig4 = fit.plot_ccdf(linewidth=2)
fit.power_law.plot_ccdf(ax=fig4, color='r', linestyle='--')
fit.lognormal.plot_ccdf(ax=fig4, color='g', linestyle='--')
plt.show()

# norm test

des=stats.describe(col2)

omnibus,p_n=stats.normaltest(col2)

print 'p',p_n,'it is not a norm distribution however'

plt.hist(col2)
plt.show()