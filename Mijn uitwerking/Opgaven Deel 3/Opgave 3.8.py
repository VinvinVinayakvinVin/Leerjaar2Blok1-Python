# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.8.py
@Time    :   2022/09/23 18:04:41
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
!! ** Schrijf een programma dat het getal 56,657 afrondt op een geheel getal. Doe dit op twee manieren.

Eén manier is met een functie die je al kent (conversiefunctie), de andere manier ken je nog niet.

Gebruik internet en probeer een standaard afrondingsfunctie te vinden voor Python. Wat is het verschil tussen beide uitkomsten?
'''

from math import ceil, floor        # Je kan op verschillende manieren de onderdelen van de modules importeren.
# from math import *                # Door een sterretje (asterik) te zetten na het keyword "import", dan importeer je alles van een bepaald module.

# Conversion method
print(int(56.657))      # dit rondt af op hele getal, maar het rond naar beneden, ook al is eerste decimaal boven de nummer 5.

# Deze website ⬇️ laat zien hoe je op verschillende manieren kan afronden.
# https://realpython.com/python-rounding/#:~:text=To%20implement%20the%20%E2%80%9Crounding%20up,equal%20to%20a%20given%20number.

# Info over ceil function:
# To implement the “rounding up” strategy in Python, we’ll use the ceil() function from the math module.
# The ceil() function gets its name from the term “ceiling,” 
# which is used in mathematics to describe the ‼️ nearest integer ‼️ that is greater than or equal to a given number.

print(ceil(56.657))     # Dit rondt naar boven af.
# print(floor(56.657))  # Dit rondt juist naar beneden af.

print(round(56.657))

'''
# Uitwerking gebruikt het functie round().
# Uitwerkings code ⬇️

getal = 56.657

print(int(getal)) #int() rond af naar beneden

print(round(getal)) #round() rond af naar dichtsbijzijnde integer
'''