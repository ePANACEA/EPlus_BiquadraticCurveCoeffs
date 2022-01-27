'''
Created on 7 oct. 2018

@author: mapas
'''


# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    COP
ratedCop = 4.32
ratedCop45 = 3.44
listaPuntosStr = """-10    25    3.25
-7    25    3.47
-2    25    3.92
2    25    4.66
7    25    5.63
12    25    7.12
-10    30    2.91
-7    30    3.15
-2    30    3.48
2    30    4.17
7    30    4.95
12    30    5.99
-10    35    2.70
-7    35    2.85
-2    35    3.16
2    35    3.71
7    35    4.32
12    35    5.15
-10    40    2.44
-7    40    2.61
-2    40    2.77
2    40    3.33
7    40    3.87
12    40    4.48
-10    45    2.27
-7    45    2.39
-2    45    2.61
2    45    3.02
7    45    3.44
12    45    3.94
-10    50    2.11
-7    50    2.21
-2    50    2.36
2    50    2.75
7    50    3.11
12    50    3.48
-10    55    1.96
-7    55    2.04
-2    55    2.19
2    55    2.49
7    55    2.78
12    55    3.14

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