# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.6.py
@Time    :   2022/09/27 21:05:45
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* Maak een functie die twee getallen als parameters heeft, a en b. De uitvoer is a/b, maar altijd naar beneden afgerond.
Test je functie ook of die werkt. Probeer een geschikte naam voor je functie te bedenken.

Hint: floor division // gebruiken.
'''

from math import floor


a =  float(input("Vul een getal in voor a: "))
b =  float(input("Vul een getal in voor b: "))

def floor_division(a, b):
    """Print uit a delen door b en print ook uit a delen door b en naar beneden afgerond."""
    print("a / b:", a / b)
    print("a // b: " + str(a // b))
    print(floor(a/b))
    return

floor_division(a, b)

# vb)
# a = 10
# b = 3
# a / b = 10 / 3 = 3.3333333333333335
# a // b = 10 // 3 = 3.0

# Ik kon ook 'print(math.floor(a/b))' doen. (nvm, zie lijn 27).

'''
# Uitwerking:

# import math

#2 getallen als testinput
x = 10
y = 3

def myFloorFunction(a, b):
    print(a//b) #naar beneden afronden doe je met //
    
myFloorFunction(x, y) # Testen

#Er is ook een "floor functie in de math module"
#Als "math" niet herkend word, moet je het nog importeren. Dit is nu achterwege gelaten 
#omdat math al wordt ingeladen bij opgave 5.5
print(math.floor(x/y))


# Output:

# 3
# 3
'''