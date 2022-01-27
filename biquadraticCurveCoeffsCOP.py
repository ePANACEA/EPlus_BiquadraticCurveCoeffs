# -*- coding: cp1252 -*-
'''
Created on 20 march. 2021

@author: mapas

Modificador cop
Aquaris V4 06 (ratedCOP = 4.47): [2.0948e+00, 5.3278e-02, 3.9306e-04, -5.6812e-02, 4.7477e-04, -8.1965e-04]
Aquaris V4 08 (ratedCOP = 4.33): [1.7087e+00, 5.7349e-02, 5.5232e-04, -3.6548e-02, 2.1548e-04, -9.3577e-04]
Aquaris V4 10 (ratedCOP = 4.42): [1.3571e+00, 5.0362e-02, 5.8378e-04, -1.7466e-02, -3.4573e-05, -7.1755e-04]
Aquaris V4 12 (ratedCOP = 4.19): [2.9576e+00, 2.8797e-02, -2.1561e-04, -9.9454e-02, 1.0429e-03, -3.2065e-04]
Aquaris V4 1414T (ratedCOP = 4.30): [2.3192e+00, 6.7502e-02, 5.7608e-04, -6.9514e-02, 6.6916e-04, -1.2253e-03]
Aquaris V4 16T (ratedCOP = 4.41): [2.0163e+00, 5.4961e-02, 6.8952e-04, -5.4991e-02, 4.9127e-04, -8.4217e-04]

AquarisV5 04 (ratedCOP = 4.78): [1.8915e+00, 6.8504e-02, 8.2205e-04, -4.3696e-02, 3.3108e-04, -1.0599e-03]
AquarisV5 06 (ratedCOP = 4.51): [1.8849e+00, 5.8364e-02, 6.7454e-04, -4.2580e-02, 3.1940e-04, -9.0265e-04]
AquarisV5 08 (ratedCOP = 4.38): [1.8521e+00, 5.7251e-02, 6.6909e-04, -4.0461e-02, 2.9753e-04, -8.7201e-04]
AquarisV5 10 (ratedCOP = 4.43): [1.8799e+00, 5.7436e-02, 5.8857e-04, -4.1755e-02, 3.0797e-04, -8.9666e-04]
AquarisV5 12 (ratedCOP = 4.32): [1.8637e+00, 5.7920e-02, 6.8368e-04, -4.1096e-02, 3.0442e-04, -8.8940e-04]
AquarisV5 14 (ratedCOP = 4.85): [1.8563e+00, 6.4050e-02, 7.8943e-04, -4.2475e-02, 3.2253e-04, -9.6099e-04]
AquarisV5 16/16T (ratedCOP = 4.67): [1.7656e+00, 6.3511e-02, 8.7850e-04, -3.8251e-02, 2.7582e-04, -9.4741e-04]
AquarisV5 18/18T (ratedCOP = 4.40): [1.7528e+00, 5.6324e-02, 7.3019e-04, -3.6639e-02, 2.5920e-04, -8.2216e-04]



Alezio.AWHP 4 Modificador COP (ratedCOP = 4.80): [1.5591e+00, 5.7082e-02, 3.1430e-04, -2.7901e-02, 1.2129e-04, -8.3222e-04]
Alezio.AWHP 6 Modificador COP (ratedCOP = 4.42): [1.5699e+00, 5.2804e-02, 2.2800e-04, -2.7865e-02, 1.2287e-04, -7.5344e-04]
Alezio.AWHP 8 Modificador COP (ratedCOP = 4.40): [1.4454e+00, 4.7159e-02, 1.1448e-04, -2.0018e-02, 4.2882e-05, -6.2860e-04]
Alezio.AWHP 11 Modificador COP (ratedCOP = 4.45): [1.2181e+00, 3.7065e-02, 2.0112e-04, -1.1107e-02, -4.7408e-05, -4.1104e-04]
Alezio.AWHP Modificador COP (ratedCOP = 4.10): [1.2902e+00, 3.4799e-02, 1.3780e-04, -1.2654e-02, -3.6833e-05, -3.7986e-04]


HPIEvolution.HPI6 Modificador COP (ratedCOP = 4.42): [1.5699e+00, 5.2804e-02, 2.2800e-04, -2.7865e-02, 1.2287e-04, -7.5344e-04]
HPIEvolution.HPI8 Modificador COP (ratedCOP = 4.40): [1.4454e+00, 4.7159e-02, 1.1448e-04, -2.0018e-02, 4.2882e-05, -6.2860e-04]
HPIEvolution.HPI Modificador COP (ratedCOP = 4.45): [1.2181e+00, 3.7065e-02, 2.0112e-04, -1.1107e-02, -4.7408e-05, -4.1104e-04]
HPIEvolution.HPI Modificador COP (ratedCOP = 4.10): [1.2902e+00, 3.4799e-02, 1.3780e-04, -1.2654e-02, -3.6833e-05, -3.7986e-04]
HPIEvolution.HPI Modificador COP (ratedCOP = 4.01): [1.5980e+00, 4.2003e-02, 1.7692e-04, -2.8532e-02, 1.4830e-04, -4.8494e-04]
HPIEvolution.HPI Modificador COP (ratedCOP = 3.65): [1.6367e+00, 3.8418e-02, 4.1948e-05, -2.9327e-02, 1.5504e-04, -4.2472e-04]


AlezioCompact.MR4.5 Modificador COP (ratedCOP = 5.06): [1.4445e+00, 5.5591e-02, 2.5757e-04, -2.2692e-02, 5.7211e-05, -7.7823e-04]
AlezioCompact.MR6 Modificador COP (ratedCOP = 4.42): [1.4116e+00, 5.8724e-02, 3.6775e-04, -1.9899e-02, 2.9458e-05, -8.8614e-04]
AlezioCompact.MR8 Modificador COP (ratedCOP = 4.40): [1.3839e+00, 4.6237e-02, 2.2401e-04, -1.7719e-02, 1.7987e-05, -6.2985e-04]
AlezioCompact.MR11 Modificador COP (ratedCOP = 4.45): [1.1097e+00, 3.8057e-02, 2.3820e-04, -5.9263e-03, -1.1256e-04, -4.3002e-04]
AlezioCompact.MR16 Modificador COP (ratedCOP = 4.10): [1.2697e+00, 3.5716e-02, 1.5271e-04, -1.2225e-02, -3.8477e-05, -3.9850e-04]

MiniChiller.KMCI5 Modificador COP (ratedCOP = 4.35): [2.1458e-01, 2.5899e-02, -5.8656e-05, 5.5219e-02, -9.8560e-04, -3.7492e-04]
MiniChiller.KMCI7 Modificador COP (ratedCOP = 4.26): [2.3059e-01, 2.6300e-02, -6.0441e-05, 5.5185e-02, -9.8923e-04, -3.8225e-04]
MiniChiller.KMCI10 Modificador COP (ratedCOP = 4.66): [1.7098e+00, 4.7388e-02, 6.4430e-04, -3.8193e-02, 2.6840e-04, -7.3382e-04]
MiniChiller.KMCI12 Modificador COP (ratedCOP = 4.21): [2.6013e-01, 2.7739e-02, -6.2000e-05, 5.6785e-02, -1.0235e-03, -4.0486e-04]
MiniChiller.KMCI14 Modificador COP (ratedCOP = 4.21): [1.7362e+00, 4.1523e-02, 5.4852e-04, -4.1185e-02, 3.3474e-04, -6.2939e-04]
MiniChiller.KMCI16 Modificador COP (ratedCOP = 4.25): [1.5710e+00, 3.8934e-02, 5.0683e-04, -3.3606e-02, 2.4529e-04, -5.6942e-04]

AquarisV4Pro.Pro125 Modificador COP (ratedCOP = 4.31): [1.3766e+00, 5.0537e-02, 3.3762e-04, -1.7715e-02, 1.3293e-05, -6.6060e-04]
AquarisV4Pro.Pro135 Modificador COP (ratedCOP = 4.14): [1.8259e+00, 3.7112e-02, 8.1545e-05, -3.6527e-02, 2.4726e-04, -4.0043e-04]
AquarisV4Pro.Pro250 Modificador COP (ratedCOP = 4.05): [1.1616e+00, 4.6708e-02, 3.1190e-04, -8.3608e-03, -7.2364e-05, -5.8120e-04]
AquarisV4Pro.Pro250F Modificador COP (ratedCOP = 4.22): [1.4952e+00, 4.1449e-02, 1.8663e-04, -2.3923e-02, 1.1181e-04, -4.7832e-04]
AquarisV4Pro.Pro260 Modificador COP (ratedCOP = 4.05): [2.2066e+00, 4.5137e-02, 3.3604e-04, -5.4796e-02, 4.4345e-04, -5.9085e-04]
AquarisV4Pro.Pro Modificador270 COP (ratedCOP = 4.05): [1.1393e+00, 4.1238e-02, 6.2761e-05, -3.5595e-03, -1.4436e-04, -5.4362e-04]
AquarisV4Pro.Pro Modificador235LT COP (ratedCOP = 4.07): [2.0971e+00, 4.2031e-02, 1.8116e-04, -4.8313e-02, 3.7383e-04, -5.6774e-04]


AquarisV4ProMax.ProMAX466 Modificador COP (ratedCOP = 4.06): [1.8941e+00, 5.7234e-02, 3.1887e-04, -4.2164e-02, 3.1379e-04, -8.1778e-04]
AquarisV4ProMax.ProMAX475 Modificador COP (ratedCOP = 4.05): [1.8630e+00, 5.5317e-02, 3.0313e-04, -4.0703e-02, 2.9832e-04, -8.0482e-04]
AquarisV4ProMax.ProMAX485 Modificador COP (ratedCOP = 4.05): [1.9391e+00, 5.5943e-02, 2.2218e-04, -4.4600e-02, 3.4464e-04, -8.5920e-04]
AquarisV4ProMax.ProMAX695 Modificador COP (ratedCOP = 3.91): [1.8234e+00, 5.3657e-02, 3.3076e-04, -3.8677e-02, 2.7388e-04, -7.5611e-04]
AquarisV4ProMax.ProMAX6105 Modificador COP (ratedCOP = 4.05): [1.9808e+00, 5.8248e-02, 2.8656e-04, -4.5907e-02, 3.5268e-04, -8.5227e-04]
AquarisV4ProMax.ProMAX6115 Modificador COP (ratedCOP = 3.90): [2.2393e+00, 5.7273e-02, 2.5897e-04, -5.7843e-02, 4.8285e-04, -8.5880e-04]


KCA.KCA Modificador COP (ratedCOP = 2.18): [1.7945e+00, 9.3007e-02, -1.4247e-03, -4.9022e-02, 3.0747e-04, -2.3411e-04]

'''

from dataPoints.AquarisV5.AquarisV516COP import xdata, ydata,zdata,ratedCop,ratedCop45,zdataConsumo,zdataConsumo45


from scipy.optimize import curve_fit

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



def bicuadratica(xy,c1,c2,c3,c4,c5,c6):
    x,y = xy
    valorFuncion = c1 + c2 * x + c3 * x**2 + c4 * y + c5 *y**2 + c6 * x * y
    return valorFuncion
    
def corrigeZDataConsumoPorInfluenciaCurvaCapacidad(xData,yData,
                                                   zDataConsumo45,
                                                   curvaCoeficientesPotencia = "1.0234e+00; 4.6530e-03; -1.9170e-04; 1.7866e-02; -7.1883e-05; -5.6136e-05"):
    
    c1,c2,c3,c4,c5,c6 = [float(x) for x in curvaCoeficientesPotencia.split(";")]
    zDataCorregida = []
    for x,y,z in zip(xData,yData,zDataConsumo45):
        modificadorPotencia = bicuadratica((y,x),c1,c2,c3,c4,c5,c6)
        zDataCorregida.append(z*modificadorPotencia)
        
    return zDataCorregida
        
    
def consumoEfectivoHulc(xy,
                        coeficientesCapacidad = [0.8232,0.0281,0.0002,0.0,0.0,0.0],
                        coeficientesConsumo = [0.9496,0.009,-0.0001,0.0,0.0,0]):
    modificadorCapacidad = bicuadratica(xy,coeficientesCapacidad[0],coeficientesCapacidad[1],coeficientesCapacidad[2],coeficientesCapacidad[3],coeficientesCapacidad[4],coeficientesCapacidad[5])
    modificadorConsumo = bicuadratica(xy,coeficientesConsumo[0],coeficientesConsumo[1],coeficientesConsumo[2],coeficientesConsumo[3],coeficientesConsumo[4],coeficientesConsumo[5])
    
    modificadorEfectivoConsumo = modificadorConsumo / modificadorCapacidad
    return modificadorEfectivoConsumo
    
    
if __name__ == '__main__':
    popt, pcov = curve_fit(bicuadratica, (xdata,ydata), zdata)
    print u"KCA.KCA Modificador COP (ratedCOP = {0:.2f}): [{1}]".format(ratedCop,", ".join([u"{:.4e}".format(x) for x in popt]))
    
 
    
    
    zdataCurvaBicuadratica = [bicuadratica(xy,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5]) for xy in zip(xdata,ydata)]
    zdataCurvaBicuadraticaOpenStudio = [bicuadratica(xy,1.19713,0.077849,-1.6e-006,-0.02675,0.000296,-0.00112) for xy in zip(xdata,ydata)]
    
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Puntos de funcionamiento de partida
    ax.scatter(xdata, ydata, zdata, c='r', marker='^',label=u'Valores tabla')
    ax.scatter(xdata, ydata, zdataCurvaBicuadratica, c='b', marker='*',label=u'Valores bicuadratica')
    ax.scatter(xdata, ydata, zdataCurvaBicuadraticaOpenStudio, c='g', marker='o',label=u'Valores defecto OS')
    
    ax.scatter([7], [35], [1.0], c='k', marker='o',label=u'Punto neutro',s=50)
    
    ax.set_xlabel(u'Tª aire')
    ax.set_ylabel(u'Tª agua')
    ax.set_zlabel(u'Modificador COP')
    
    ax.legend()
    
    plt.show()
    
    
    
    
    # Lo siguiente es para calcular los coeficientes en HULC
    # Lo siguiente es para calcular los coeficientes en HULC
    # Lo siguiente es para calcular los coeficientes en HULC
    # Lo siguiente es para calcular los coeficientes en HULC
    # Lo siguiente es para calcular los coeficientes en HULC
    # Lo siguiente es para calcular los coeficientes en HULC
    # Lo siguiente es para calcular los coeficientes en HULC
    # Lo siguiente es para calcular los coeficientes en HULC
    
    
    
    
    
    
    # Hay que tener en cuenta que la curva modifcadora de la capacidad afecta también al consumo efectivo
    # v4 pro 125
#     zdataConsumoCorregido = corrigeZDataConsumoPorInfluenciaCurvaCapacidad(xdata,ydata,
#                                                                   zdataConsumo45,
#                                                                   curvaCoeficientesPotencia = "1.0234e+00; 4.6530e-03; -1.9170e-04; 1.7866e-02; -7.1883e-05; -5.6136e-05")    
    # v506
#     zdataConsumoCorregido = corrigeZDataConsumoPorInfluenciaCurvaCapacidad(xdata,ydata,
#                                                                   zdataConsumo45,
#                                                                   curvaCoeficientesPotencia = "1.0746e+00; -3.1247e-03; 2.8345e-05; 5.7476e-03; 4.2503e-04; -5.2404e-05")
#     
#     popt, pcov = curve_fit(bicuadratica, (xdata,ydata), zdataConsumoCorregido)
#        
#     print u"####################################################################################################"
#     print u"##### ATENCION: RECUERDA QUE HAY QUE ACTUALIZAR LOS COEFICIENTES DE HULC DE LA CAPACIDAD ###########"
#     print u"####################################################################################################"
#     
#        
#     print u"HULC"
#     print u"Coeficientes Modificador Consumo (ratedCOP = {0:.2f}): {1}".format(ratedCop45,"; ".join([u"{:.4e}".format(x) for x in [popt[0], popt[3],popt[4],popt[1],popt[2],popt[5]]]))    
#     print u"Exponentes: 0;0; 1;0; 2;0; 0;1; 0;2; 1;1" 
#     print u"Limites var 1: de {0} a {1}".format(min(ydata),max(ydata))  # reordenamos, primero impulsión y luego exterior
#     print u"Limites var 2: de {0} a {1}".format(min(xdata),max(xdata))  # 
#     
#     zdataCurvaBicuadratica = [consumoEfectivoHulc(xy,
#                                                   coeficientesCapacidad = [1.0234e+00,  1.7866e-02, -7.1883e-05, 4.6530e-03, -1.9170e-04, -5.6136e-05],
#                                                   coeficientesConsumo = [6.7652e-01,  -2.3289e-02, -1.2028e-04, 7.6842e-03, 4.3060e-05, 1.7433e-04]) for xy in zip(xdata,ydata)]
#     
#     zdataCurvaBicuadraticaHulcAireAguaBDC_ACS = [consumoEfectivoHulc(xy) for xy in zip(xdata,ydata)]
#     
#     zdataCurvaBicuadraticaAltherma = [consumoEfectivoHulc(xy,
#                                                           coeficientesCapacidad = [1.67806, 0.041495,0.000404, -0.03092, 0.000265,-0.000312],
#                                                           coeficientesConsumo = [0.403277, -0.009013,-0.000143,0.007422,0.000116,0.00032]) for xy in zip(xdata,ydata)]
#     
#     
# 
#     
#     
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     
#     # Puntos de funcionamiento de partida
#     ax.scatter(xdata, ydata, zdataConsumo45, c='r', marker='^',label=u'Valores tabla')
#     ax.scatter(xdata, ydata, zdataCurvaBicuadratica, c='b', marker='*',label=u'Valores bicuadratica')
#     ax.scatter(xdata, ydata, zdataCurvaBicuadraticaHulcAireAguaBDC_ACS, c='c', marker='.',label=u'EQ_ED_AireAgua_BDC-ACS-Defecto curva efectiva')
#     ax.scatter(xdata, ydata, zdataCurvaBicuadraticaAltherma, c='m', marker='.',label=u'Altherma')
#     ax.scatter([7], [35], [1.0], c='k', marker='o',label=u'Punto neutro 35º',s=50)
#     ax.scatter([7], [45], [1.0], c='k', marker='o',label=u'Punto neutro 45º',s=50)
#     
#     ax.set_title(u"Modificador del consumo")
#     ax.set_xlabel(u'Tª aire')
#     ax.set_ylabel(u'Tª agua')
#     ax.set_zlabel(u'Modificador Consumo')
#     
#     ax.legend()
#     
#     plt.show()    
# 
# 
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     
#     # Puntos de funcionamiento de partida
#     ax.scatter(xdata, ydata, [ratedCop45 / x for x in zdataCurvaBicuadratica], c='b', marker='*',label=u'Valores bicuadratica')
#     ax.scatter(xdata, ydata, [2.72 / x for x in zdataCurvaBicuadraticaHulcAireAguaBDC_ACS], c='c', marker='.',label=u'EQ_ED_AireAgua_BDC-ACS-Defecto curva efectiva')
#     ax.scatter(xdata, ydata, [3.03 / x for x in zdataCurvaBicuadraticaAltherma], c='m', marker='.',label=u'Altherma')
#     ax.scatter([7], [45], [ratedCop45], c='k', marker='o',label=u'COP nominal aquaris',s=50)
#     ax.scatter([7], [45], [3.03], c='k', marker='o',label=u'COP nominal altherma',s=50)
#     
#     ax.set_title(u"COP")
#     ax.set_xlabel(u'Tª aire')
#     ax.set_ylabel(u'Tª agua')
#     ax.set_zlabel(u'COP')
#     
#     ax.legend()
#     plt.show()    
#     
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     
#     xyzAquaris = filter(lambda aux: aux[1] == 45,zip(xdata,ydata,[ratedCop45 / x for x in zdataCurvaBicuadratica]))
#     xyzAquarisConCurvaPorDefectoHULC = filter(lambda aux: aux[1] == 45,zip(xdata,ydata,[ratedCop45 / x for x in zdataCurvaBicuadraticaHulcAireAguaBDC_ACS]))
#     
#     
#     xyzAltherma = filter(lambda aux: aux[1] == 45,zip(xdata,ydata,[3.03 / x for x in zdataCurvaBicuadraticaAltherma]))
#     
#     ax.plot([aux[0] for aux in xyzAquaris],[aux[2] for aux in xyzAquaris])
#     ax.plot([aux[0] for aux in xyzAltherma],[aux[2] for aux in xyzAltherma])
#     ax.plot([aux[0] for aux in xyzAquarisConCurvaPorDefectoHULC],[aux[2] for aux in xyzAquarisConCurvaPorDefectoHULC])
#     ax.set_title(u'COP a 45º')
#     ax.legend([u"Aquaris",u"Altherma",u"Aquaris con curva por defecto"])
#     
#     plt.show()    
    
    
