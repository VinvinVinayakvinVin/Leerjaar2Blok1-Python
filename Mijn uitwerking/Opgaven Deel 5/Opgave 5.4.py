# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.4.py
@Time    :   2022/10/20 08:05:05
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
4.¶
* append statement.

Je kunt ook een lijst aanmaken via input (i.p.v. handmatig een lijst maken in je code).
Hiervoor hebben we de append statement nodig en een lege lijst.
Eerst wordt een lege lijst aangemaakt en daarna vullen we die lijst met elementen. Voorbeeld:
'''

'''
#Lege lijst
namen = []

#Drie namen om in de lijst 'namen' te zetten
naam1 = input('Vul de eerste naam in\n ')
naam2 = input('Vul de tweede naam in\n ')
naam3 = input('Vul de derde naam in \n ')

#De lijst 'namen' aanvullen met de drie opgegeven namen via input
namen.append(naam1)
namen.append(naam2)
namen.append(naam3)

#De lijst 'namen' printen
print(namen)
'''

'''
Een lege lijst verkrijg je door [], bijv. namen = []. Namen is nu een lege lijst.
Je kunt daarna steeds een nieuw element toevoegen aan de lijst met .append().
namen.append(naam1) voegt dan de waarde van naam1 toe aan de lijst namen.

a. Schrijf een programma dat de gebruiker vijf getallen laat invullen en die getallen in een lijst zet. Print de lijst daarna uit.
'''


from random import *

num1 = float(input("Vul getal 1 in: "))
num2 = float(input("Vul getal 2 in: "))
num3 = float(input("Vul getal 3 in: "))
num4 = float(input("Vul getal 4 in: "))
num5 = float(input("Vul getal 5 in: "))

lijstje = []

lijstje.append(num1)
lijstje.append(num2)
lijstje.append(num3)
lijstje.append(num4)
lijstje.append(num5)

print(lijstje)


'''
b. Schrijf een programma dat drie willekeurige getallen tussen [0, 10) in een lijst zet. Print de lijst daarna uit.

Tip: Met welke functie kon je ook alweer willekeurige (gehele) getallen maken uit een gegeven bereik?
'''

random_lijstje = []

random_lijstje.append(int(random()*10))
random_lijstje.append(int(random()*10))
random_lijstje.append(randint(0, 9))

print(random_lijstje)


'''
# Uitwerking b:

getallen = []

#a
getal1 = float(input('Vul een getal in\n'))
getal2 = float(input('Vul een getal in\n'))
getal3 = float(input('Vul een getal in\n'))
getal4 = float(input('Vul een getal in\n'))
getal5 = float(input('Vul een getal in\n'))

#Nog een manier om meerdere inputs te geven. Type meerdere getallen in 1 keer gescheiden door een spatie.
# getal1, getal2, getal3, getal4, getal5 = input("Vul 5 getallen in: ").split()
# deze .split() wordt in een latere les nog besproken, maar nu ken je hem alvast!

getallen.append(getal1)
getallen.append(getal2)
getallen.append(getal3)
getallen.append(getal4)
getallen.append(getal5)

print(getallen)


# # Output:

# Vul een getal in
# 6
# Vul een getal in
# 2
# Vul een getal in
# 9
# Vul een getal in
# 7
# Vul een getal in
# 1
# [6.0, 2.0, 9.0, 7.0, 1.0]
'''

'''
# Uitwerking b:

#b
import random

willekeur = []

#Kies random 3 getallen
getal1 = random.randint(0, 9)
getal2 = random.randint(0, 9)
getal3 = random.randint(0, 9)

willekeur.append(getal1)
willekeur.append(getal2)
willekeur.append(getal3)

print(willekeur)


# # Output:

# [6, 2, 8]
'''