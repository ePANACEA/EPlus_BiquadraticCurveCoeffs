# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''

# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría  ---  T entrada aire    EER
ratedEER = 3.25
ratedEIR = 1.0 / ratedEER
listaPuntosStr = """
5    20    5.14
5    25    4.30
5    30    3.65
5    35    3.13
5    40    2.70
5    45    2.32
7    20    5.53
7    25    4.62
7    30    3.77
7    35    3.25
7    40    2.82
7    45    2.43
10    20    6.08
10    25    5.01
10    30    4.05
10    35    3.56
10    40    3.02
10    45    2.61
12    20    7.04
12    25    5.76
12    30    4.69
12    35    4.04
12    40    3.43
12    45    2.94
15    20    8.81
15    25    7.26
15    30    6.05
15    35    5.06
15    40    4.28
15    45    3.61
18    20    9.71
18    25    7.98
18    30    6.53
18    35    5.40
18    40    4.55
18    45    3.86

"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [ratedEER / float(x.split('    ')[2]) for x in listaPuntos]