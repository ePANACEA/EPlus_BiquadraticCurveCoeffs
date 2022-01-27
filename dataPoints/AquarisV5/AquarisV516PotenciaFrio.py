# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 13.80
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría   ---    T entrada aire    Capacidad frío kW
listaPuntosStr = """
5    20    12.14
5    25    12.14
5    30    12.80
5    35    12.86
5    40    12.17
5    45    11.43
7    20    12.85
7    25    12.91
7    30    13.59
7    35    13.80
7    40    13.10
7    45    12.23
10    20    14.08
10    25    14.30
10    30    15.00
10    35    15.05
10    40    14.21
10    45    13.55
12    20    14.48
12    25    14.54
12    30    14.89
12    35    14.94
12    40    14.11
12    45    13.33
15    20    15.08
15    25    14.89
15    30    14.73
15    35    14.77
15    40    13.95
15    45    13.01
18    20    16.23
18    25    16.00
18    30    16.02
18    35    15.80
18    40    14.96
18    45    14.04

"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]