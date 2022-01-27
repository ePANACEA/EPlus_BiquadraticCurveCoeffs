# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 5.02
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría   ---    T entrada aire    Capacidad frío kW
listaPuntosStr = """5    20    4.91
5    25    4.92
5    30    4.86
5    35    4.70
5    40    4.42
5    45    4.14
7    20    5.26
7    25    5.26
7    30    5.19
7    35    5.02
7    40    4.72
7    45    4.42
10    20    5.80
10    25    5.82
10    30    5.75
10    35    5.55
10    40    5.23
10    45    4.90
12    20    5.91
12    25    5.88
12    30    5.81
12    35    5.64
12    40    5.32
12    45    4.99
15    20    6.08
15    25    5.98
15    30    5.90
15    35    5.78
15    40    5.46
15    45    5.13
18    20    6.50
18    25    6.38
18    30    6.32
18    35    6.18
18    40    5.83
18    45    5.48

"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]