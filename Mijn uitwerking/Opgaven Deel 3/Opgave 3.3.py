# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.3.py
@Time    :   2022/09/18 09:28:21
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* Schrijf een programma dat als invoer een decimaal getal x heeft en als uitvoer de waarde van 𝑠𝑖𝑛(𝑥)^2+𝑐𝑜𝑠(𝑥)^2 geeft. 
Test met een paar x-waarden (0; 1; 100). Waarom komt hier niet altijd precies 1 uit denk je?
'''

import math


x = float(input("Type een decimaal getal in voor x: "))
# x = math.pi
uitvoer = math.sin(x)**2+math.cos(x)**2
print(f"sin(x)^2+cos(x)^2 = {uitvoer}")
# print("sin(x)^2+cos(x)^2 = " + str(uitvoer))
# print("sin(x)^2+cos(x)^2 =", uitvoer)

# Als je 100 invult, dan krijg je geen 1.0, maar 0.9999999999999999

# print(math.sin(100), math.sin(100)**2, math.cos(100), math.cos(100)**2)
# ⬆️ Dit print uit:
# -0.5063656411097588 
# 0.25640616249649706 
# 0.8623188722876839 
# 0.7435938375035028
# 0.25640616249649706 + 0.7435938375035028 = 0.99999999999999986 ongeveer 1.0