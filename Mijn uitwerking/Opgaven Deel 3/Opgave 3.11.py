# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.11.py
@Time    :   2022/09/23 21:20:56
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
!! ** Schrijf een programma met invoer een getal x en dat de volgende wiskundige functie berekent én het antwoord afrond op drie decimalen:
𝑓(𝑥)=πe^(-2|x|)
'''

from math import *


x = float(input("Vul een getal in: "))
calculate = round(pi*e**(-2*abs(x)), 3)     # let op, abs geeft het absolute waarde voor x in datatype float🟡, omdat x een float type🟡 is.
print(calculate)

# x = float(input('Geef x: '))
# fx = pi * e ** (-2 * fabs(x))
# print(round(fx, 3))
# print(f"{fx:.3f}")

# FABS VS ABS! ❗❗❗❗❗❗❗❗❗❗👓
# fabs(number) will always return a floating-point number even if the argument is an integer, 
# whereas abs() will return a floating-point or an integer depending upon the argument.

# x = 3.999899999999
# print(f"{x:.6f}")     # Testen hoe die :.2f werkt. (Het rondt af op 2 decimalen).

'''
Uitwerking:

import math

x = float(input('Geef x: '))

fx = math.pi * (math.e ** (-2 * math.fabs(x)))

print(round(fx, 3)) #round(fx, 3) rond fx af op 3 decimalen

# Alternatief:
print(f"{fx:.3f}") 

# output:
# Geef x: 1
# 0.425
# 0.425
'''