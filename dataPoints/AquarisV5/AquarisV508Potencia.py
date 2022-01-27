# -*- coding: cp1252 -*-
'''
Created on 7 oct. 2018

@author: mapas
'''
ratedPower = 7.81
ratedPower45 = 7.58
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    Capacidad
listaPuntosStr = """
-10    25    6.63
-7    25    6.64
-2    25    6.70
2    25    6.70
7    25    7.74
12    25    8.27
-10    30    6.60
-7    30    6.64
-2    30    6.66
2    30    6.74
7    30    7.78
12    30    8.27
-10    35    6.59
-7    35    6.60
-2    35    6.56
2    35    6.61
7    35    7.81
12    35    8.16
-10    40    6.52
-7    40    6.49
-2    40    6.53
2    40    6.59
7    40    7.70
12    40    8.09
-10    45    6.48
-7    45    6.57
-2    45    6.55
2    45    6.58
7    45    7.58
12    45    7.98
-10    50    6.52
-7    50    6.51
-2    50    6.52
2    50    6.60
7    50    7.55
12    50    7.87
-10    55    6.53
-7    55    6.54
-2    55    6.49
2    55    6.67
7    55    7.55
12    55    7.79

"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador de la capacidad
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]
zdata45 = [float(x.split('    ')[2]) / ratedPower45 for x in listaPuntos]