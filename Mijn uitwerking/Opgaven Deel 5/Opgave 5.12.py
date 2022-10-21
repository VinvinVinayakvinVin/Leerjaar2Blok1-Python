# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.12.py
@Time    :   2022/10/21 12:04:50
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
12.¶
** Inproduct van twee vectoren

Neem de vector v = [1, 2, 3, 4, 5] en de vector w = [25, 16, 9, 4, 1].
Schrijf een programma dat van deze twee vectoren het inproduct bepaald.

Hint: Gebruik een for-loop en voor een vector kun je een list gebruiken.
'''

v = [1, 2, 3, 4, 5]
w = [25, 16, 9, 4, 1]
inproduct = 0

for i in range(5):
    inproduct = inproduct + v[i] * w[i]

print(inproduct)


'''
# Uitwerking:

v = [1, 2, 3, 4, 5] 
w = [25, 16, 9, 4, 1]

#Maak een variabele om de som bij te houden
inproduct = 0

for x in range(5):
    #tel steeds het product van v[x] en w[x] bij de som op
    inproduct = inproduct + v[x] * w[x]

print(inproduct)


#alternatief met len(). len() geeft de lengte van een vector terug. 
#Handig als de lengte van de vectoren niet van te voren bekend is of kan variëren.

v = [1, 2, 3, 4, 5] 
w = [25, 16, 9, 4, 1]

inproduct = 0

for x in range(len(v)):
    inproduct = inproduct + v[x] * w[x]

print(inproduct)
'''