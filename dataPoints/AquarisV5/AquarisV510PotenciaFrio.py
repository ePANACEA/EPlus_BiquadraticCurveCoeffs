# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 7.53
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría   ---    T entrada aire    Capacidad frío kW
listaPuntosStr = """5    20    7.20
5    25    7.49
5    30    7.21
5    35    7.03
5    40    6.78
5    45    6.28
7    20    7.79
7    25    7.83
7    30    7.78
7    35    7.53
7    40    7.22
7    45    6.77
10    20    8.61
10    25    8.82
10    30    8.72
10    35    8.25
10    40    7.93
10    45    7.47
12    20    8.74
12    25    8.88
12    30    8.85
12    35    8.42
12    40    8.07
12    45    7.62
15    20    8.93
15    25    8.97
15    30    9.06
15    35    8.67
15    40    8.28
15    45    7.86
18    20    9.78
18    25    9.87
18    30    9.78
18    35    9.50
18    40    8.97
18    45    8.44
"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]