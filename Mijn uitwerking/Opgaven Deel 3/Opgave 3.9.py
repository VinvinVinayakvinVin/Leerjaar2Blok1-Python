# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.9.py
@Time    :   2022/09/23 18:16:59
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
** Schrijf een programma dat een willekeurige geheel getal tussen [500 en 2300) uitprint.

Gebruik hiervoor de random() functie en je creativiteit. Dus geen andere functie zoals in opgave 3.7b. Andere statements zijn wel toegestaan.
'''

# from random import random     => random()
# from random import *          => random()
# import random                 => random.random()
# ☝️ nog een manier om modules te importeren.

from random import *

num1 = 500
num2 = 2300 - num1
print(int(num1 + random()*num2))

'''
# Uitwerking:

# import random 

#random() trekt tussen [0, 1)
#int() rond het getal af naar beneden
getal = int(500 + 1800 * random.random()) 

print(getal)
'''