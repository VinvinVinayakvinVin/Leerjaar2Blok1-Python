# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.7.b.2.py
@Time    :   2022/09/23 17:57:03
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
** b.   Maak een programma dat tussen de gehele getallen n en m een willekeurig geheel getal uitprint.
        Kun je op internet een geschikte functie hiervoor vinden in de random module?
'''

from random import randrange


for i in range(30):
        x = randrange(0, 3, 1)          # Pakt een willekeurig getal tussen 0 en 3, maar 3 is exclusief en 0 is inclusief. (Het neemt stappen van 1).
        print(x)

# randrange kan je ook gebruiken om een willekeurig getal te pakken.