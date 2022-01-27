'''
Created on 7 oct. 2018

@author: mapas
'''


# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    COP
ratedCop = 4.78
ratedCop45 = 3.82
listaPuntosStr = """-10    25    3.26
-7    25    3.57
-2    25    4.13
2    25    5.11
7    25    6.37
12    25    8.39
-10    30    2.97
-7    30    3.20
-2    30    3.68
2    30    4.50
7    30    5.50
12    30    6.84
-10    35    2.68
-7    35    2.85
-2    35    3.27
2    35    4.00
7    35    4.78
12    35    5.95
-10    40    2.45
-7    40    2.63
-2    40    2.98
2    40    3.58
7    40    4.24
12    40    5.10
-10    45    2.28
-7    45    2.43
-2    45    2.69
2    45    3.20
7    45    3.82
12    45    4.38
-10    50    2.10
-7    50    2.23
-2    50    2.47
2    50    2.92
7    50    3.37
12    50    3.94
-10    55    1.96
-7    55    2.06
-2    55    2.25
2    55    2.64
7    55    3.01
12    55    3.42

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