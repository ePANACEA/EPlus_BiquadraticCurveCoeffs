'''
Created on 7 oct. 2018

@author: mapas
'''

ratedPower = 4.55
ratedPower45 = 4.47
# Lista de puntos de funcionamiento en string copia y pegado de excel
# T entrada aire    T salida agua    Capacidad
listaPuntosStr = """
-10    25    5.56
-7    25    5.46
-2    25    5.03
2    25    4.58
7    25    4.51
12    25    5.05
-10    30    5.5
-7    30    5.37
-2    30    4.93
2    30    4.54
7    30    4.46
12    30    5.02
-10    35    5.41
-7    35    5.37
-2    35    4.94
2    35    4.48
7    35    4.55
12    35    4.98
-10    40    5.42
-7    40    5.4
-2    40    5
2    40    4.44
7    40    4.48
12    40    4.95
-10    45    5.37
-7    45    5.37
-2    45    4.93
2    45    4.56
7    45    4.47
12    45    4.9
-10    50    5.43
-7    50    5.39
-2    50    4.88
2    50    4.55
7    50    4.44
12    50    4.84
-10    55    5.44
-7    55    5.38
-2    55    4.83
2    55    4.53
7    55    4.41
12    55    4.77


"""

listaPuntos = listaPuntosStr.strip().split('\n')
xdata = [float(x.split('    ')[0]) for x in listaPuntos]
ydata = [float(x.split('    ')[1]) for x in listaPuntos]

# Modificador de la capacidad
zdata = [float(x.split('    ')[2]) / ratedPower for x in listaPuntos]
zdata45 = [float(x.split('    ')[2]) / ratedPower45 for x in listaPuntos]