# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 17.90
ratedPower45 = 17.30
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    Capacidad
listaPuntosStr = """
-10    25    12.20
-7    25    12.93
-2    25    13.78
2    25    14.94
7    25    18.13
12    25    18.66
-10    30    12.19
-7    30    12.53
-2    30    13.50
2    30    14.73
7    30    18.03
12    30    18.48
-10    35    12.27
-7    35    12.61
-2    35    13.59
2    35    15.12
7    35    17.90
12    35    18.26
-10    40    11.81
-7    40    12.41
-2    40    13.44
2    40    14.99
7    40    17.64
12    40    18.11
-10    45    12.03
-7    45    12.46
-2    45    13.35
2    45    14.90
7    45    17.32
12    45    17.69
-10    50    12.08
-7    50    12.29
-2    50    13.27
2    50    14.62
7    50    17.32
12    50    17.57
-10    55    11.40
-7    55    12.30
-2    55    13.14
2    55    14.73
7    55    17.25
12    55    17.33
"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador de la capacidad
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]
zdata45 = [float(x.split('    ')[2]) / ratedPower45 for x in listaPuntos]