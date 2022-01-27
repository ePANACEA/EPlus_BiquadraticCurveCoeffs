# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''

# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría  ---  T entrada aire    EER
ratedEER = 3.15
ratedEIR = 1.0 / ratedEER
listaPuntosStr = """
5    20    5.02
5    25    4.24
5    30    3.55
5    35    2.98
5    40    2.59
5    45    2.26
7    20    5.39
7    25    4.56
7    30    3.75
7    35    3.15
7    40    2.73
7    45    2.37
10    20    6.03
10    25    4.93
10    30    4.11
10    35    3.35
10    40    2.90
10    45    2.54
12    20    6.83
12    25    5.58
12    30    4.62
12    35    3.79
12    40    3.26
12    45    2.82
15    20    8.40
15    25    6.87
15    30    5.69
15    35    4.75
15    40    4.02
15    45    3.42
18    20    9.26
18    25    7.54
18    30    6.16
18    35    5.02
18    40    4.28
18    45    3.64


"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [ratedEER / float(x.split('    ')[2]) for x in listaPuntos]