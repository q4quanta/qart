import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
def phase(phi,value):
    xval = np.arange(0, 2*np.pi, 0.01)
    yval = np.ones_like(xval)
    xo =  phi;yo = 1.0
    colormap = plt.get_cmap('hsv')
    norm = mpl.colors.Normalize(0.0, 2*np.pi)
    ax = plt.subplot(1, 1, 1, polar=True)
    ax.scatter(0,0, s = value*12000, color = 'blue', norm=norm, linewidths=0)
    ax.scatter(xval, yval, c=xval, s=100, cmap=colormap, norm=norm, linewidths=0)
    ax.scatter(xo,yo, s=100, color = 'black', norm=norm, linewidths=0)
    ax.set_yticks([])
    return 
phase(np.pi/2,1.0)
