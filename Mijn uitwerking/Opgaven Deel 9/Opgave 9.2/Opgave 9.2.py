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
of juist op strings (lower(), strip(), split(), etc) 
of juist voor openen en lezen van een tekstfile (open(), read(), readlines(), etc) 
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

# sin, cos, isinf, isinfinite functies en pi, inf waarden.
print(math.sin(math.pi))
print(math.cos(math.pi))
print(math.inf)
print(-math.inf)
print(math.isinf(math.inf))
print(math.isfinite(math.pi))

# read, readline, readlines, split functies.
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


# Let op! De strip functie haalt whitespace weg van linker en rechterkant van string!
print("\n\nStrip() gebruiken:")
a_str = "                hoi vin...                      "
print("Originele string:" + "test" + a_str + "test")
newstr = a_str.strip()
print("Nu met strip functie in toepassing:" + "test" + newstr + "test")

print("\n\nStrip() gebruiken, nu met \\t:")
a_str = "\t\t\t\t\t\thoi vin...\t\t\t\t\t"
print("Originele string:" + "test" + a_str + "test")
newstr = a_str.strip("\t")
print("Nu met strip functie in toepassing:" + "test" + newstr + "test")

print("\n\nStrip() gebruiken, nu met \\t en \" \":")
a_str = "\t\t\t\t\t\thoi vin...                    "
print("Originele string:" + "test" + a_str + "test")
newstr = a_str.strip("\t")
print("Nu met strip functie in toepassing:" + "test" + newstr + "test")

print("\n\nStrip() gebruiken, nu met \\t en \" \", hierbij is er wel nog een strip() func geroepen!:")
a_str = "\t\t\t\t\t\thoi vin...                    "
print("Originele string:" + "test" + a_str + "test")
newstr = a_str.strip("\t").strip()
print("Nu met strip functie in toepassing:" + "test" + newstr + "test")

print("\n\nStrip() gebruiken, nu met whitespace in het midden van str.:")
a_str = "\t\t\t\t\t\thoi                                   vin...                    "
print("Originele string:" + "test" + a_str + "test")
newstr = a_str.strip("\t").strip()
print("Nu met strip functie in toepassing:" + "test" + newstr + "test")

# replace functie.
print("\n\nNu over de replace functie!")
a_str = "a b c a e f a i j"
print(a_str + "\n" + a_str.replace("a", "d", 1))


# len functie.
print("\n\nNu over de len functie!")
a_str = "a b c a e f a i j"
print(a_str + "\n" + str(len(a_str)))


# tel characters zonder whitespace.
print("\n\ntel characters zonder whitespace:")
a_str = "a b c a e f a i j"
teller = 0
for i in a_str:
    if i != " ":
        teller += 1
print(a_str + "\n" + str(teller))


# Nu over de lijsten!
print("\n\nlijst functies:")
print("copy() functie:")
lijstje = [1, 2]
print(lijstje)
copy_lijstje = lijstje.copy()
print("kopieer een holle kopie: " + str(copy_lijstje))

print("\n\nlijst2 = lijst1 gebruiken en dan lijst2.append func gebruiken!")
wiccas = ['Vuur', 'Aarde', 'Lucht']
wiccas2 = wiccas
wiccas2.append('Water')
print(wiccas2)
print(wiccas)   # Deze heeft nu ook het element 'Water'.

print("\n\nlijst2 = lijst.copy() en dan lijst2.append func gebruiken!")
wiccas = ['Vuur', 'Aarde', 'Lucht']
wiccas2 = wiccas.copy()
wiccas2.append('Water')
print(wiccas2)
print(wiccas)   # Nu heeft het element 'Water' niet meegenomen.

print("\n\nlijst is 2d lijst, then lijst2 = lijst.copy() en dan lijst2[1][0] element wijzigen.")
wiccas = ['Vuur', ['Aarde', 'Magma'], 'Lucht']
wiccas2 = wiccas.copy()
wiccas2[1][0] = 'Steen'
print(wiccas2)
print(wiccas)   # 'Aarde' is *ook* gewijzigd naar 'Steen'!

print("\n\nlijst is 2d lijst, then lijst2 = lijst.deepcopy() en dan lijst2[1][0] element wijzigen.")
import copy
wiccas = ['Vuur', ['Aarde', 'Magma'], 'Lucht']
wiccas2 = copy.deepcopy(wiccas)
wiccas2[1][0] = 'Steen'
print(wiccas2)
print(wiccas)   # 'Aarde' is hetzelfde hier gebleven.


# lower, upper func.
print("\n\nlower() en upper() func op str gebruiken:")
a_str = "Hallo jongens en meisjes :D"
print("a_str: " + a_str)
print("lower: " + a_str.lower())
print("upper: " + a_str.upper())


#TODO range(), input(), print(), int(), str(), ... etc
