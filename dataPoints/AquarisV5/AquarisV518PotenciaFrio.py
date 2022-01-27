# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 15.04
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T salida agua fría   ---    T entrada aire    Capacidad frío kW
listaPuntosStr = """
5    20    13.37
5    25    13.70
5    30    14.06
5    35    14.26
5    40    13.39
5    45    12.63
7    20    14.24
7    25    14.82
7    30    15.01
7    35    15.04
7    40    14.33
7    45    13.36
10    20    15.63
10    25    16.19
10    30    16.29
10    35    16.67
10    40    15.77
10    45    14.82
12    20    15.78
12    25    16.18
12    30    16.17
12    35    16.34
12    40    15.37
12    45    14.51
15    20    16.01
15    25    16.17
15    30    16.00
15    35    15.85
15    40    14.78
15    45    14.04
18    20    17.39
18    25    17.51
18    30    17.33
18    35    17.10
18    40    16.17
18    45    15.18

"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]