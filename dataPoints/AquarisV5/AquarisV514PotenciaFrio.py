# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 11.48
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría   ---    T entrada aire    Capacidad frío kW
listaPuntosStr = """
5    20    10.39
5    25    10.78
5    30    11.19
5    35    10.88
5    40    10.25
5    45    9.58
7    20    11.33
7    25    11.61
7    30    12.04
7    35    11.48
7    40    10.94
7    45    10.18
10    20    12.30
10    25    12.74
10    30    13.10
10    35    12.77
10    40    11.93
10    45    11.21
12    20    13.14
12    25    13.25
12    30    13.34
12    35    12.89
12    40    12.10
12    45    11.33
15    20    14.40
15    25    14.02
15    30    13.71
15    35    13.07
15    40    12.35
15    45    11.52
18    20    15.60
18    25    15.05
18    30    14.76
18    35    14.00
18    40    13.25
18    45    12.44
"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]