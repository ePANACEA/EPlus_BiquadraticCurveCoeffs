# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 16.30
ratedPower45 = 15.77
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    Capacidad
listaPuntosStr = """
-10    25    11.85
-7    25    12.30
-2    25    12.68
2    25    14.03
7    25    16.58
12    25    16.42
-10    30    11.84
-7    30    12.19
-2    30    12.88
2    30    14.17
7    30    16.39
12    30    16.29
-10    35    11.79
-7    35    12.00
-2    35    12.81
2    35    14.05
7    35    16.30
12    35    16.13
-10    40    11.75
-7    40    11.99
-2    40    12.65
2    40    14.04
7    40    16.13
12    40    15.95
-10    45    11.61
-7    45    11.86
-2    45    12.56
2    45    14.36
7    45    15.77
12    45    15.79
-10    50    11.64
-7    50    11.80
-2    50    12.45
2    50    14.10
7    50    15.84
12    50    15.47
-10    55    11.30
-7    55    11.79
-2    55    12.39
2    55    14.15
7    55    15.63
12    55    15.27
"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador de la capacidad
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]
zdata45 = [float(x.split('    ')[2]) / ratedPower45 for x in listaPuntos]