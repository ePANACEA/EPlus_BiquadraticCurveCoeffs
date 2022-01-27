# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''


# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    EER
ratedCop = 4.51
ratedCop45 = 3.54
listaPuntosStr = """-10    25    3.35
-10    30    3.02
-10    35    2.76
-10    40    2.48
-10    45    2.33
-10    50    2.11
-10    55    2.01
-7    25    3.57
-7    30    3.22
-7    35    2.86
-7    40    2.67
-7    45    2.44
-7    50    2.25
-7    55    2.03
-2    25    4.1
-2    30    3.6
-2    35    3.22
-2    40    2.93
-2    45    2.67
-2    50    2.45
-2    55    2.17
2    25    4.79
2    30    4.26
2    35    3.82
2    40    3.34
2    45    3.06
2    50    2.76
2    55    2.58
7    25    5.93
7    30    5.14
7    35    4.51
7    40    3.93
7    45    3.54
7    50    3.15
7    55    2.82
12    25    7.37
12    30    6.22
12    35    5.25
12    40    4.64
12    45    4.02
12    50    3.56
12    55    3.19
"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [float(x.split('    ')[2]) / ratedCop for x in listaPuntos]
zdata45 = [float(x.split('    ')[2]) / ratedCop45 for x in listaPuntos]

# modificador del consumo (para hulc)
zdataConsumo = [1.0/x for x in zdata]
zdataConsumo45 = [1.0/x for x in zdata45]

if __name__ == '__main__':
    for x,y,z in zip(xdata,ydata,zdata):
        print x,y,z