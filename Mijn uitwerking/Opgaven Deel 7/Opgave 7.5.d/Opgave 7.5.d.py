# -*-coding:utf-8 -*-
'''
@File    :   Opgave 7.5.d.py
@Time    :   2022/11/07 11:49:09
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
*** d. Bepaal nu het gemiddelde cijfer van de hele klas en de bijbehorende standaarddeviatie.
(De formule hiervan moet je misschien weer even opzoeken in je statistiek boek).
'''

import os
import math


os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.5.c\\")
file = open("Klas.txt")
file.readline()     # skip de eerste lijn, waarbij er kopjes staan.

leeftijden = []
lengtes = []
gewichten = []
cijfers = []
gem = 0
stdev = 0

def gemiddelde(lijst):
    """
    Berekent het gemiddelde van een lijst getallen.

    Parameters
    ----------
    lijst: array type (elementen moeten getallen zijn)!

    Returns
    -------
    gemiddelde: float type
    """
    som = 0
    for element in lijst:
        som += element

    gemiddelde = som / len(lijst)

    return gemiddelde

def stdev(lijst):
    """
    Dit berekent het standaarddeviatie van het lijst (populatie).

    Parameters
    ----------
    lijst: array type (elementen moeten getallen zijn)!
    gem: gemiddelde van het lijst.

    Returns
    -------
    stdev: float type
    """

    gem = gemiddelde(lijst)
    som = 0
    for element in lijst:
        som += math.pow((element - gem), 2)

    stdev = math.sqrt(som / len(lijst))

    return stdev

aantalm = 0     # aantalm -> aantal mensen
lines = file.readlines()    # note: file.readlines() heeft het vorm als -> ['zin_1', 'zin_2', ..., 'zin_n']
for line in lines:
    leeftijd = float(line.split()[2])
    lengte = float(line.split()[3])
    gewicht = float(line.split()[4])
    cijfer = float(line.split()[5])

    aantalm += 1
    leeftijden.append(leeftijd)
    lengtes.append(lengte)
    gewichten.append(gewicht)
    cijfers.append(cijfer)

# print(f"""Het aantal mensen in de klas is: {aantalm}.
# Het gemiddelde leeftijd van de mensen is: {gemiddelde(leeftijden)}.
# Het gemiddelde lengte van de mensen is: {gemiddelde(lengtes)}.
# Het gemiddelde gewicht van de mensen is: {gemiddelde(gewichten)}.
# Het gemiddelde cijfer van de mensen is: {gemiddelde(cijfers)}.
# Het standaarddeviatie leeftijd van de mensen is: {stdev(leeftijden)}.
# Het standaarddeviatie lengte van de mensen is: {stdev(lengtes)}.
# Het standaarddeviatie gewicht van de mensen is: {stdev(gewichten)}.
# Het standaarddeviatie cijfer van de mensen is: {stdev(cijfers)}.
# """)

print(f"""Het aantal mensen in de klas is: {aantalm}.
Het gemiddelde cijfer van de mensen is: {gemiddelde(cijfers)}.
Het standaarddeviatie cijfer van de mensen is: {stdev(cijfers)}.
""")

file.close()