#!/usr/bin/env python3

"""
This demonstrates how using numerical derivative
in complex i direction avoids loss of precision
and quickly converges to actual numbers.
"""
import numpy as np
import matplotlib.pyplot as plt

func = np.exp
x0 = 3

xi = []
yi1 = []
yi2 = []
for n in np.arange(1, 60):
    h = 1.0 / 10**n
    xr = x0 + h
    xc = x0 + 1j * h
    fpp = (func(xr) - func(x0)) / h
    hc = 1j * h
    fpc = (func(xc) - func(x0)) / hc
    print(h, fpp, fpc.real)
    yi1.append(fpp.real)
    yi2.append(fpc.real)
    xi.append(n)
#

plt.plot(xi, yi1, '-', xi, yi2, '-')
plt.show()
