# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 11.80
ratedPower45 = 11.47
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    Capacidad
listaPuntosStr = """
-10    25    8.95
-7    25    9.01
-2    25    9.54
2    25    10.24
7    25    12.01
12    25    12.49
-10    30    8.93
-7    30    8.93
-2    30    9.50
2    30    10.16
7    30    11.89
12    30    12.39
-10    35    8.86
-7    35    8.90
-2    35    9.40
2    35    10.30
7    35    11.80
12    35    12.28
-10    40    8.92
-7    40    8.85
-2    40    9.45
2    40    10.38
7    40    11.71
12    40    12.11
-10    45    8.83
-7    45    8.91
-2    45    9.25
2    45    10.39
7    45    11.47
12    45    11.97
-10    50    8.71
-7    50    8.75
-2    50    9.19
2    50    10.05
7    50    11.46
12    50    11.84
-10    55    8.85
-7    55    8.85
-2    55    9.15
2    55    10.19
7    55    11.37
12    55    11.67

"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador de la capacidad
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]
zdata45 = [float(x.split('    ')[2]) / ratedPower45 for x in listaPuntos]