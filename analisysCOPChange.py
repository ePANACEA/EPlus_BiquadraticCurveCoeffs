# -*- coding: cp1252 -*-
'''
Created on 20 march. 2021

@author: mapas
'''
from AquarisV406COP import xdata, ydata
from AquarisV406COP import zdata as zdata06
from AquarisV408COP import zdata as zdata08
from AquarisV410COP import zdata as zdata10
from AquarisV412COP import zdata as zdata12
from AquarisV41414TCOP import zdata as zdata1414T
from AquarisV416TCOP import zdata as zdata16T
from scipy.optimize import curve_fit

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



    
if __name__ == '__main__':    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Puntos de funcionamiento de partida
    ax.scatter(xdata, ydata, zdata06,  marker='^',label=u'AquarisV406COP')
    ax.scatter(xdata, ydata, zdata08,  marker='^',label=u'AquarisV408COP')
    ax.scatter(xdata, ydata, zdata10,  marker='^',label=u'AquarisV410COP')
    ax.scatter(xdata, ydata, zdata12,  marker='*',label=u'AquarisV412COP')
    ax.scatter(xdata, ydata, zdata1414T,  marker='^',label=u'AquarisV41414TCOP')
    ax.scatter(xdata, ydata, zdata16T, marker='^',label=u'AquarisV416TCOP')
    
    ax.set_xlabel(u'Tª aire')
    ax.set_ylabel(u'Tª agua')
    ax.set_zlabel(u'Modificador COP')
    
    ax.legend()
    
    plt.show()
    

