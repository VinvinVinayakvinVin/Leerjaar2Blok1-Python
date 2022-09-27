# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.15.py
@Time    :   2022/09/23 22:16:41
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
** Maak het volgende programma:

Invoer: een decimaal getal r.

Uitvoer: de oppervlakte van een cirkel, met straal r en een aantal regels met

            “Hiep hiep hoera!”.  
Werking: de oppervlakte van een cirkel bepalen met straal r en uitprinten. Vervolgens print je x-keer de regel.

            “Hiep hiep hoera!” 
onder elkaar uit. Hierbij is x gelijk aan het cijfer voor de komma (punt) van de oppervlakte van de cirkel.

Vereisten: Voor het bepalen van de oppervlakte én het uitprinten “Hiep hiep hoera!” schrijf je twee aparte functies.
'''

from math import pi


r = int(input("Vul een geheel positief getal in: "))

def opp_berekenen(r):
    """
    Functie opp_berekenen, berekent het oppervlakte van een cirkel.
    Om de functie te roepen, moet je in de 
    """
    return pi * r ** 2

def print_hoera_x_keer(r):
    """
    Functie die x keer "Hiep hiep hoera!" uit print.
    """
    print("Hiep hiep hoera!\n"*r)
    return 

print(opp_berekenen(r))
print_hoera_x_keer(r)

'''
❗ Definitie van parameter en argument ❗

De termen parameter en argument kunnen voor hetzelfde worden gebruikt: informatie die in een functie wordt doorgegeven.

Vanuit het perspectief van een functie:

Een parameter is de variabele die tussen haakjes staat in de functiedefinitie.

Een argument is de waarde die naar de functie wordt gestuurd wanneer deze wordt aangeroepen.
'''


'''
# uitwerking:

# import math 

r = float(input("Voer de straal van de cirkel in:"))

def oppervlakteCirkel(r):
    """Return oppervlakte van cirkel met straal r"""
    
    oppervlakte = (r**2) * math.pi
    
    return oppervlakte

def HiepHiep(x):
    """print 'Hiep hiep hoera!' x keer onder elkaar"""

    print("Hiep hiep hoera!\n"*x, end = '')
    
print(oppervlakteCirkel(r))

HiepHiep(int(oppervlakteCirkel(r))) #Let op: hier gebruiken we geen print, die zit al in de functie 'HiepHiep'.
'''