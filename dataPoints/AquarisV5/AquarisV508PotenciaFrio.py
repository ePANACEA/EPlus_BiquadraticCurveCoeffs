# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 6.08
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría   ---    T entrada aire    Capacidad frío kW
listaPuntosStr = """5    20    6.16
5    25    6.17
5    30    6.02
5    35    5.61
5    40    5.33
5    45    5.03
7    20    6.58
7    25    6.59
7    30    6.43
7    35    6.08
7    40    5.71
7    45    5.36
10    20    7.26
10    25    7.28
10    30    7.08
10    35    6.71
10    40    6.26
10    45    5.91
12    20    7.43
12    25    7.42
12    30    7.24
12    35    6.92
12    40    6.49
12    45    6.12
15    20    7.68
15    25    7.62
15    30    7.49
15    35    7.25
15    40    6.84
15    45    6.42
18    20    8.24
18    25    8.19
18    30    8.00
18    35    7.72
18    40    7.29
18    45    6.85
"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]