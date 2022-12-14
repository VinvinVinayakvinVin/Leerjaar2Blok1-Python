# -*-coding:utf-8 -*-
'''
@File    :   Opgave 6.11.py
@Time    :   2022/10/22 10:49:13
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
11.ΒΆ
*** Nested for-loops III. Volume onder een oppervlak (LASTIG)

Je gaat een programma schrijven dat het volume bepaalt tussen het xy-vlak, 
een oppervlak beschreven door  π(π₯,π¦)=π₯4π¦2  op het rechthoekige domein  2β€π₯β€4  en  2β€π¦β€6 .
'''

# Zie plaatjes in jupyter notebook, kan handig zijn om een beeld te krijgen wat er gedaan moet worden.

'''
Het programma moet dus het volume van het zalmroze object bepalen. 
Dit doen we door een zogenaamde dubbele Riemannsom te berekenen. 
We delen het object op in heel veel rechte staafjes. 
Het volume van al die staafjes is bij benadering het volume van het object. 
Het volume van een staafje is makkelijk te berekenen:

Volume_staafje = hoogte x breedte x diepte.
'''

'''
Het programma heeft 2 input variabelen:

β’ n: het aantal balkjes op de x-as
β’ m: het aantal balkjes op de y-as

Met het gegeven domein en de input n en m, kun je het programma zelf de breedte en diepte laten bepalen van een balkje. De hoogte van elk van de balkjes varieert:  π(π₯π,π¦π)  met:

β’  π₯π=π₯0+πβπππππ‘π=2+πβπππππ‘π 
β’  π¦π=π¦0+πβππππππ‘π=2+πβππππππ‘π

Het eerste balkje (helemaal linksachter in het plaatje) staat dan 
bij de coΓΆrdinaten  π₯0  en  π¦0  ( π=0  en  π=0 ). Door  π  te variΓ«ren tussen 0 en ( πβ1 ) en  π  te 
variΓ«ren tussen 0 en ( πβ1 ) krijgen we  πβπ  balkjes. Bepaal van al die balkjes het volume en tel op. 
Dat is dan de benadering van het volume dat we zoeken.

Schrijf dit programma.

De βexacteβ waarde van het volume is overigens ongeveer 13.755,7333. Je kunt hiermee je benadering controleren.
'''

n = int(input("Het aantal balkjes op de x-as: "))
m = int(input("Het aantal balkjes op de y-as: "))

x_i = []
y_j = []

diepte = (4 - 2) / n
breedte = (6 - 2) / m

temp_list = []
f_xy = []
volume = 0

# Alle x'tjes verzamelen
for i in range(0, n):
    x_i.append(2 + i * diepte)

# Alle y'tjes verzamelen
for j in range(0, m):
    y_j.append(2 + j * breedte)

# Alle f(x_i, y_j) berekenen en opslaan in een lijst voor later gebruik.
for i in range(0, n):
    for j in range(0, m):

        temp_list.append(pow(x_i[i], 4) * pow(y_j[j], 2))
        if j == (m - 1):
            f_xy.append(temp_list)
            temp_list = []


# Het volume benaderen
for i in range(0, n):
    for j in range(0, m):
        volume += (f_xy[i][j] * breedte * diepte)

print(volume)

# print(x_i)
# print(y_j)
# print(f_xy)



# Uitwerking β¬οΈ
'''
import math

n = int(input('Hoeveel balkjes op de x-as?\n'))
m = int(input('Hoeveel balkjes op de y-as?\n'))

diepte = (4 - 2)/n #de lengte van het grondvlak balkje op de x-as. x loopt van 2 t/m 4 en wordt verdeeld in n intervallen
breedte = (6 - 2)/m #de lengte van het grondvlak op de y-as. y loopt van 2 t/m 6 en wordt verdeeld in m intervallen

def vol_balk(x, y, diepte, breedte):   
    """
    Berekent het volume van 1 balkje.

    Parameters
    ----------
    x, y: float
        De x en y coordinaten. Hiermee wordt de hoogte van een balkje berekend: f(x, y)
        
    diepte, breedte: float
        De lengte en breedte van het grondvlak van de balk.

    Returns
    -------
    float
        Het volume van 1 balkje
    """
    
    f_xy = math.pow(x, 4)*math.pow(y, 2)
    
    return diepte * breedte * f_xy

vol = 0

#ga alle balkjes langs
for i in range(n):
    for j in range(m):
        x = 2 + diepte * i
        y = 2 + breedte * j
        vol = vol + vol_balk(x, y, diepte, breedte)

print(vol) 



# # Output:

# Hoeveel balkjes op de x-as?
# 75
# Hoeveel balkjes op de y-as?
# 100
# 13410.058732238247
'''