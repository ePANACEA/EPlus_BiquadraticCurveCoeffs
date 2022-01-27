# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''

# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría  ---  T entrada aire    EER
ratedEER = 3.28
ratedEIR = 1.0 / ratedEER
listaPuntosStr = """5    20    4.99
5    25    4.26
5    30    3.65
5    35    3.12
5    40    2.67
5    45    2.31
7    20    5.34
7    25    4.53
7    30    3.87
7    35    3.28
7    40    2.82
7    45    2.41
10    20    5.89
10    25    4.94
10    30    4.22
10    35    3.59
10    40    3.04
10    45    2.62
12    20    6.77
12    25    5.61
12    30    4.74
12    35    4.00
12    40    3.38
12    45    2.90
15    20    8.42
15    25    6.89
15    30    5.70
15    35    4.74
15    40    3.98
15    45    3.39
18    20    9.15
18    25    7.43
18    30    6.09
18    35    5.02
18    40    4.22
18    45    3.57

"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [ratedEER / float(x.split('    ')[2]) for x in listaPuntos]