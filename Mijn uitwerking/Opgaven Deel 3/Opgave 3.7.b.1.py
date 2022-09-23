# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.7.b.1.py
@Time    :   2022/09/23 17:42:53
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
** b.   Maak een programma dat tussen de gehele getallen n en m een willekeurig geheel getal uitprint.
        Kun je op internet een geschikte functie hiervoor vinden in de random module?
'''

from random import randint

n = int(input("Type een geheel getal in: "))
m = int(input("Type nogmaals een geheel getal in: "))

for i in range (50):                     # Dit voert de instructies beneden 3 keer.
    x = randint(min(n, m), max(n, m))   # Pakt een willekeurig geheel getal tussen 0 en 3 (inclusief getallen 0 en 3).
    print(x)

# Mijn antwoord: Gebruik randint functie om een willekeurig geheel getal te pakken.

'''
# Uitwerking van dit opdracht:

# import random 

n = int(input('Geef n: '))
m = int(input('Geef m: '))

print(random.randint(n, m))

# Geef n: 20
# Geef m: 100
# 97
'''