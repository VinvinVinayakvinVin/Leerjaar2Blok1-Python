# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.16.py
@Time    :   2022/10/19 19:22:46
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
4.16¶
** Schrijf een programma met drie gehele getallen als invoervariabelen
en waarvan de output False is als een van de variabelen gelijk of 
groter is dan de som van de twee andere variabelen, anders is de output True.

PS: Dit programma bepaalt of de drie getallen de lengte zouden kunnen zijn van de zijden van een driehoek! Ben je het hiermee eens?
'''

a = int(input("Vul geheel getal voor a: "))
b = int(input("Vul geheel getal voor b: "))
c = int(input("Vul geheel getal voor c: "))

var1 = a >= b + c
var2 = b >= a + c
var3 = c >= a + b

print(not (var1 or var2 or var3))

# Bekijk ook deze websites:
# https://www.mathwarehouse.com/geometry/triangles/
# https://tutorme.com/blog/post/triangle-rules/

# Denk ook als je bijv: een zijde 4 neemt, 5 en 12, dat die driehoek niet bestaat.

'''
# Uitwerking

a = int(input('Geef a: '))
b = int(input('Geef b: '))
c = int(input('Geef c: '))

if a >= b + c or b >= a + c or c >= a + b:
    print(False)
else:
    print(True)
'''