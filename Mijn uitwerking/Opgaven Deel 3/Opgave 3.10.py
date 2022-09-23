# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.10.py
@Time    :   2022/09/23 18:27:53
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* Onderzoek de random module nog eens (op internet).

Doe opgave 3.9 nogmaals, maar nu met een functie uit de random module.
'''

'''
Dit is de opgave van 3.9 ⬇️
** Schrijf een programma dat een willekeurige geheel getal tussen [500 en 2300) uitprint.
Gebruik hiervoor de random() functie en je creativiteit. Dus geen andere functie zoals in opgave 3.7b. Andere statements zijn wel toegestaan.
'''

from random import *

# print(500 + randint(0, 1799))   # randint function [0, 1799] (1800 is exclusief). => 500 + 0 = 500 minimum, 500 + 1799 = 2299 als maximum.
for i in range(1000):           # Deze laten loopen, om te testen of er 2300 wel in de lijstje staat.
    print(randint(500, 2300))   # <- Deze heeft als maximum 2300 inclusief.
    

'''
Uitwerking:

# import random

#randrange() genereert een random getal in de gegeven range
print(random.randrange(500, 2300))
'''