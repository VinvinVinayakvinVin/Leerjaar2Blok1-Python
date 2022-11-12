# -*-coding:utf-8 -*-
'''
@File    :   Opgave 9.2.py
@Time    :   2022/11/11 17:44:21
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
Overzicht¶
2.
Tot nu toe heb je veel functies en technieken voorbij zien komen. 
Stap voor stap, beetje bij beetje. Nadeel is dat je nu misschien wat overzicht mist. Dat kun je oplossen:

!! * a. Schrijf alle functies die je tot nu toe hebt gezien of gebruikt op in een overzicht 
(op je computer of met pen en papier of hier in een cell van Jupyter). 
Probeer te ordenen, dus alle functies uit de math module bij elkaar (sin(), pow(), pi etc.), 
alle functies die te maken hebben met of bewerkingen doen op lijstjes (append(), copy(), range(), etc) 
of juist op strings (lower(), strip(), split(), etc) of juist voor openen en lezen van een tekstfile (open(), read(), readlines(), etc) 
en overige functies (print(), input(), etc).

Schrijf op wat de functies doen en wat de in- en uitvoer van de functies is. 
Bij sommige functies heb je meerdere opties tot invoer, bijv de range functie:

range(5) maakt lijst aan [0, 1, 2, 3, 4]
range(3, 8) maakt lijst aan [3, 4, 5, 6, 7].

Zelfde functie, maar andere invoer.

Of de print() die kan meerdere input hebben, niet slechts één:

print(‘Hello, World!’)* print(‘Hello’, ‘World’, ‘!’)
print(‘Hello, World!’, end = ‘’)

!! * b. Gegeven de operatoren + * - / % //.
Wat doen deze operatoren (op verschillende datatypes (integer, string) en objecten (lists))?
'''

import math
import os
import random


print(math.sin(math.pi))
print(math.cos(math.pi))
print(math.inf)
print(-math.inf)
print(math.isinf(math.inf))
print(math.isfinite(math.pi))

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 9\\Opgave 9.2\\")
print("\n\nNu read() functie gebruiken op het bestand van \"quotes.txt\".")
file = open("quotes.txt")
print(file.read())
file.close()

print("\n\nNu read().split() functie gebruiken op het bestand van \"quotes.txt\".")
file = open("quotes.txt")
print(file.read().split())
file.close()

print("\n\nNu readlines() functie gebruiken op het bestand van \"quotes.txt\".")
file = open("quotes.txt")
print(file.readlines())
file.close()

print("\n\nNu readline() functie gebruiken op het bestand van \"quotes.txt\".")
file = open("quotes.txt")
print(file.readline())
file.close()

print("\n\nNu readlines()[0] functie gebruiken op het bestand van \"quotes.txt\".")
file = open("quotes.txt")
print(file.readlines()[0])
file.close()

print("\n\nNu readlines()[0].split() functie gebruiken op het bestand van \"quotes.txt\".")
file = open("quotes.txt")
print(file.readlines()[0].split())
file.close()

print("\n\nNu readline()[0] functie gebruiken op het bestand van \"quotes.txt\".")
file = open("quotes.txt")
print(file.readline()[0])
file.close()

print("Strip() gebruiken:")
str = "                hoi vin...                      "
print("Originele string:", str)
newstr = str.strip()
print("Nu met strip functie in toepassing:", newstr)

