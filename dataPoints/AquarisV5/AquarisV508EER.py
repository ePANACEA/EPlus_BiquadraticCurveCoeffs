# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''

# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría  ---  T entrada aire    EER
ratedEER = 3.05
ratedEIR = 1.0 / ratedEER
listaPuntosStr = """
5    20    4.62
5    25    3.96
5    30    3.39
5    35    2.86
5    40    2.50
5    45    2.19
7    20    4.91
7    25    4.15
7    30    3.55
7    35    3.05
7    40    2.62
7    45    2.28
10    20    5.43
10    25    4.55
10    30    3.82
10    35    3.28
10    40    2.80
10    45    2.44
12    20    6.09
12    25    5.06
12    30    4.23
12    35    3.60
12    40    3.07
12    45    2.66
15    20    7.34
15    25    6.02
15    30    4.97
15    35    4.17
15    40    3.54
15    45    3.05
18    20    7.90
18    25    6.33
18    30    5.24
18    35    4.38
18    40    3.73
18    45    3.20

"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [ratedEER / float(x.split('    ')[2]) for x in listaPuntos]