# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.14.py
@Time    :   2022/09/23 22:07:49
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* Maak een functie die de oppervlakte van een cirkel bepaald. 
De invoer is een decimaal getal, de straal r. 
Test je functie en controleer.
'''

from math import pi


def cirkel_oppervlakte(r):
    """Berekent het oppervlakte van een cirkel met een radius van r (float datatype)"""
    return pi*r**2

r = float(input("Vul een getal in voor straal: "))
print(cirkel_oppervlakte(r))

'''
# Uitwerking:

# import math

straal = 2.456

def oppervlakteCirkel(r):
    """Return oppervlakte van cirkel met straal r"""
    
    oppervlakte = (r**2) * math.pi
    
    return oppervlakte #geef aan welke waarde de functie moet retouneren wanneer je het aanroept

# Testen:
oppervlakte = oppervlakteCirkel(straal) #roep de functie aan met als input 'straal'

print(oppervlakte)


# output:
18.949885824523804
'''


# ⬇️ Even code van uitwerking uittesten.

# import math

# straal = 2.456

# def oppervlakteCirkel(r):
#     """Return oppervlakte van cirkel met straal r"""

#     oppervlakte = (r**2) * math.pi

#     return oppervlakte #geef aan welke waarde de functie moet retouneren wanneer je het aanroept

# # Testen:

# oppervlakte = oppervlakteCirkel(straal) #roep de functie aan met als input 'straal'

# print(oppervlakte)