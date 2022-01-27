# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''

# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría  ---  T entrada aire    EER
ratedEER = 3.14
ratedEIR = 1.0 / ratedEER
listaPuntosStr = """5    20    4.90
5    25    4.10
5    30    3.49
5    35    2.98
5    40    2.57
5    45    2.22
7    20    5.13
7    25    4.40
7    30    3.69
7    35    3.14
7    40    2.69
7    45    2.32
10    20    5.80
10    25    4.75
10    30    4.03
10    35    3.40
10    40    2.92
10    45    2.51
12    20    6.61
12    25    5.39
12    30    4.51
12    35    3.79
12    40    3.23
12    45    2.77
15    20    8.26
15    25    6.70
15    30    5.47
15    35    4.54
15    40    3.82
15    45    3.27
18    20    8.98
18    25    7.22
18    30    5.81
18    35    4.82
18    40    4.05
18    45    3.45


"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [ratedEER / float(x.split('    ')[2]) for x in listaPuntos]