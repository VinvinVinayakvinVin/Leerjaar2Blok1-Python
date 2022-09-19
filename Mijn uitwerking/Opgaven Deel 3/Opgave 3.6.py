# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.6.py
@Time    :   2022/09/18 18:13:09
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
!! ** Een andere module die goed van pas komt is de random module. 
Als je functies wil gebruiken uit deze module moet je de module eerst importeren, 
zoals je dat deed bij de math module. Eén van de functies in random is random(), 
die genereert willekeurig een getal tussen [0, 1). 0 kan het worden, maar 1 nooit.

Schrijf een programma dat drie willekeurige getallen tussen [0 en 1) uitprint. 
Zet de getallen naast elkaar met ertussen vier spaties.

Hint: hoe roep je functies ook alweer aan in de math module? Doe nu iets soortgelijks voor de random module.
'''

import math
import random

random_num1 = random.random()
random_num2 = random.random()
random_num3 = random.random()
print(f"{random_num1}\n{random_num2}\n{random_num3}")

'''
# Uitwerking:

import random

#genereer 3 random getallen tussen [0, 1)
random1 = random.random()
random2 = random.random()
random3 = random.random()

#1e manier
print(f"{random1}    {random2}    {random3}")

#2e manier
print(str(random1) + "    " + str(random2) + "    " + str(random3)) # Waarom moet je ook alweer str() gebruiken?

#3e manier
string_length1 = len(str(random1)) + 4 #len() geeft de lengte van een string. Met 4 maak je deze 4 karakters langer
string_length2 = len(str(random2)) + 4
string_length3 = len(str(random3)) + 4

random1_string = str(random1).ljust(string_length1) #ljust() voegt space toe aan het eind van een string
random2_string = str(random2).ljust(string_length2) #tegenovergestelde: rjust() voegt space toe aan het begin van een string
random3_string = str(random3).ljust(string_length3)
                     
print(f'{random1_string}{random2_string}{random3_string}')

# output:
# 0.029898263221144084    0.0335937898510863    0.10547926099254601
# 0.029898263221144084    0.0335937898510863    0.10547926099254601
# 0.029898263221144084    0.0335937898510863    0.10547926099254601  
'''

