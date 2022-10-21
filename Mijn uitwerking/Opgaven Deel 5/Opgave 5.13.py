# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.13.py
@Time    :   2022/10/21 12:09:36
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
13.¶
!! *** Lijst aanpassen

Schrijf een programma met daarin:

Een functie die een lijst aanmaakt met n-elementen.
Elk element is een geheel getal met een waarde tussen de 1 en 10 (10 doet mee).
De functie retourneert de lijst als output.

Een functie die als invoer een lijst heeft en dan de elementen van die lijst aanpast:
elk element wordt gekwadrateerd. De functie retourneert deze veranderde lijst.
Hint: Je weet niet precies hoe groot de lijst is, terwijl de range() statement dat wel moet weten.
Gebruik dus de len() statement. Vergeten wat len() doet met een lijst?
Check internet! Zoektermen len() en list.

Je programma heeft als input het getal n en print de twee lijsten uit.
'''

# ⬇️ Eerste poging!

# import random


# def random_lijst_generator():
#     """
#     Dit genereert een willekeurige lijst.
#     Het aantal elementen in de lijst is random (willekeurig), het kan 1 tot 20 elementen bevatten.
#     Verder heeft elk element een willekeurige waarde tussen 1 en 10.
#     """
#     random_lijst = []
#     for i in range(random.randint(1, 20)):
#         random_lijst.append(random.randint(1, 10))
#     return random_lijst

# def lijst_aanpassen(random_lijst):
#     """
#     Dit verandert de waardes van binnen de lijst.
#     Vervolgens wordt elk waarde gekwadrateerd.
#     """
#     for i in range(len(random_lijst)):
#         random_lijst[i] = int(input("Vul een geheel getal in die tussen 1 en 10 ligt: "))
#         random_lijst[i] = random_lijst[i] ** 2
#     return random_lijst


# random_lijst = random_lijst_generator()
# # print(random_lijst)
# # print(len(random_lijst))
# # print(len(set(random_lijst)))
# print("Het lijst dat genereert is: ", random_lijst)
# print("Het aangepaste lijstje: " + str(lijst_aanpassen(random_lijst)))


'''
# Uitwerking:

import random

def lijstmaker(n):
    """
    Maakt een lijst van n random elementen met een waarde tussen [1, 10]
    
    Parameters
    ----------
    n: float
       de lengte van de lijst 
       
    Returns
    -------
    lijst
    
    """
    lijst = []
    
    for i in range(n):
        lijst.append(random.randint(1, 10))
    
    return lijst

def lijstaanpassen(lijst):
    """
    Kwadrateert elk element van een lijst
    
    Parameters
    ----------
    lijst: list
           de lijst om te kwadrateren
       
    Returns
    -------
    list
        een lijst met elk element gekwadrateert
    
    """
    kwadraten = []
    
    n = len(lijst)
    
    for i in range(n):
        kwadraten.append(lijst[i] * lijst[i])
        
    return kwadraten

n = int(input('Vul een geheel getal in\n'))

lijst = lijstmaker(n)
nwe_lijst = lijstaanpassen(lijst)

print(lijst)
print(nwe_lijst)


# # Output:

# Vul een geheel getal in
# 6
# [3, 3, 9, 5, 2, 5]
# [9, 9, 81, 25, 4, 25]
'''

# Ik heb het te ingewikkeld begrepen.
# Ik kon gewoon die random.randint(...) vervangen met variabele n die als input is.

# ⬇️ Tweede poging!

import random

def lijst_maken(n):
    """
    Maakt een lijst met getallen die tussen [1, 10] ligt.

    Parameters
    ----------
    n: integer
        De lengte van de lijst.

    Returns
    ------
    lijst
    """

    lijst = []

    for i in range(n):
        lijst.append(random.randint(1,9))

    return lijst

def lijst_aanpassen(lijst):
    """
    Hier wordt de lijst aangepast door user input,
    waarbij de user een geheel getal tussen 1 en 10 typt voor elk element in de lijst.

    Parameters
    ---------
    lijst: array
        Lijst die bevat willekeurige waardes per element.

    Returns
    -------
    nieuwe_lijst
    """

    n = len(lijst)

    for i in range(n):
        lijst[i] = int(input("Vul een geheel getal in die tussen 1 en 10 ligt: "))
        lijst[i] = pow(lijst[i], 2)
    return lijst

n = int(input("Vul een geheel getal in: "))

lijst = lijst_maken(n)
print(lijst)

nieuwe_lijst = lijst_aanpassen(lijst)
print(nieuwe_lijst)