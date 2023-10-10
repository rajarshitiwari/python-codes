#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

a, b = 1.0, 10.0
n = 7

tt = np.linspace(0, 2.0 * np.pi, 10000)
nmax = 36
for n in range(1, nmax):
    ii = (n / nmax)**2
    # rr = 1 + np.tanh(b * np.sin(n * tt) * np.cos(tt)) / b
    rr = (1 + np.tanh(b * np.sin(n * tt) * np.cos(n * tt)) / b) * ii
    #
    x = rr * np.cos(tt)
    y = rr * np.sin(tt)
    #
    plt.plot(x, y, '-',c=cm.afmhot_r(ii))
    # plt.plot(tt, rr, '-')
plt.show()
