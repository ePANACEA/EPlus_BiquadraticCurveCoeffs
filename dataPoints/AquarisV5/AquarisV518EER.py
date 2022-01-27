# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''

# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría  ---  T entrada aire    EER
ratedEER = 3.08
ratedEIR = 1.0 / ratedEER
listaPuntosStr = """
5    20    5.00
5    25    4.15
5    30    3.52
5    35    2.96
5    40    2.57
5    45    2.25
7    20    5.23
7    25    4.35
7    30    3.65
7    35    3.08
7    40    2.69
7    45    2.33
10    20    5.75
10    25    4.80
10    30    4.07
10    35    3.33
10    40    2.88
10    45    2.50
12    20    6.51
12    25    5.34
12    30    4.51
12    35    3.69
12    40    3.16
12    45    2.75
15    20    8.09
15    25    6.42
15    30    5.42
15    35    4.46
15    40    3.76
15    45    3.25
18    20    8.73
18    25    7.04
18    30    5.80
18    35    4.76
18    40    4.05
18    45    3.45

"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [ratedEER / float(x.split('    ')[2]) for x in listaPuntos]