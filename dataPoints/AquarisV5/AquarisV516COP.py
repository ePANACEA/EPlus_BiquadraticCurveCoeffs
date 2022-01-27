'''
Created on 7 oct. 2018

@author: mapas
'''


# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    COP
ratedCop = 4.67
ratedCop45 = 3.72
listaPuntosStr = """-10    25    3.20
-7    25    3.45
-2    25    3.99
2    25    4.83
7    25    6.05
12    25    7.91
-10    30    2.91
-7    30    3.13
-2    30    3.61
2    30    4.30
7    30    5.30
12    30    6.65
-10    35    2.67
-7    35    2.86
-2    35    3.23
2    35    3.88
7    35    4.67
12    35    5.77
-10    40    2.44
-7    40    2.60
-2    40    2.94
2    40    3.49
7    40    4.13
12    40    5.02
-10    45    2.25
-7    45    2.44
-2    45    2.68
2    45    3.13
7    45    3.72
12    45    4.43
-10    50    2.09
-7    50    2.21
-2    50    2.45
2    50    2.87
7    50    3.32
12    50    3.93
-10    55    1.92
-7    55    2.05
-2    55    2.25
2    55    2.60
7    55    3.02
12    55    3.51


"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador del rendimiento
zdata = [float(x.split('    ')[2]) / ratedCop for x in listaPuntos]
zdata45 = [float(x.split('    ')[2]) / ratedCop45 for x in listaPuntos]

# modificador del consumo (para hulc)
zdataConsumo = [1.0/x for x in zdata]
zdataConsumo45 = [1.0/x for x in zdata45]

if __name__ == '__main__':
    for x,y,z in zip(xdata,ydata,zdata):
        print x,y,z