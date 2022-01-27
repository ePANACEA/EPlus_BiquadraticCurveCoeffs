'''
Created on 7 oct. 2018

@author: mapas
'''


# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    COP
ratedCop = 4.40
ratedCop45 = 3.52
listaPuntosStr = """-10    25    3.19
-7    25    3.43
-2    25    3.85
2    25    4.66
7    25    5.62
12    25    7.13
-10    30    2.91
-7    30    3.11
-2    30    3.49
2    30    4.17
7    30    4.94
12    30    6.10
-10    35    2.66
-7    35    2.83
-2    35    3.15
2    35    3.81
7    35    4.40
12    35    5.29
-10    40    2.47
-7    40    2.60
-2    40    2.87
2    40    3.37
7    40    3.91
12    40    4.65
-10    45    2.26
-7    45    2.37
-2    45    2.62
2    45    3.05
7    45    3.52
12    45    4.14
-10    50    2.10
-7    50    2.20
-2    50    2.38
2    50    2.76
7    50    3.18
12    50    3.69
-10    55    1.88
-7    55    2.04
-2    55    2.21
2    55    2.63
7    55    2.88
12    55    3.31


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