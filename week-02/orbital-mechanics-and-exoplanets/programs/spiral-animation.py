# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:01:14 2021

@author: Varun Kumar S
"""

import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 

#Initializing the figure for the plot
fig,ax = plt.subplots(nrows=1, ncols=1,figsize = (5,5)) 
#To fix the frame from not moving we can specify the limits
ax.set_ylim(-50, 50) 
ax.set_xlim(-50, 50)

#Initializing the curve and point
ln, = plt.plot([], [], 'b-')
pt, = plt.plot([], [], 'ro')

#Initializing Variables
xdata,ydata = [],[]

def animate(i,line,point): 
    # t is a parameter which varies with the frame number
    t = 0.1 * i 
       
    # x, y values to be plotted 
    x = t * np.sin(t) 
    y = t * np.cos(t) 
       
    # appending values to the previously empty x and y data holders 
    xdata.append(x) 
    ydata.append(y) 
    line.set_data(xdata, ydata)
    point.set_data(x,y)
    return line,point

anim = animation.FuncAnimation(fig, animate, frames = 500, blit = True, fargs = (ln,pt))
anim.save('Spiral.gif', writer = 'pillow',fps =30)

