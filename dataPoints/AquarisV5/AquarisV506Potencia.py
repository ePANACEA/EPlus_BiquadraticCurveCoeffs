# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 6.08
ratedPower45 = 5.88
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    Capacidad
listaPuntosStr = """
-10    25    5.95
-10    30    5.87
-10    35    5.82
-10    40    5.82
-10    45    5.83
-10    50    5.83
-10    55    5.84
-7    25    5.96
-7    30    5.92
-7    35    6.0
-7    40    5.86
-7    45    5.85
-7    50    5.89
-7    55    5.84
-2    25    5.95
-2    30    5.89
-2    35    5.92
-2    40    5.77
-2    45    5.86
-2    50    5.78
-2    55    5.76
2    25    5.92
2    30    5.93
2    35    6.07
2    40    5.85
2    45    5.77
2    50    6.0
2    55    5.99
7    25    6.21
7    30    6.13
7    35    6.08
7    40    6.04
7    45    5.88
7    50    6.07
7    55    6.03
12    25    6.68
12    30    6.65
12    35    6.57
12    40    6.55
12    45    6.53
12    50    6.38
12    55    6.31

"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador de la capacidad
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]
zdata45 = [float(x.split('    ')[2]) / ratedPower45 for x in listaPuntos]