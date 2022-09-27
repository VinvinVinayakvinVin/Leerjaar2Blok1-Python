# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.5.a.py
@Time    :   2022/09/27 20:40:25
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
Zie opgavens in de comment van Opgaven 4.5.py, of zie hieronder:
'''

'''
a. Schrijf een programma met invoer een getal en als uitvoer de absolute waarde van dit getal. 
Gebruik de math module.
'''

from math import *


x = int(input("Type een getal in: "))

print(fabs(x))      # let op, fabs returnt een float type.
print(abs(x))       # Doet hetzelfde, maar retourneert zelfde datatype hoe je de argument ingevuld hebt. (dit retourneert in int type).