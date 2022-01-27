'''
Created on 7 oct. 2018

@author: mapas
'''


# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    COP
ratedCop = 4.38
ratedCop45 = 3.50
listaPuntosStr = """-10    25    3.29
-7    25    3.50
-2    25    3.97
2    25    4.73
7    25    5.86
12    25    7.10
-10    30    3.01
-7    30    3.17
-2    30    3.59
2    30    4.17
7    30    5.05
12    30    6.04
-10    35    2.70
-7    35    2.88
-2    35    3.17
2    35    3.72
7    35    4.38
12    35    5.22
-10    40    2.48
-7    40    2.68
-2    40    2.86
2    40    3.37
7    40    3.91
12    40    4.55
-10    45    2.32
-7    45    2.42
-2    45    2.67
2    45    3.08
7    45    3.50
12    45    4.05
-10    50    2.16
-7    50    2.26
-2    50    2.42
2    50    2.81
7    50    3.15
12    50    3.57
-10    55    1.96
-7    55    2.09
-2    55    2.17
2    55    2.53
7    55    2.85
12    55    3.18


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