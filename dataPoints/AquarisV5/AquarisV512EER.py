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
5    20    4.54
5    25    3.99
5    30    3.42
5    35    2.84
5    40    2.52
5    45    2.19
7    20    4.96
7    25    4.20
7    30    3.66
7    35    3.05
7    40    2.66
7    45    2.26
10    20    5.48
10    25    4.65
10    30    3.94
10    35    3.36
10    40    2.85
10    45    2.44
12    20    5.99
12    25    5.01
12    30    4.26
12    35    3.57
12    40    3.03
12    45    2.59
15    20    6.91
15    25    5.64
15    30    4.80
15    35    3.90
15    40    3.32
15    45    2.82
18    20    7.56
18    25    6.20
18    30    5.19
18    35    4.16
18    40    3.51
18    45    3.01


"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [ratedEER / float(x.split('    ')[2]) for x in listaPuntos]