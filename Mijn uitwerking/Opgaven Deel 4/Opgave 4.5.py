# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.5.py
@Time    :   2022/09/27 20:38:26
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
** Absolute waarde

a. Schrijf een programma met invoer een getal en als uitvoer de absolute waarde van dit getal. 
Gebruik de math module.

b. Zie a, maar gebruik de math module nu niet, maak zelf een programma dat de absolute waarde van een getal bepaalt.
Hint: iets met een if-statement.

c. Zie b, maar schrijf nu geen programma, 
maar een functie die hetzelfde doet (dus van een getal de absolute waarde maken) en noem die functie bijvoorbeeld absoluut.
'''

'''
# Uitwerking:

#Omdat we de math module gaan gebruiken, moeten we die eerst inladen
#Als je modules gaat gebruiken, importeer die altijd helemaal bovenaan je code
import math

#Geef een getal als invoer
getal = float(input('Vul een getal in: '))

#a
#fabs is de functie uit de math module dat de absolute waarde bepaald
print('De absolute waarde met fabs functie ' + str(math.fabs(getal))) 

#b
#zonder functie kunnen we met een if-statement controleren of het getal kleiner is dan 0
#als getal < 0 True is, print dan -getal uit.
if getal < 0:
    getal = -getal

print('De absolute waarde met if-statement '+ str(getal))
    
#c
#gebruik de methode van b in jouw zelfgemaakte functie
def absoluut(x):
    if x < 0:
        x = -x
    print('De absolute waarde met absoluut functie ' + str(x)) 
    
absoluut(getal)


# Output:

# Vul een getal in: -6
# De absolute waarde met fabs functie 6.0
# De absolute waarde met if-statement 6.0
# De absolute waarde met absoluut functie 6.0
'''