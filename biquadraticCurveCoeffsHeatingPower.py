# -*- coding: cp1252 -*-
'''
Created on 20 march. 2021


@author: mapas

Modificador capacidad calor
Aquaris V4 06 (ratedCapacity = 6.57): [1.1955e+00, 1.2677e-02, -2.8499e-04, -8.4949e-03, 2.5734e-05, -1.1520e-04]
Aquaris V4 08 (ratedCapacity = 8.01): [7.8308e-01, 1.8549e-02, -2.0658e-05, 9.7241e-03, -1.9660e-04, -5.8276e-05]
Aquaris V4 10 (ratedCapacity = 10.00): [1.0007e+00, 1.7497e-02, 5.2028e-05, -4.7052e-03, -7.1094e-06, 2.8627e-05]
Aquaris V4 12 (ratedCapacity = 12.10): [1.0057e+00, 2.7293e-02, 4.5632e-05, -4.4844e-03, -2.5941e-05, -2.0546e-04]
Aquaris V4 1414T (ratedCapacity = 13.76): [9.0863e-01, 1.4281e-02, -8.5699e-05, 3.7476e-03, -1.0204e-04, -6.0752e-05]
Aquaris V4 16T (ratedCapacity = 15.21): [8.5258e-01, 1.3348e-02, -7.9909e-05, 4.3548e-03, -9.0637e-05, 4.8655e-05]

Aquaris V4 Pro 125 (ratedCapacity = 24.72): [9.1738e-01, 1.6016e-02, -6.4439e-05, 4.1711e-03, -1.7185e-04, -5.0322e-05]


Aquaris V5 04 (ratedCapacity = 4.55): [1.0911e+00, -7.9699e-03, 1.0146e-03, -2.2190e-03, 1.7443e-05, -4.0954e-05]
Aquaris V5 06 (ratedCapacity = 6.08): [1.0393e+00, 5.5585e-03, 4.1105e-04, -3.0220e-03, 2.7412e-05, -5.0681e-05]
Aquaris V5 08 (ratedCapacity = 7.81): [9.1600e-01, 1.0694e-02, 6.2640e-04, -2.0228e-03, 1.3820e-05, -6.5286e-05]
Aquaris V5 10 (ratedCapacity = 10.10): [8.9301e-01, 1.3966e-02, 3.2689e-04, 6.2318e-04, -2.1216e-05, -8.0304e-05]
Aquaris V5 12 (ratedCapacity = 11.80): [8.7247e-01, 1.6758e-02, 2.9524e-04, -4.3783e-04, -7.8020e-06, -8.2793e-05]
Aquaris V5 14 (ratedCapacity = 14.10): [8.4621e-01, 1.6753e-02, 2.1129e-04, 1.6046e-03, -3.4729e-05, -7.8124e-05]
Aquaris V5 16 (ratedCapacity = 16.30): [8.6205e-01, 1.6112e-02, -1.6696e-05, 8.6721e-05, -1.5483e-05, -5.8586e-05]
Aquaris V5 18 (ratedCapacity = 17.90): [8.4750e-01, 1.9040e-02, 1.5530e-04, -5.5333e-04, -9.5327e-06, -6.0546e-05]



Alezio.AWHP 4 (ratedCapacity = 4.10): [1.0226e+00, 9.2934e-03, 2.7465e-04, -1.4558e-03, -4.6515e-06, 1.4037e-04]
Alezio.AWHP 6 (ratedCapacity = 6.00): [8.9412e-01, 1.7458e-02, 2.0023e-04, -7.5533e-04, -7.1979e-06, 1.0734e-04]
Alezio.AWHP 8 (ratedCapacity = 8.00): [8.7545e-01, 9.9913e-03, 2.9329e-04, 3.7368e-03, -5.4568e-05, 4.3752e-05]
Alezio.AWHP 11 (ratedCapacity = 11.20): [8.5691e-01, 1.6904e-02, 2.5800e-04, 1.4046e-03, -1.9202e-05, 7.4072e-06]
Alezio.AWHP 16 (ratedCapacity = 16.00): [6.5258e-01, 2.2230e-02, 2.5015e-04, 9.8914e-03, -1.3634e-04, -5.8023e-05]


HPIEvolution.HPI6 (ratedCapacity = 6.00): [8.9412e-01, 1.7458e-02, 2.0023e-04, -7.5533e-04, -7.1979e-06, 1.0734e-04]
HPIEvolution.HPI8 (ratedCapacity = 8.00): [8.7545e-01, 9.9913e-03, 2.9329e-04, 3.7368e-03, -5.4568e-05, 4.3752e-05]
HPIEvolution.HPI11 (ratedCapacity = 11.20): [8.5691e-01, 1.6904e-02, 2.5800e-04, 1.4046e-03, -1.9202e-05, 7.4072e-06]
HPIEvolution.HPI16 (ratedCapacity = 16.00): [6.5258e-01, 2.2230e-02, 2.5015e-04, 9.8914e-03, -1.3634e-04, -5.8023e-05]
HPIEvolution.HPI22 (ratedCapacity = 16.37): [8.1307e-01, 2.5191e-02, 1.0447e-04, 5.4246e-03, -1.4341e-04, -4.5795e-05]
HPIEvolution.HPI27 (ratedCapacity = 19.73): [7.7200e-01, 2.5576e-02, 6.9511e-05, 5.1429e-03, -1.3572e-04, -4.3413e-05]


AlezioCompact.MR4.5  (ratedCapacity = 4.50): [2.4249e+00, 7.3663e-02, 7.5984e-04, 3.4070e-02, -4.9045e-04, -1.0529e-04]
AlezioCompact.MR6  (ratedCapacity = 5.50): [1.2797e+00, 8.7639e-04, 3.1435e-04, -1.2145e-02, 7.9314e-05, 4.0160e-04]
AlezioCompact.MR8  (ratedCapacity = 8.00): [1.1074e+00, 2.9324e-03, -1.2493e-04, -1.6739e-03, -3.2725e-05, 2.9873e-04]
AlezioCompact.MR11  (ratedCapacity = 11.20): [9.7560e-01, 1.1501e-02, 1.4034e-04, -5.0385e-04, -1.2956e-05, 9.8841e-05]
AlezioCompact.MR16  (ratedCapacity = 16.00): [6.8199e-01, 2.0718e-02, 2.1371e-04, 9.5821e-03, -1.3794e-04, -2.9614e-05]


MiniChiller.KMCI5  (ratedCapacity = 6.39): [-4.9409e-01, 5.1539e-02, 8.1949e-05, 7.3529e-02, -1.0311e-03, -6.1336e-04]
MiniChiller.KMCI7  (ratedCapacity = 8.24): [-5.6317e-01, 5.7823e-02, 9.1779e-05, 8.3224e-02, -1.1665e-03, -6.8497e-04]
MiniChiller.KMC10  (ratedCapacity = 11.33): [7.9375e-01, 2.2331e-02, 5.4165e-04, -3.3792e-03, 1.3348e-05, -2.9615e-05]
MiniChiller.KMCI12  (ratedCapacity = 12.00): [-5.7706e-01, 6.1147e-02, 9.6848e-05, 8.7080e-02, -1.2228e-03, -7.2542e-04]
MiniChiller.KMCI14  (ratedCapacity = 14.75): [9.5366e-01, 2.3710e-02, 5.6012e-04, -1.2520e-02, 1.2361e-04, -1.1176e-04]
MiniChiller.KMCI16  (ratedCapacity = 17.00): [8.1944e-01, 2.3385e-02, 5.7596e-04, -6.6612e-03, 5.1747e-05, -1.0581e-04]

AquarisV4Pro.Pro125  (ratedCapacity = 24.72): [9.1750e-01, 1.6011e-02, -6.4349e-05, 4.1652e-03, -1.7178e-04, -5.0220e-05]
AquarisV4Pro.Pro135  (ratedCapacity = 32.65): [9.5806e-01, 1.2440e-02, -3.3401e-04, -1.9112e-03, 3.6732e-06, 5.3108e-05]
AquarisV4Pro.Pro250  (ratedCapacity = 48.70): [1.1528e+00, 2.7676e-02, -1.3007e-04, -7.2496e-03, -4.6793e-05, -3.8725e-04]
AquarisV4Pro.Pro250F  (ratedCapacity = 48.25): [1.3268e+00, 2.0838e-02, -2.9334e-04, -1.8789e-02, 1.5494e-04, -1.8180e-04]
AquarisV4Pro.Pro  (ratedCapacity = 52.00): [9.6613e-01, 1.3682e-02, -3.2947e-04, -3.1884e-03, 1.0956e-05, -8.9589e-06]
AquarisV4Pro.Pro270  (ratedCapacity = 65.10): [1.2432e+00, 5.9298e-03, -2.8084e-04, -1.4214e-02, 1.0889e-04, 1.8112e-04]
AquarisV4Pro.Pro235LT  (ratedCapacity = 32.50): [9.1364e-01, -1.5807e-04, -2.2333e-04, 8.3495e-03, -1.5106e-04, 1.7080e-05]


AquarisV4ProMax.ProMAX466  (ratedCapacity = 68.46): [1.3344e+00, 1.6716e-02, 2.2561e-04, -1.9362e-02, 1.8672e-04, -9.5654e-05]
AquarisV4ProMax.ProMAX475  (ratedCapacity = 74.70): [1.1774e+00, 2.2743e-02, 2.1679e-04, -1.2455e-02, 1.0599e-04, -1.8105e-04]
AquarisV4ProMax.ProMAX485  (ratedCapacity = 85.60): [1.0275e+00, 1.9847e-02, 1.8918e-04, -1.0869e-02, 9.2490e-05, -1.5800e-04]
AquarisV4ProMax.ProMAX695  (ratedCapacity = 93.34): [1.2603e+00, 2.4083e-02, 1.4823e-04, -1.8022e-02, 1.8636e-04, -2.0602e-04]
AquarisV4ProMax.ProMAX6105  (ratedCapacity = 102.47): [1.2062e+00, 2.7186e-02, 4.9625e-04, -1.5992e-02, 1.5804e-04, -2.5280e-04]
AquarisV4ProMax.ProMAX6115  (ratedCapacity = 111.47): [1.4827e+00, 2.5759e-02, 5.0665e-04, -2.8849e-02, 3.0726e-04, -2.1591e-04]

KCA.KCA  (ratedCapacity = 1.00): [1.0911e+00, 9.8873e-02, -1.6225e-03, -2.5245e-02, 1.0428e-04, 5.9466e-05]

'''
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange
from scipy.optimize import curve_fit

from dataPoints.AquarisV5.AquarisV4Pro125Potencia import xdata, ydata, zdata, ratedPower, ratedPower45, \
     zdata45
    

import matplotlib.pyplot as plt


def bicuadratica(xy,c1,c2,c3,c4,c5,c6):
    x,y = xy
    valorFuncion = c1 + c2 * x + c3 * x**2 + c4 * y + c5 *y**2 + c6 * x * y
    return valorFuncion
    
if __name__ == '__main__':
    popt, pcov = curve_fit(bicuadratica, (xdata,ydata), zdata)
    print u"KCA.KCA  (ratedCapacity = {0:.2f}): [{1}]".format(ratedPower,", ".join([u"{:.4e}".format(x) for x in popt]))
    
    zdataCurvaBicuadratica = [bicuadratica(xy,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5]) for xy in zip(xdata,ydata)]
    zdataCurvaBicuadraticaOpenStudio = [bicuadratica(xy,0.369827,0.043341,-0.00023,0.000466,2.6e-005,-0.00027) for xy in zip(xdata,ydata)]    
    
    
    
    
    
#     print u"HULC"
#     print u""" Hay un problema en la forma de definición de las curvas en HULC y es que el consumo está afectado por las tres curvas:
#     - La de las temperaturas disponibles (con_T)
#     - La del (con_FCP)
#     - Pero también la de Cap_T, porque si la capacidad disminuye, aumenta el fcp y por lo tanto aumenta el consumo, a través del factor de proporcionalidad de con_FPC
#      
#     """
#     
#     
#     popt, pcov = curve_fit(bicuadratica, (xdata,ydata), zdata45)
#     
#     print u"Coeficientes Modificador capacidad (ratedCapacity = {0:.2f}): {1}".format(ratedPower45,"; ".join([u"{:.4e}".format(x) for x in [popt[0], popt[3],popt[4],popt[1],popt[2],popt[5]]]))    
#     print u"Exponentes: 0;0; 1;0; 2;0; 0;1; 0;2; 1;1" 
#     print u"Limites var 1: de {0} a {1}".format(min(ydata),max(ydata))  # reordenamos, primero impulsión y luego exterior
#     print u"Limites var 2: de {0} a {1}".format(min(xdata),max(xdata))  
    
    

    
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Puntos de funcionamiento de partida
    ax.scatter(xdata, ydata, zdata, c='r', marker='^',label=u'Valores tabla')
    ax.scatter(xdata, ydata, zdataCurvaBicuadratica, c='b', marker='*',label=u'Valores bicuadratica')
    ax.scatter(xdata, ydata, zdataCurvaBicuadraticaOpenStudio, c='g', marker='o',label=u'Valores defecto')
    
    ax.set_xlabel(u'Tª aire')
    ax.set_ylabel(u'Tª agua')
    ax.set_zlabel(u'Modificador potencia disponible')
    
    ax.legend()
    
    plt.show()

#     # Modificador capcadidad en función de la  temperatura húmeda exterior
#     xHulc = arange(-15,30,0.1)
#     modCapacidad = [0.8232 + 0.0281 * x  + 0.0002 * x**2 for x in xHulc]
#     modConsumo = [0.9496 + 0.009 * x - 0.0001 * x**2 for x in xHulc]
#     
#     modConsumoEfectiva = [x/y for x,y in zip(modConsumo,modCapacidad)]
#     fig = plt.figure()
#     ax = ax = fig.add_subplot(111)
#     ax.plot(xHulc,modCapacidad)
#     ax.plot(xHulc,modConsumo)
#     ax.plot(xHulc,modConsumoEfectiva)
#     ax.legend([u'capacidad',u'consumo',u'efectiva'])
#     plt.show()
#     
#     xHulc = arange (0,1,0.005)
#     modConsumo = [0.0856522 + 0.938814 * x -0.183436 * x**2 + 0.15897 * x**3 for x in xHulc]
#     fig = plt.figure()
#     ax = ax = fig.add_subplot(111)
#     ax.plot(xHulc,modConsumo)
#     
#     
#     plt.show()    
    
    
