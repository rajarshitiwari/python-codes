#!/usr/bin/env python3

import numpy as np

def dsc(tup):
    """Compute distance on simple cubic lattice.
    IN: tup is 3 length array, list of tuple.
    """
    x, y, z = tup
    return (x*x + y*y + z*z)
#

def dbcc(tup):
    """Compute distance on body-centered cubic lattice.
    IN: tup is 3 length array, list of tuple.
    """
    x, y, z = tup
    return 3 * (x*x + y*y + z*z) - 2 * (x*y + y*z + z*x)
#

def dfcc(tup):
    """Compute distance on face-centered cubic lattice.
    IN: tup is 3 length array, list of tuple.
    """
    x, y, z = tup
    return 2 * (x*x + y*y + z*z) + 2 * (x*y + y*z + z*x)
#

def get_xsc(x, y, z):
    return np.array([x, y, z])

def get_xbcc(x, y, z):
    return np.array([-x+y+z, x-y+z, x+y-z])

def get_xfcc(x, y, z):
    return np.array([y+z, x+z, x+y])

func = dbcc
getvec = get_xbcc
Ndmax = 8


def get_nn_from_nd(Nd, func):
    N = Nd
    nn = []
    for i in range(-N, N+1):
        for j in range(-N, N+1):
            for k in range(-N, N+1):
                tup = (i, j, k)
                num = func(tup)
                if num == Nd:
                    nn.append(tup)
                #
    #
    return nn
#
dic_nn = {i: None for i in range(1, Ndmax)}

def get_neighbours():
    
    for Nd in range(1, Ndmax):
        # print(f"For distance squared = {Nd}")
        dic_nn[Nd] = get_nn_from_nd(Nd, func)
        #
    
    dic = {}
    ii = 1
    for k, v in dic_nn.items():
        if len(v) > 0:
            a = np.array(v)
            l = a.shape[0]
            dic[ii] = {'half': a[:l//2], 'full':a}
            ii += 1
        # print(k, len(v))
    return dic
#
dd = get_neighbours()