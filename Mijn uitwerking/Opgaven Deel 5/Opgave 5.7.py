# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.7.py
@Time    :   2022/10/21 10:08:12
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
7.¶
* Doe opgave 4 nogmaals, maar nu met een kortere code door een for-loop te gebruiken.
'''

# Onderdeel a!
#Lege lijst

getallen = []

# Dit loopt 5 keer, waarbij je 5 keer getal invult en dat in de lijst zet van 'getallen'.
for i in range(0, 5):   # Kon ook range(5) nemen, i.p.v range(0, 5).
    getal = float(input("Vul een getal in: "))
    getallen.append(getal)

#De lijst 'namen' printen
print(getallen)


# Onderdeel b!
import random

getallen = []

# Dit loopt 3 keer, waarbij er 3 random gehele getallen worden genomen tussen 0 en 9 (inclusief grenzen).
for i in range(0, 3):
    getal = random.randint(0, 9)
    getallen.append(getal)

print(getallen)


'''
# Uitwerking a & b:


#a
getallen = []

for x in range(5):
    getal = float(input('Vul een getal in\n'))
    getallen.append(getal)

print(getallen)


#b
import random

willekeur = []

for x in range(3):
    getal = random.randint(0, 9)
    willekeur.append(getal)

print(willekeur)
'''