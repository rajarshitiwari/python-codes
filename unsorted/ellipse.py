#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def hexcolor(r, g, b):
    r,g,b = int(255 * r), int(255 * g), int(255 * b)
    # value = (r << 16) + (g << 8) + b
    value = '#{:02x}{:02x}{:02x}'.format(r,g,b)
    return value
#
t = np.linspace(0, 2 * np.pi, 1000)

major = 5.0

for minor in np.linspace(0.0, major, 21):
    x = major * np.cos(t)
    y = minor * np.sin(t)
    c = minor / major
    print(major, minor)
    c = hexcolor(c, 0.5 * c, 0.5 * c)
    plt.plot(x, y, c=c)
    plt.plot(y, x, c=c)
#
plt.show()
#print(t)
