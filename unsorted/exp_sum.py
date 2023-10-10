#!/usr/bin/env python3
"""
from EU import members

members_prime = members.copy()
del members_prime[-1]           # that's UK
members = members_prime
"""

import numpy as np
import matplotlib.pyplot as plt

def exp_sum(m, d, y, N):
    x = np.asarray ([np.exp( 2.0 * np.pi * 1j * (n/m + n**2/d + n**3/y)) for n in np.arange(N)])
    x = x.cumsum()
    return x
#

# x = exp_sum(3, 28, 19, 10000)
x = exp_sum(4, 30, 1985, 120000)
print(x)

plt.tick_params(
    axis='both',             # changes apply to the x-axis
    which='both',            # both major and minor ticks are affected
    bottom=False,            # ticks along the bottom edge are off
    top=False,               # ticks along the top edge are off
    labelbottom=False,       # labels along the bottom edge are off
    left=False,
    right=False)
plt.axis('off')
#plt.plot(np.real(x), np.imag(x), '.', color='r')
plt.scatter(np.real(x), np.imag(x), s=0.1, c=np.abs(x))
plt.show()
