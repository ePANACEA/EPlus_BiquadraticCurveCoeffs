# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 4.23
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría   ---    T entrada aire    Capacidad frío kW

listaPuntosStr = """
5    20    4.41
5    25    4.36
5    30    4.17
5    35    3.96
5    40    3.72
5    45    3.49
7    20    4.72
7    25    4.67
7    30    4.47
7    35    4.23
7    40    3.99
7    45    3.73
10    20    5.19
10    25    5.15
10    30    4.94
10    35    4.69
10    40    4.41
10    45    4.14
12    20    5.47
12    25    5.36
12    30    5.14
12    35    4.88
12    40    4.59
12    45    4.31
15    20    5.88
15    25    5.67
15    30    5.43
15    35    5.16
15    40    4.87
15    45    4.57
18    20    6.28
18    25    6.06
18    30    5.80
18    35    5.51
18    40    5.20
18    45    4.88

"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]