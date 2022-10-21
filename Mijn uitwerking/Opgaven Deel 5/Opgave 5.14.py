# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.14.py
@Time    :   2022/10/21 17:49:57
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
14.¶
** Zie opgave 3. Als je utrecht schrijft i.p.v. 
Utrecht zal je programma bij opgave a False geven. 
Om dit te voorkomen kun je ervoor zorgen dat de stadsnamen allemaal met kleine letters wordt geschreven, 
of juist allemaal met hoofdletter! Zowel de namen in je stedenlijst als de stadsnaam van je input.

Vul je programma van opgave 3 nu aan met:

Laat je programma (dus niet handmatig) de stadsnamen in je stedenlijst veranderen: alles nu met kleine letters geschreven.
Zorg ervoor dat de inputwaarde verandert in een naam met alleen maar kleine letters.
Je hebt hier de functie lower() voor nodig. Zoek dit op internet op! En een for-loop.

Lukt het alternatief ook, alles met hoofdletter schrijven?
'''

# Eerste poging ⬇️:

# # Versie met lower():

# steden = ['utrecht', 'amsterdam', 'den bosch', 'rotterdam', 'den haag', 'haarlem', 'maastricht']
# stadsnaam = input("Vul een stadsnaam in: ").lower()

# # if stadsnaam in steden:
# #     print(True)
# # else:
# #     print(False)

# n = len(steden)
# is_stadsnaam = False
# for i in range(n):
#     if stadsnaam == steden[i]:
#         is_stadsnaam = True
# print(is_stadsnaam)


# # Versie met upper():

# steden = ['UTRECHT', 'AMSTERDAM', 'DEN BOSCH', 'ROTTERDAM', 'DEN HAAG', 'HAARLEM', 'MAASTRICHT']
# stadsnaam = input("Vul een stadsnaam in: ").upper()

# n = len(steden)
# is_stadsnaam = False
# for i in range(n):
#     if stadsnaam == steden[i]:
#         is_stadsnaam = True
# print(is_stadsnaam)


'''
# Uitwerking v1:

steden = ['Utrecht', 'Amsterdam', 'Den Bosch', 'Rotterdam', 'Den Haag', 'Haarlem', 'Maastricht']

#lower() geeft een string met alleen kleine letters (lower case)
for i in range(len(steden)):
    steden[i] = steden[i].lower()

stadsnaam = input('Vul een stadsnaam in.\n').lower() # .lower() mag je dus direct achter de print statement zetten
print(stadsnaam in steden)

# Zie hoe de lijst en je input veranderd is:
print(steden)
print(stadsnaam)


# # Output v1:

# Vul een stadsnaam in.
# UTRecht
# True
# ['utrecht', 'amsterdam', 'den bosch', 'rotterdam', 'den haag', 'haarlem', 'maastricht']
# utrecht
'''

'''
# Uitwerking v2:

# Alternatief met uppercase

steden = ['Utrecht', 'Amsterdam', 'Den Bosch', 'Rotterdam', 'Den Haag', 'Haarlem', 'Maastricht']

for i in range(len(steden)):
    steden[i] = steden[i].upper()

stadsnaam = input('Vul een stadsnaam in.\n').upper()
print(stadsnaam in steden)

# Zie hoe de lijst en je input veranderd is:
print(steden)
print(stadsnaam)


# # Output v2:

# Vul een stadsnaam in.
# GrOnInGeN
# False
# ['UTRECHT', 'AMSTERDAM', 'DEN BOSCH', 'ROTTERDAM', 'DEN HAAG', 'HAARLEM', 'MAASTRICHT']
# GRONINGEN
'''

# Tweede poging ⬇️:
# lowercase versie:

steden = ['Utrecht', 'Amsterdam', 'Den Bosch', 'Rotterdam', 'Den Haag', 'Haarlem', 'Maastricht']

for i in range(len(steden)):
    steden[i] = steden[i].lower()

stadsnaam = input("Vul een stadsnaam in: ").lower()

print(stadsnaam in steden)
print(steden)
print(stadsnaam)

# uppercase versie:

steden = ['Utrecht', 'Amsterdam', 'Den Bosch', 'Rotterdam', 'Den Haag', 'Haarlem', 'Maastricht']

for i in range(len(steden)):
    steden[i] = steden[i].upper()

stadsnaam = input("Vul een stadsnaam in: ").upper()

print(stadsnaam in steden)
print(steden)
print(stadsnaam)