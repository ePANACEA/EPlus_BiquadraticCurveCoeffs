# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 14.10
ratedPower45 = 13.56
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    Capacidad
listaPuntosStr = """
-10    25    10.70
-7    25    10.90
-2    25    11.24
2    25    12.43
7    25    14.26
12    25    15.00
-10    30    10.65
-7    30    10.78
-2    30    11.47
2    30    12.54
7    30    14.09
12    30    14.88
-10    35    10.64
-7    35    10.70
-2    35    11.38
2    35    13.02
7    35    14.10
12    35    14.74
-10    40    10.65
-7    40    10.72
-2    40    11.25
2    40    12.50
7    40    13.87
12    40    14.58
-10    45    10.50
-7    45    10.65
-2    45    11.17
2    45    12.69
7    45    13.56
12    45    14.43
-10    50    10.48
-7    50    10.68
-2    50    11.11
2    50    12.40
7    50    13.62
12    50    14.14
-10    55    10.28
-7    55    10.58
-2    55    10.98
2    55    12.40
7    55    13.44
12    55    13.96
"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador de la capacidad
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]
zdata45 = [float(x.split('    ')[2]) / ratedPower45 for x in listaPuntos]