#!/usr/bin/env python3

# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# from matplotlib.patches import Rectangle
# from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import string
from random import choice, choices

alphabet = [i for i in string.ascii_uppercase]
print(alphabet)

for ii in range(12):
    letters = [choices(alphabet, k=26) for _ in range(26)]
    letters = np.array(letters).reshape(26, 26)
    for i in range(26):
        print(' '.join(letters[i]))
    #
    print('')
#

"""
while True:
    letters = [choice(alphabet) for _ in range(26 * 26)]
    letters = np.array(letters).reshape(26, 26)
    for i in range(26):
        print(' '.join(letters[i]))
    #
    print('')
#
"""
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
