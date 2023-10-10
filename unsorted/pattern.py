#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# static plot #
maxt = 8 * 24 * np.pi
# aa, bb = 4.0, 3.88
aa, bb = 1.0, 0.999

tt = np.linspace(0, maxt, 10000)
xt = np.sin(aa * tt) / (1.0 + np.sin(bb * tt)**6)
yt = np.cos(bb * tt) / (1.0 + np.cos(aa * tt)**6)

plt.plot(xt, yt, '-', lw=0.5)
plt.show()


"""
# animation #
import matplotlib.animation as animation


fig = plt.figure(figsize=(8,8))
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1)) 
line, = ax.plot([], [], lw=2) 

# initialization function 
def init(): 
	# creating an empty plot/frame 
	line.set_data([], []) 
	return line, 

# lists to store x and y axis points 
xdata, ydata = [], [] 
numpoints = 10000
# animation function 
def animate(i):
	# tt is a parameter 
    tt = 24 * np.pi * i / numpoints
	# x, y values to be plotted 

    xt = np.sin(4 * tt) / (1.0 + np.sin(3.88 * tt)**6)
    yt = np.cos(3.88 * tt) / (1.0 + np.cos(4 * tt)**6)
    #
    # appending new points to x, y axes points list 
    xdata.append(xt) 
    ydata.append(yt) 
    line.set_data(xdata, ydata) 
    return line, 
#
# setting a title for the plot 
plt.title('Creating a growing coil with matplotlib!') 
# hiding the axis details 
plt.axis('off') 

# call the animator	 
anim = animation.FuncAnimation(fig, animate, init_func=init, 
							frames=numpoints, interval=20, blit=True) 

# save the animation as mp4 video file 
anim.save('pattern.gif',writer='pillow')
"""
