# -*- coding: cp1252 -*-
'''
Created on 20 march. 2021

@author: mapas

coeficientes modificador capacidad frio:
Aquaris V4 06 (potenciaFrio: 5.07): [-4.07607623e-01,2.97475457e-02, -6.27691121e-06,7.41451065e-02,-1.13294825e-03, 1.86687100e-05]
Aquaris V4 08 (potenciaFrio: 6.12): [-4.39837552e-01  3.23285731e-02  3.37317509e-06  7.47625009e-02 -1.13931684e-03  3.31315300e-05]
Aquaris V4 10 (potenciaFrio: 7.56): [-3.71585830e-01  2.66914558e-02 -2.54700339e-06  7.29542853e-02 -1.11063870e-03  2.63437128e-05]
Aquaris V4 12 (potenciaFrio: 8.49): [-6.27648346e-01  3.20042226e-02  4.57272745e-06  8.59022237e-02 -1.30251276e-03  5.76207942e-05]
Aquaris V4 1414T (potenciaFrio: 11.46): [-3.24574449e-01  1.67714932e-02 -2.88626087e-06  7.40059240e-02 -1.12035652e-03  2.84141450e-05]
Aquaris V4 16T (potenciaFrio: 14.64): [-2.04640049e-01  5.75565820e-03  1.02198260e-06  7.10393592e-02 -1.07094067e-03  9.76073655e-06]

Aquaris V5 04 - Modificador potencia frio (potencia frío nominal = 4.23): [8.2970e-01, 5.0956e-02, -4.9775e-04, 4.0125e-03, -1.7505e-04, -3.3115e-04]
Aquaris V5 06 - Modificador potencia frio (potencia frío nominal = 5.02): [6.1054e-01, 4.4153e-02, -8.6986e-04, 1.6204e-02, -3.4197e-04, -1.0173e-04]
Aquaris V5 08 - Modificador potencia frio (potencia frío nominal = 6.08): [7.1790e-01, 4.1528e-02, -6.7426e-04, 1.2426e-02, -3.1700e-04, -5.7604e-05]
Aquaris V5 10 - Modificador potencia frio (potencia frío nominal = 7.53): [5.3656e-01, 4.0841e-02, -6.1216e-04, 2.0812e-02, -3.9303e-04, -1.2959e-04]
Aquaris V5 12 - Modificador potencia frio (potencia frío nominal = 8.60): [6.7858e-01, 3.1131e-02, -2.9257e-04, 1.4549e-02, -3.4441e-04, 1.2255e-04]
Aquaris V5 14 - Modificador potencia frio (potencia frío nominal = 11.48): [2.8183e-01, 5.5994e-02, -4.9370e-04, 3.0627e-02, -4.5721e-04, -6.5668e-04]
Aquaris V5 16 - Modificador potencia frio (potencia frío nominal = 13.80): [2.4664e-01, 4.8577e-02, -8.2737e-04, 3.0870e-02, -4.4884e-04, -4.1753e-04]
Aquaris V5 18 - Modificador potencia frio (potencia frío nominal = 15.04): [2.8105e-01, 4.5619e-02, -8.9813e-04, 3.1406e-02, -4.7540e-04, -3.4735e-04]
'''
from dataPoints.AquarisV5.AquarisV518PotenciaFrio import xdata, ydata,zdata,ratedPower
from scipy.optimize import curve_fit

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



def bicuadratica(xy,c1,c2,c3,c4,c5,c6):
    x,y = xy
    valorFuncion = c1 + c2 * x + c3 * x**2 + c4 * y + c5 *y**2 + c6 * x * y
    return valorFuncion
    
if __name__ == '__main__':
    popt, pcov = curve_fit(bicuadratica, (xdata,ydata), zdata)
    print u"Aquaris V5  - Modificador potencia frio (potencia frío nominal = {0:.2f}): [{1}]".format(ratedPower,", ".join([u"{:.4e}".format(x) for x in popt]))
    
    
    zdataCurvaBicuadratica = [bicuadratica(xy,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5]) for xy in zip(xdata,ydata)]
    zdataCurvaBicuadraticaOpenStudio = [bicuadratica(xy,0.258,0.0389,-0.000217,0.0469,-0.000943,-0.000343) for xy in zip(xdata,ydata)]
    AC_2010_PA_CAPFT = [bicuadratica(xy,1.0433825,0.0407073,0.0004506,-0.0041514,-0.0000886,-0.0003467) for xy in zip(xdata,ydata)]

    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Puntos de funcionamiento de partida
    ax.scatter(xdata, ydata, zdata, c='r', marker='^',label=u'Valores tabla')
    ax.scatter(xdata, ydata, zdataCurvaBicuadratica, c='b', marker='*',label=u'Valores bicuadratica')
    ax.scatter(xdata, ydata, zdataCurvaBicuadraticaOpenStudio, c='g', marker='o',label=u'Valores defecto OS')
    ax.scatter(xdata, ydata, AC_2010_PA_CAPFT, c='y', marker='o',label=u'AC_2010_PA_CAPFT')
    
    ax.set_xlabel(u'Tª agua salida')
    ax.set_ylabel(u'Tª aire entrada')
    ax.set_zlabel(u'Modificador potencia disponible')
    
    ax.legend()
    
    plt.show()

    
    
