# -*-coding:utf-8 -*-
'''
@File    :   Opgave 8.3.py
@Time    :   2022/11/10 20:53:21
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
3.
*** Snijpunt bepalen

Schrijf een programma dat het snijpunt van de volgende twee functies bepaalt en uitprint. 
De uitvoer is zowel de x-coördinaat als de y-coördinaat. Rond af op drie decimalen nauwkeurig.

𝑓(𝑥)=𝑒^𝑥 
𝑔(𝑥)=𝑙𝑛(𝑥),𝑥>0 
Hint: Gebruik een While-loop. Bedenk dat  𝑓(𝑥)  en  𝑔(𝑥)  bijna aan elkaar gelijk zijn als  𝑓(𝑥)–𝑔(𝑥)  ≈ 0. 
Varieer je x waarde in een while-loop en als  𝑓(𝑥)–𝑔(𝑥)  dan bijna 0 of 0 is ben je er. 
Je moet zelf bepalen wanneer het verschil voldoende bij 0 ligt. 
De while-loop stopt als het verschil klein genoeg is en gaat anders door.
PS: bij Programmeren 3.3. zullen we een betere en veel snellere manier behandelen om snijpunten te bepalen.
'''

import math

def f(x):
    """
    Berekent het functie f en geeft het waarde terug.

    Parameters
    ----------
    x: float type

    Returns
    -------
    e^x: float type
    """

    return math.e ** (-x)


def g(x):
    """
    Berekent het functie g en geeft het waarde terug.

    Parameters
    ----------
    x > 0: float type

    Returns
    -------
    ln(x): float type
    """

    return math.log(x, math.e)

x = 0.01
fx = f(x)
gx = g(x)
delta = 1
print(f(x), g(x))

while delta > 0.00001:
    delta = abs(round((fx - gx), 3))
    x += 0.000001
    fx = f(x)
    gx = g(x)

print(fx, gx)
# print(f"Snijpunt ligt op het punt van: ({x}, {fx})")
print(f"Snijpunt ligt op het punt van: ({round(x, 3)}, {round(fx, 3)})")
# print(f"Snijpunt ligt op het punt van: {x, fx}")      # Zo kan je ook schrijven, dit geeft automatisch die haakjes om de x en fx.



# Uitwerking:
'''
import math

delta = 1.0
x = 0.01

# In de while-loop halen we gx van fx (voor verschillende x-waarden) en dat verschil noemen we delta.  
# Als delta bijna 0 is, dan zijn fx en gx dus bijna aan elkaar gelijk en hebben we het snijpunt gevonden.
# We moeten afronden op vier decimalen, dus als delta kleiner is dan 0.00001, wordt aan die nauwkeurigheid voldaan. 0.00000001 kan
# bijv. ook, dat is nog nauwkeuriger, maar dan moet je langer rekenen en die nauwkeurigheid wordt niet gevraagd, dus doen we dat niet.
# Startwaarde van delta moet groter zijn dan 0.00001, anders stopt de while-loop direct en dat moet niet. Ik kies hier delta = 1.0.

while delta > 0.00001:
    fx = math.e**(-x)
    gx = math.log(x)
    
    delta = abs(fx - gx)
    
    x = x + 0.000001
    
y = math.e**(-x)

print(f'Snijpunt: ({round(x, 3)}, {round(y, 3)})') #derde decimaal getal is 0 en wordt niet geprint



# Output:
# Snijpunt: (1.31, 0.27)
'''