# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.3.py
@Time    :   2022/10/20 07:58:33
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
3.¶
* in statement.

Stel je wilt nagaan of een element in een lijst zit.
Bijv. of de kaassoort Goudse in de lijst kazen staat: kazen = [‘Edammer’, ‘Brie’, ‘Blue Danish’, ‘Stilton’]
Hiervoor kun je het in statement gebruiken:
'''

'''
kazen = ['Edammer', 'Brie', 'Blue Danish', 'Stilton']

print('Goudse' in kazen)
print('Brie' in kazen)
'''

'''
Als het element in de lijst staat geeft het in statement True,
zo niet dan False (dus een boolean datatype).

Maak nu een programma met daarin de volgende lijst (handmatig):
[‘Utrecht’, ‘Amsterdam’, ‘Den Bosch’, ‘Rotterdam’, ‘Den Haag’, ‘Haarlem’, ‘Maastricht’]

Noem deze lijst steden.

Als input kun je een stadsnaam invullen. Je programma geeft als uitvoer True als de stad in de lijst staat, anders False.
'''

steden = ['Utrecht', 'Amsterdam', 'Den Bosch', 'Rotterdam', 'Den Haag', 'Haarlem', 'Maastricht']
stadsnaam = input("Vul een stadsnaam in: ")

if stadsnaam in steden:
    print(True)
else:
    print(False)


'''
# Uitwerking:

steden = ['Utrecht', 'Amsterdam', 'Den Bosch', 'Rotterdam', 'Den Haag', 'Haarlem', 'Maastricht']

stadsnaam = input('Vul een stadsnaam in.\n')

#Komt de ingevulde stad voor in 'steden'
print(stadsnaam in steden)


# Output:

Vul een stadsnaam in.
Groningen
False
'''