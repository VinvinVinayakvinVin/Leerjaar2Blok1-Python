# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.2.py
@Time    :   2022/09/15 10:03:13
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* a. Schrijf een programma dat als invoer een decimaal getal x (in radialen) heeft en als uitvoer de waarde van sin x.
** b. Zoals a, maar nu is de invoer x in graden.

Tip: Houd het gebruikersvriendelijk!
'''

# programma voor a)
from math import pi, sin

x = float(input("Voer een decimaal getal x in radialen: "))
print(f"sin x = {sin(x)}")

# programma voor b)

x = float(input("Voer een decimaal getal x in graden: "))
print(f"sin x = {sin(x*pi/180)}")

'''
Uitwerking:

#a
import math #laad de math module

x = float(input('Geef het aantal radialen: ')) # Gebruiksvriendelijk: stel ook je vraag bij de input!

print('sin(x) = ' + str(math.sin(x))) #Gebruik de sinus functie uit de math module met math.sin()

#b
x = float(input('Geef het aantal graden: '))
radians = math.radians(x) #Zet het aantal graden eerst om naar radialen met radians()
print('' + str(math.sin(radians))) 

# als alternatief had je kunnen doen: radians = x/360*2*math.pi
'''

# # Zelf uitproberen wat met math.radians(x).
# import math
# x = float(input("Geef hier het aantal graden: "))
# print(math.radians(x))    # Berekent graden om naar radialen en daarna print het waarde uit.
# print(x*math.pi/180)      # Zelfde ⬆️