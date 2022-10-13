#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


lsize = 100
nsize = lsize * lsize
fill = 0.5
ifill = int(fill * nsize)

print(f"lattice nsize = {nsize}, filled = {ifill}")
x = np.hstack([np.ones(ifill, dtype=int),np.zeros(nsize-ifill,dtype=int)])
y = x.reshape((lsize, lsize))
plt.imshow(y);plt.show()


for i in range(12):
    np.random.shuffle(x)
    y = x.reshape((lsize, lsize))
    plt.imshow(y);plt.show()
#

"""
one, zero = np.ones(ifill, dtype=int),np.zeros(nsize-ifill,dtype=int)

x = np.zeros(nsize, dtype=int)
flag_0, flag_1 = True, True

i0 = 0
i1 = 0
while flag_1 or flag_0:
    if np.random.random() < 0.5:
        x[i0] = 1; i0 += 1
    else:
        x[i1

"""
