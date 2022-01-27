# -*- coding: cp1252 -*-
'''
Created on 20 march. 2021

@author: mapas

Modificador EIR
Aquaris V4 06 (ratedEER = 2.91): modificadora EIR [ 5.45699710e-01 -1.61527741e-02  7.05913874e-04  4.14655647e-03  4.73925065e-04 -7.98875423e-04]
Aquaris V4 08 (ratedEER = 2.90): modificadora EIR [ 8.24409790e-01 -3.31795312e-02  8.29027216e-04 -6.82940373e-03 5.75288585e-04 -3.88514164e-04]
Aquaris V4 10 (ratedEER = 3.11): modificadora EIR [ 8.02250512e-01 -3.10953865e-02  7.73132311e-04 -5.37016985e-03  5.65760794e-04 -5.09414334e-04]
Aquaris V4 12 (ratedEER = 3.10): modificadora EIR [ 9.47404056e-01 -3.72839407e-02  1.00032711e-03 -1.16366494e-02  6.58569497e-04 -5.35908777e-04]
Aquaris V4 1414T (ratedEER = 3.10): modificadora EIR [ 8.10345353e-01 -2.64255536e-02  5.78799251e-04 -6.18477125e-03 5.83505806e-04 -6.25342308e-04]
Aquaris V4 16T (ratedEER = 3.24): modificadora EIR [ 4.36010800e-01 -4.03713342e-03  2.03114893e-04  7.31390122e-03  4.41891377e-04 -9.26450315e-04]


Aquaris V5 04 - Modificador EIR (ratedEER = 3.28): [4.3299e-01, -1.3873e-02, 1.6988e-04, 1.0856e-02, 3.5882e-04, -6.8184e-04]
Aquaris V5 06 - Modificador EIR (ratedEER = 3.14): [3.4821e-01, -1.1562e-02, 8.0798e-05, 1.5249e-02, 2.9666e-04, -6.9169e-04]
Aquaris V5 08 - Modificador EIR (ratedEER = 3.05): [3.6737e-01, -1.3724e-02, 1.5862e-04, 1.5400e-02, 2.6593e-04, -5.7229e-04]
Aquaris V5 10 - Modificador EIR (ratedEER = 3.15): [3.7277e-01, -1.8234e-02, 3.8813e-04, 1.5027e-02, 2.7917e-04, -5.2046e-04]
Aquaris V5 12 - Modificador EIR (ratedEER = 3.05): [5.0967e-01, -2.1605e-02, 3.8997e-04, 7.1009e-03, 3.7411e-04, -3.7859e-04]
Aquaris V5 14 - Modificador EIR (ratedEER = 3.25): [2.5441e-01, -8.0386e-04, -2.5637e-04, 1.8383e-02, 2.6711e-04, -8.7665e-04]
Aquaris V5 16 - Modificador EIR (ratedEER = 3.15): [2.1191e-01, -2.6128e-03, -1.4019e-04, 2.0655e-02, 2.3712e-04, -8.4671e-04]
Aquaris V5 18 - Modificador EIR (ratedEER = 3.08): [2.4375e-01, -3.9267e-03, -1.5170e-04, 1.8779e-02, 2.4007e-04, -7.1631e-04]
'''
from dataPoints.AquarisV5.AquarisV518EER import xdata, ydata,zdata,ratedEER
from scipy.optimize import curve_fit

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



def bicuadratica(xy,c1,c2,c3,c4,c5,c6):
    x,y = xy
    valorFuncion = c1 + c2 * x + c3 * x**2 + c4 * y + c5 *y**2 + c6 * x * y
    return valorFuncion
    
if __name__ == '__main__':
    popt, pcov = curve_fit(bicuadratica, (xdata,ydata), zdata)

    print u"Aquaris V5  - Modificador EIR (ratedEER = {0:.2f}): [{1}]".format(ratedEER,", ".join([u"{:.4e}".format(x) for x in popt]))
    
    
    zdataCurvaBicuadratica = [bicuadratica(xy,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5]) for xy in zip(xdata,ydata)]
    AC_2010_PA_EIRFT = [bicuadratica(xy,0.5961907,-0.0099493,0.0007888, 0.0004506,0.0004875,-0.0007623) for xy in zip(xdata,ydata)]
    openStudioDefecto = [bicuadratica(xy,0.934,-0.0582,0.0045,0.00243,0.000486,-0.00122) for xy in zip(xdata,ydata)]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Puntos de funcionamiento de partida
    ax.scatter(xdata, ydata, zdata, c='r', marker='^',label=u'Valores tabla')
    ax.scatter(xdata, ydata, zdataCurvaBicuadratica, c='b', marker='*',label=u'Valores bicuadratica')
    ax.scatter(xdata, ydata, AC_2010_PA_EIRFT, c='g', marker='o',label=u'Valores AC_2010_PA_EIRFT')
    ax.scatter(xdata, ydata, openStudioDefecto, c='y', marker='o',label=u'Valores OpenStudio')
    
    ax.set_xlabel(u'Tª agua salida')
    ax.set_ylabel(u'Tª aire entrada')
    ax.set_zlabel(u'Modificador EIR')
    
    ax.legend()
    
    plt.show()

    
    
