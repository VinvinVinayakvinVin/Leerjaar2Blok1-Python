# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.16.py
@Time    :   2022/10/21 20:39:07
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
16.¶
!! *** Minimum en maximum

a. Maak een programma met daarin:

1. Een zelfgeschreven functie met invoer een geheel getal n. 
De functie heeft als uitvoer een lijst met daarin n willekeurige getallen tussen de [0, 100).

Hint: De random module en append().

2. Een zelfgeschreven functie met invoer een lijst en die als uitvoer het minimum geeft van die lijst. 
Hint: zoek op internet (of in Python) een waarde die plus oneindig representeert, 
zoals math.pi bijvoorbeeld de waarde van pi representeert.

3. Het programma print de n getallen van de gemaakte lijst uit en geeft daarna aan wat het minimum is van die getallen. 
Hiervoor maak je gebruik van de twee geschreven functies.

b. Zoals a, maar nu maximum.
'''

import math
import random


n = int(input("Vul een positief geheel getal in voor n: "))

def lijstmaker(n):
    """
    Dit maakt een lijst met n aantal elementen,
    waarbij de elementen een willekeurige waarde heeft tussen [0, 100).

    Parameters
    ----------
    n: integer
        Wordt gebruikt voor hoeveel elementen er in de lijst komt.
    
    Returns
    -------
    lijst: array
    """

    lijst = []

    for i in range(n):
        # lijst.append(random.randint(0, 99))   # Met dit, zullen de elementen integer type zijn.
        # lijst.append(random.random() * 100)   # Met dit, zullen de elementen float type zijn.
    
    return lijst

def zoek_minimum(lijst):
    """
    Dit zoekt het minimum waarde van de lijst.

    Parameters
    ----------
    lijst: array
        Wordt gebruikt om de minimum waarde te vinden.
    
    Returns
    -------
    minimum: int/float
    """

    # minimum = lijst[0]                  # Uitwerking gebruikt minimum = math.inf zoiets.
    minimum = math.inf
    for i in range(0, len(lijst)):
        if minimum > lijst[i]:
            minimum = lijst[i]

    return minimum

def zoek_maximum(lijst):
    """
    Dit zoekt het maximum waarde van de lijst.

    Parameters
    ----------
    lijst: array
        Wordt gebruikt om de maximum waarde te vinden.
    
    Returns
    -------
    maximum: int/float
    """

    maximum = -math.inf
    for i in range(0, len(lijst)):
        if maximum < lijst[i]:
            maximum = lijst[i]

    return maximum

lijst = lijstmaker(n)
print(lijst)
minimum = zoek_minimum(lijst)
print(minimum)
maximum = zoek_maximum(lijst)
print(maximum)


'''
# Uitwerking voor a:

#a
import random
import math

def lijstmaker(n):
    lijst = []
    for i in range(n):
        lijst.append(random.randint(0, 100))
    return lijst

def minimum(lijst):
    mini = math.inf # plus oneindig waarde. 
    
    for i in range(len(lijst)):
        if lijst[i] < mini: # Je kijkt voor elk element in de lijst of het kleiner is dan je huidige minimum.
            mini = lijst[i] # Zo ja, dan heb je een nieuw minimum gevonden.
                            # Waarom heb je dan plus oneindig nodig?: Je zult het eerste element in je lijst 
    return mini             # met een ander getal moeten vergelijken! Geen enkel getal is groot genoeg, 
                            # behalve oneindig. (Waarom?).
n = int(input('Vul een geheel getal in\n'))

lijst = lijstmaker(n)

print(lijst)
print(minimum(lijst))


# # Output:

# Vul een geheel getal in
# 7
# [63, 8, 57, 30, 17, 80, 4]
# 4
'''

'''
# Uitwerking voor b:

#b
# import random
# import math

def lijstmaker(n):
    lijst = []
    
    for i in range(n):
        lijst.append(random.randint(0, 100))
        
    return lijst

def maximum(lijst):
    maxi = -math.inf  #zet een maximum van -oneindig
    
    for i in range(len(lijst)):
        if lijst[i] > maxi: #Vergelijk de getallen met het huidige maximum. Als een getal groter is, stel dan het maximum gelijk aan het getal. 
            maxi = lijst[i]
            
    return maxi

n = int(input('Vul een geheel getal in\n'))

lijst = lijstmaker(n)

print(lijst)
print(maximum(lijst))

# # Output:

# Vul een geheel getal in
# 11
# [86, 92, 9, 40, 80, 70, 71, 40, 10, 56, 41]
# 92
'''