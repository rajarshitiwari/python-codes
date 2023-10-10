#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import time

nk = 6

K1 = np.array([
    [0.00,  0.00,  0.00],
    [0.50, -0.50,  0.50],
    [0.00,  0.00,  0.50],
    [0.00,  0.00,  0.00],
    [0.25,  0.25,  0.25],
    [0.25,  0.25,  0.25]])

K2 = np.array([
    [0.50, -0.50,  0.50],
    [0.00,  0.00,  0.50],
    [0.00,  0.00,  0.00],
    [0.25,  0.25,  0.25],
    [0.50, -0.50,  0.50],
    [0.00,  0.00,  0.50]])

n_per_line = 100
npoints = nk * n_per_line

num_nn = 4
nn = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]])

lsize = 24
coeff = 2.0 * np.pi / lsize

nsize = lsize * lsize * lsize


def eps_k(k):
    """
    Compute TB eigenvalue \epsilon_{k}
    Parameters
    ----------
    k : array of length 3
        bloch vector k
    Returns
    -------
    ek : Float
        Energy
    """
    ek = -2.0 * np.sum(np.cos(np.matmul(nn, k)))
    #ek = -2.0 * np.sum(np.cos(np.matmul(nn, k)))
    return ek
#

def tb_spectrum_3d(lsize, nn, Jey, qvec=np.zeros(3), mz=0.0):
    """
    USAGE: ek = tb_spectrum_3d(lsize, nn)
    Parameters
    ----------
    lsize : Int
        size of the lattice.
    nn : array of shape(:, 3)
        array of neighbours.
    Returns
    -------
    Spectrum ek
    """
    # there is a bug here in k, kq part regarding scale of the q vectors
    mp = np.sqrt(1.0 - mz**2)
    k_iter = (eps_k(np.array(k)) for k in np.ndindex((lsize, lsize, lsize)))
    kq_iter = (eps_k(np.array(k) + qvec) for k in np.ndindex((lsize, lsize, lsize)))
    ek = np.fromiter(k_iter, float)
    ekq = np.fromiter(kq_iter, float)
    tmp = (ekq - ek + 2 * mz * Jey)
    tmp = tmp * tmp + 4 * (mp * Jey)**2
    tmp = np.sqrt(tmp)
    ek_plus = 0.5 * (ek + ekq + tmp)
    ek_minus = 0.5 * (ek + ekq - tmp)
    ek = np.concatenate([ek_minus, ek_plus])
    ek.sort()
    return ek
#

def eps_k1(k):
    """
    Compute TB eigenvalue \epsilon_{k}
    Parameters
    ----------
    k : array of length 3
        bloch vector k
    Returns
    -------
    ek : Float
        Energy
    """
    m = 1.0 * nn.T
    ek = -2.0 * np.sum(np.cos(np.einsum('ij,jk', k, m)), axis=1)
    #ek = -2.0 * np.sum(np.cos(np.matmul(nn, k)))
    return ek
#

def tb_spectrum_3d_new(lsize, nn, Jey, qvec=np.zeros(3), mz=0.0):
    """
    USAGE: ek = tb_spectrum_3d(lsize, nn)
    Parameters
    ----------
    lsize : Int
        size of the lattice.
    nn : array of shape(:, 3)
        array of neighbours.
    Returns
    -------
    Spectrum ek
    """
    # there is a bug here in k, kq part regarding scale of the q vectors
    mp = np.sqrt(1.0 - mz**2)
    k_iter = coeff * np.stack([k for k in np.ndindex((lsize, lsize, lsize))])
    kq_iter = k_iter + qvec
    ek = eps_k1(k_iter)
    ekq = eps_k1(kq_iter)
    tmp = (ekq - ek + 2 * mz * Jey)
    tmp = tmp * tmp + 4 * (mp * Jey)**2
    tmp = np.sqrt(tmp)
    ek_plus = 0.5 * (ek + ekq + tmp)
    ek_minus = 0.5 * (ek + ekq - tmp)
    ek = np.concatenate([ek_minus, ek_plus])
    ek.sort()
    return ek
#





qvec = coeff * np.array([12, 12, 12]) # period vector
mz = 0.0                           # z-component of spin

Jey = 6.0

tic = time.time()
ek1 = tb_spectrum_3d(lsize, nn, Jey, qvec, mz)
print("time = ", time.time() - tic)

tic = time.time()
ek2 = tb_spectrum_3d_new(lsize, nn, Jey, qvec, mz)
print("time = ", time.time() - tic)

ek = ek2
np.savetxt("eig_py.dat", ek, fmt="%.15f")

