# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.5.py
@Time    :   2022/09/18 18:01:08
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''

* Schrijf een programma met invoer het getal x en dat de volgende wiskundige functie berekent:  𝑓(𝑥)=𝑒^|𝑥| 
Hint: In het overzicht van de math module staat ook een functie die van een getal de absolute waarde maakt.
'''

import math


x = float(input("Voer een getal in voor x: "))
output = math.e ** abs(x)
print("e^|x| =", output)

# # Andere alternatief:
# output = math.e ** math.fabs(x)
# print(output)

'''
Uitwerking:

x = float(input('Geef x: '))

print(math.e ** math.fabs(x))
'''
