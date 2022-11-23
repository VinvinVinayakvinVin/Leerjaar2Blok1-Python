# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.11.a.py
@Time    :   2022/11/22 17:51:17
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
11. Gegevens opzoeken uit een databestand¶
Download het bestand scores.txt van Bightspace. Open het bijv. met notepad of kladblok. 
Je ziet er voetballers staan met het aantal doelpunten per maand dat ze in een zeker jaar hebben gemaakt. 
(Sorry als het niet helemaal realistisch is).

** a. Schrijf een programma dat het bestand scores.txt opent en 
inleest en de gegevens opslaat in een matrix (geneste lijst). 
De elementen van elke rij van de matrix zijn de naam van de voetballer en de scores van hem. 
Print de matrix daarna uit (en controleer of de matrix klopt).

Hint: gebruik een for-loop en ook split()
'''

import os

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 10\\Opgave 10.11\\")
file = open("scores.txt")

# maand lijst opslaan in een variabele regel1:
regel1 = file.readline().split()
regel1.remove("Naam")

alle_scores = []
namen = []

for zin in file.readlines():
    individu_scores = zin.split()
    namen.append(individu_scores[0])
    del individu_scores[0:1]
    alle_scores.append(individu_scores)

print(regel1)

# print(alle_scores)
# print(namen)

Ronaldo = alle_scores[0]
Maradonna = alle_scores[1]
Figo = alle_scores[2]
Zidane = alle_scores[3]
Muller = alle_scores[4]
Gullit = alle_scores[5]
Cruijf = alle_scores[6]
Rijkaard = alle_scores[7]

print(Ronaldo)
print(Maradonna)
print(Figo)
print(Zidane)
print(Muller)
print(Gullit)
print(Cruijf)
print(Rijkaard)

file.close()



# Uitwerking:
'''
# a.
file = open('scores.txt')
scores = file.readlines()

score_matrix = []

for line in scores:
    score_matrix.append(line.split())

print(score_matrix)



# Output:

[['Naam', 'jan', 'feb', 'maa', 'apr', 'mei', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec'], ['Ronaldo', '6', '6', '4', '8', '9', '7', '10', '6', '5', '7', '8', '9'], ['Maradonna', '5', '7', '3', '9', '8', '8', '9', '7', '4', '8', '7', '10'], ['Figo', '3', '9', '2', '4', '4', '16', '12', '6', '10', '7', '5', '6'], ['Zidane', '10', '9', '8', '7', '6', '5', '6', '7', '8', '9', '10', '11'], ['Muller', '5', '5', '5', '8', '8', '8', '10', '10', '10', '6', '6', '6'], ['Gullit', '3', '5', '7', '11', '13', '11', '7', '5', '3', '5', '7', '11'], ['Cruijf', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9'], ['Rijkaard', '11', '9', '10', '8', '7', '9', '9', '6', '5', '7', '6', '5']]
'''