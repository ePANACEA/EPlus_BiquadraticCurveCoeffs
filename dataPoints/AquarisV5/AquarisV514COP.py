'''
Created on 7 oct. 2018

@author: mapas
'''


# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    COP
ratedCop = 4.85
ratedCop45 = 3.82
listaPuntosStr = """-10    25    3.31
-7    25    3.62
-2    25    4.25
2    25    5.16
7    25    6.36
12    25    8.20
-10    30    3.00
-7    30    3.26
-2    30    3.72
2    30    4.46
7    30    5.51
12    30    6.83
-10    35    2.73
-7    35    2.95
-2    35    3.34
2    35    4.02
7    35    4.85
12    35    5.94
-10    40    2.49
-7    40    2.68
-2    40    3.02
2    40    3.62
7    40    4.30
12    40    5.15
-10    45    2.31
-7    45    2.44
-2    45    2.74
2    45    3.24
7    45    3.82
12    45    4.52
-10    50    2.13
-7    50    2.21
-2    50    2.51
2    50    2.95
7    50    3.41
12    50    4.00
-10    55    2.01
-7    55    2.09
-2    55    2.33
2    55    2.71
7    55    3.09
12    55    3.56


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