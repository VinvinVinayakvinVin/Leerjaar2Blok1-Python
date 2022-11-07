# -*-coding:utf-8 -*-
'''
@File    :   Opgave 7.5.c.py
@Time    :   2022/11/07 11:13:57
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
*** c. Zie b, alleen nu print je de acht lijstjes niet meer uit, maar print je het gemiddelde van beide geslachten uit van 
leeftijd, lengte, gewicht en cijfer en ook hoeveel jongens en meisjes er zijn. 
Laat de gebruiker duidelijk zien welke gemiddeldes het zijn en van welk geslacht. 
Schrijf hiervoor ook een functie gemiddelde, dat het gemiddelde van een lijst uitrekent.
'''

import os


os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.5.c\\")
file = open("Klas.txt")
file.readline()     # skip de eerste lijn, waarbij er kopjes staan.

# j voor jongens
jleeftijden = []
jlengtes = []
jgewichten = []
jcijfers = []
jgem = 0

# m voor meisjes
mleeftijden = []
mlengtes = []
mgewichten = []
mcijfers = []
mgem = 0

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

aantalj = 0    # aantal jongens
aantalm = 0    # aantal meisjes
lines = file.readlines()    # note: file.readlines() heeft het vorm als -> ['zin_1', 'zin_2', ..., 'zin_n']
for line in lines:
    leeftijd = float(line.split()[2])
    lengte = float(line.split()[3])
    gewicht = float(line.split()[4])
    cijfer = float(line.split()[5])

    if line.split()[1] == "jongen":
        aantalj += 1
        jleeftijden.append(leeftijd)
        jlengtes.append(lengte)
        jgewichten.append(gewicht)
        jcijfers.append(cijfer)
    else:
        aantalm += 1
        mleeftijden.append(leeftijd)
        mlengtes.append(lengte)
        mgewichten.append(gewicht)
        mcijfers.append(cijfer)

# print("Er zijn totaal " + str(aantalj) + " jongens in het klas.")
# print("Het gemiddelde van de jongens van leeftijden is: " + str(gemiddelde(jleeftijden)))
# print("Het gemiddelde van de jongens van lengtes is: " + str(gemiddelde(jlengtes)))
# print("Het gemiddelde van de jongens van gewichten is: " + str(gemiddelde(jgewichten)))
# print("Het gemiddelde van de jongens van cijfers is: " + str(gemiddelde(jcijfers)))
# print()
# print("Er zijn totaal " + str(aantalm) + " meisjes in het klas.")
# print("Het gemiddelde van de meisjes van leeftijden is: " + str(gemiddelde(mleeftijden)))
# print("Het gemiddelde van de meisjes van lengtes is: " + str(gemiddelde(mlengtes)))
# print("Het gemiddelde van de meisjes van gewichten is: " + str(gemiddelde(mgewichten)))
# print("Het gemiddelde van de meisjes van cijfers is: " + str(gemiddelde(mcijfers)))

print(f"""Het aantal jongens is: {aantalj}.
Het gemiddelde leeftijd van de jongens is: {gemiddelde(jleeftijden)}.
Het gemiddelde lengte van de jongens is: {gemiddelde(jlengtes)}.
Het gemiddelde gewicht van de jongens is: {gemiddelde(jgewichten)}.
Het gemiddelde cijfer van de jongens is: {gemiddelde(jcijfers)}.
""")
print(f"""Het aantal meisjes is: {aantalm}.
Het gemiddelde leeftijd van de meisjes is: {gemiddelde(mleeftijden)}.
Het gemiddelde lengte van de meisjes is: {gemiddelde(mlengtes)}.
Het gemiddelde gewicht van de meisjes is: {gemiddelde(mgewichten)}.
Het gemiddelde cijfer van de meisjes is: {gemiddelde(mcijfers)}.
""")

file.close()