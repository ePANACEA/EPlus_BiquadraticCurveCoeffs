# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 8.60
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría   ---    T entrada aire    Capacidad frío kW
listaPuntosStr = """5    20    8.60
5    25    8.35
5    30    8.30
5    35    7.78
5    40    7.62
5    45    7.21
7    20    9.17
7    25    8.97
7    30    8.80
7    35    8.51
7    40    8.17
7    45    7.52
10    20    10.06
10    25    10.04
10    30    9.79
10    35    9.60
10    40    8.99
10    45    8.34
12    20    10.26
12    25    10.29
12    30    10.08
12    35    10.06
12    40    9.45
12    45    8.79
15    20    10.55
15    25    10.66
15    30    10.51
15    35    10.74
15    40    10.14
15    45    9.46
18    20    11.64
18    25    11.71
18    30    11.47
18    35    11.60
18    40    10.88
18    45    10.27

"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]