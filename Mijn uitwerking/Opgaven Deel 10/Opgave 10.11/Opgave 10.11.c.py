# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.11.c.py
@Time    :   2022/11/23 01:53:27
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
!! *** c. (Lastig!) Vul b aan met: Als de naam van de voetballer niet voorkomt of de maandnaam niet goed is gespeld, 
moet je programma dit aangeven en opnieuw de voetballernaam of maandnaam vragen.
'''

################################################################################################## 10.11.c:

import os

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 10\\Opgave 10.11\\")
file = open("scores.txt")

maanden = []
namen = []
scores = []
dictionary = []

# Maanden setup
for maand in file.readline().split():
    if maand != "Naam":
        maanden.append(maand)

print(maanden)

# Namen en scores setup
i = 0
for zin in file.readlines():
    i += 1
    namen.append(zin.split()[0])
    scores.append(zin.split()[1:12+1])  # pak de tweede tot en met de 13ste element, ofwel 1e maand score t/m 12e score pakken :D
    dictionary.append([i, namen[i - 1]])  # 1 = Ronaldo, 2 = Maradonna, ..., 8 = Rijkaard -> (in code) -> [[1, 'Ronaldo'], [2, 'Maradonna'], ..., [3, 'Rijkaard']]

maandInput = input("Vul eerste drie letters van het maand in: ")
naaminput = input("Vul naam in: ")

while maandInput not in maanden:
    maandInput = input("Vul eerste drie letters van het maand in: ")

while naaminput not in namen:
    naaminput = input("Vul naam in: ")

for i in range(len(namen)):
    if dictionary[i][1] == naaminput:
        for j in range(len(maanden)):
            if maandInput == maanden[j]:
                print(scores[dictionary[i][0] - 1][j])
        
file.close()



# Uitwerking:
'''
# c.
file = open('scores.txt')
scores = file.readlines()

score_matrix = []

for line in scores:
    score_matrix.append(line.split())

print(score_matrix)

# Bepaal eerst in welke rij de voetballer staat, let op je begint met index 0.
def rijnr():
    # Als naam niet gevonden is, naam opnieuw vragen en zoeken in de matrix, totdat bekende naam is ingevoerd.
    is_naamonbekend = True
    is_eersteloop = True
    
    while is_naamonbekend:
        if is_eersteloop: #als de eersteloop True is, vraag dan om de naam als input anders, vraag opnieuw om een naam
            naam = input('Vul de naam van de voetballer in: ')
        else:
            naam = input('Ingevulde naam van de voetballer staat niet in het bestand, vul een juiste naam in: ')
            
        rij_nr = 0
        
        for rij in score_matrix: #zoek dan de naam op in de matrix
            if rij[0] == naam:
                is_naamonbekend = False
                return rij_nr
            else:               
                rij_nr = rij_nr + 1
                if rij_nr == len(score_matrix): #als je aan het eind van de matrix zit, vraag dan opnieuw een naam
                    is_eersteloop = False
            
# Bepaal eerst in welke kolom de maand staat, let op je begint met index 0.
def kolomnr():
    is_maandonbekend = True
    is_eersteloop = True
    
    while is_maandonbekend:
        if is_eersteloop:
            naam = input('Vul de maandnaam in, afgekort dus als jan, feb of maa: ')
        else:
            naam = input('Ingevulde maand is niet juist, vul juiste maandnaam in als jan, feb of maa: ')        
        kolom_nr = 0
        for kolom in score_matrix[0]:  # Op de eerste rij staan de maandnamen
            if kolom == naam:
                is_maandonbekend = False
                return kolom_nr
            else:
                kolom_nr = kolom_nr + 1
                if kolom_nr == len(score_matrix[0]):
                    is_eersteloop = False

rij_index = rijnr()
kolom_index = kolomnr()

print(score_matrix[rij_index][kolom_index])  
'''

# Output:
'''
[['Naam', 'jan', 'feb', 'maa', 'apr', 'mei', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec'], ['Ronaldo', '6', '6', '4', '8', '9', '7', '10', '6', '5', '7', '8', '9'], ['Maradonna', '5', '7', '3', '9', '8', '8', '9', '7', '4', '8', '7', '10'], ['Figo', '3', '9', '2', '4', '4', '16', '12', '6', '10', '7', '5', '6'], ['Zidane', '10', '9', '8', '7', '6', '5', '6', '7', '8', '9', '10', '11'], ['Muller', '5', '5', '5', '8', '8', '8', '10', '10', '10', '6', '6', '6'], ['Gullit', '3', '5', '7', '11', '13', '11', '7', '5', '3', '5', '7', '11'], ['Cruijf', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9'], ['Rijkaard', '11', '9', '10', '8', '7', '9', '9', '6', '5', '7', '6', '5']]
Vul de naam van de voetballer in: Michiel
Ingevulde naam van de voetballer staat niet in het bestand, vul een juiste naam in: Fido
Ingevulde naam van de voetballer staat niet in het bestand, vul een juiste naam in: Figo
Vul de maandnaam in, afgekort dus als jan, feb of maa: feb
9
'''