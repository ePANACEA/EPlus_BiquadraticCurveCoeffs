'''
Created on 7 oct. 2018

@author: mapas
'''


# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    COP
ratedCop = 4.43
ratedCop45 = 3.48
listaPuntosStr = """-10    25    3.30
-7    25    3.54
-2    25    3.99
2    25    4.85
7    25    5.84
12    25    7.12
-10    30    3.03
-7    30    3.18
-2    30    3.58
2    30    4.29
7    30    5.04
12    30    6.04
-10    35    2.75
-7    35    2.90
-2    35    3.19
2    35    3.78
7    35    4.43
12    35    5.14
-10    40    2.50
-7    40    2.63
-2    40    2.89
2    40    3.41
7    40    3.89
12    40    4.45
-10    45    2.31
-7    45    2.44
-2    45    2.61
2    45    3.03
7    45    3.48
12    45    3.90
-10    50    2.13
-7    50    2.23
-2    50    2.37
2    50    2.75
7    50    3.09
12    50    3.47
-10    55    2.00
-7    55    2.06
-2    55    2.18
2    55    2.48
7    55    2.78
12    55    3.09



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