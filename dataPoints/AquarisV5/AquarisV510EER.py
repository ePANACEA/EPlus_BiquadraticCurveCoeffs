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
5    20    4.86
5    25    4.04
5    30    3.39
5    35    2.97
5    40    2.59
5    45    2.19
7    20    5.20
7    25    4.46
7    30    3.71
7    35    3.15
7    40    2.73
7    45    2.34
10    20    5.85
10    25    4.73
10    30    4.02
10    35    3.41
10    40    2.95
10    45    2.54
12    20    6.36
12    25    5.11
12    30    4.32
12    35    3.64
12    40    3.14
12    45    2.70
15    20    7.29
15    25    5.79
15    30    4.86
15    35    4.05
15    40    3.45
15    45    2.97
18    20    8.00
18    25    6.49
18    30    5.35
18    35    4.41
18    40    3.70
18    45    3.15


"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [ratedEER / float(x.split('    ')[2]) for x in listaPuntos]