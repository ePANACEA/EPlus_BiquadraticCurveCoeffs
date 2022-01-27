# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 10.10
ratedPower45 = 9.76
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    Capacidad
listaPuntosStr = """
-10    25    8.33
-7    25    8.41
-2    25    8.63
2    25    9.15
7    25    10.23
12    25    10.92
-10    30    8.22
-7    30    8.42
-2    30    8.52
2    30    9.22
7    30    10.17
12    30    10.83
-10    35    8.22
-7    35    8.30
-2    35    8.56
2    35    9.50
7    35    10.10
12    35    10.74
-10    40    8.19
-7    40    8.35
-2    40    8.51
2    40    9.18
7    40    10.03
12    40    10.63
-10    45    8.17
-7    45    8.23
-2    45    8.40
2    45    9.41
7    45    9.76
12    45    10.49
-10    50    8.22
-7    50    8.25
-2    50    8.35
2    50    9.28
7    50    9.79
12    50    10.36
-10    55    8.11
-7    55    8.26
-2    55    8.31
2    55    9.01
7    55    9.73
12    55    10.21


"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador de la capacidad
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]
zdata45 = [float(x.split('    ')[2]) / ratedPower45 for x in listaPuntos]