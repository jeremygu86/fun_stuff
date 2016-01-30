__author__ = 'wenxiao'

## Ref: http://lifelines.readthedocs.org/en/latest/

import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import scipy

import lifelines

figsize(12.5,5)
np.set_printoptions(precision=2, suppress=True)

from lifelines import KaplanMeierFitter
survival_times = np.array([0.,3.,4.5, 10., 1.])
events = np.array([False, True, True, False, True])

kmf = KaplanMeierFitter()
kmf.fit(survival_times, event_observed=events)

print kmf.survival_function_
print kmf.median_
kmf.plot()


## example 2
import matplotlib.pylab as plt
%pylab

figsize(12.5,6)
from lifelines.plotting import plot_lifetimes
from numpy.random import uniform, exponential
N = 25
current_time = 10
actual_lifetimes = np.array([[exponential(12), exponential(2)][uniform()<0.5] for i in range(N)])
observed_lifetimes = np.minimum(actual_lifetimes,current_time)
observed= actual_lifetimes < current_time
plt.xlim(0,25)
plt.vlines(10,0,30,lw=2, linestyles="--")
plt.xlabel('time')
plt.title('Births and deaths of our population, at $t=10$')
plot_lifetimes(observed_lifetimes, censorship=observed)
print "Observed lifetimes at time %d:\n"% (current_time), observed_lifetimes

?plot_lifetimes

import patsy







