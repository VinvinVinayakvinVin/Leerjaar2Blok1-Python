# -*-coding:utf-8 -*-
'''
@File    :   Opgave 6.2.py
@Time    :   2022/10/22 07:40:22
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
2.¶
* We hebben de volgende lijst elementen:

elementen = ['roos', 'distel', 10, 'viooltje', True, 9.6, False]

In een lijst kunnen blijkbaar waardes staan met verschillende datatypes: string, integer, boolean, etc.

Schrijf een programma dat een lijst genereert waarin n-maal de elementen uit de lijst 'elementen' staat. Dus bij n = 2, krijg je:

['roos', 'distel', 10, 'viooltje', True, 9.6, False, 'roos', 'distel', 10, 'viooltje', True, 9.6, False]
'''

import random

# def lijst_maken():
#     """
#     Dit functie maakt een lijst m.b.v jouw user input

#     Parameters
#     ----------
#     None

#     Returns
#     -------
#     lijst: array
#     """
    
#     lijst = []
#     for i in range(random.randint(1, 5)):
#         lijst.append(input("Vul hier iets in: "))
#     return lijst

def mult_elements_in_list(lijst, n):
    """
    Dit zorgt ervoor dat de bestaande elementen in een lijst,
    n maal nogmaal staat in de bewerkte lijst.

    Parameters
    ----------
    lijst: array
        lijst waarbij al bestaande elementen al zitten.

    n: integer
        n komt van een user input, die een geheel getal heeft getypd.

    Returns
    -------
    nw_lijst: array (lijst)
    """
    
    nw_lijst = []
    for i in range(n):
        nw_lijst = nw_lijst + lijst
    return nw_lijst

n = int(input("Vul een geheel getal in voor n: "))
# lijst = lijst_maken()
lijst = ['roos', 'distel', 10, 'viooltje', True, 9.6, False]
nw_lijst = mult_elements_in_list(lijst, n)

print(lijst)
print(nw_lijst, end="\n\n\n")



'''
# Uitwerking:

elementen = ['roos', 'distel', 10, 'viooltje', True, 9.6, False]

n = int(input('Vul geheel getal in: '))

print(elementen * n)
'''

print(lijst * n)    # <-- deze kan je ook doen.