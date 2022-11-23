# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.11.b.py
@Time    :   2022/11/23 01:09:06
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
** b. Vul je programma aan met: 
Na het inlezen van de textfile wordt de gebruiker gevraagd om de naam van een voetballer in te vullen en daarna de maandnaam (jan, jun, aug, etc). 
Vervolgens wordt er geprint wat het aantal doelpunten is geweest van de desbetreffende voetballer en maand.
'''

################################################################################################## 10.11.b:

import os

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 10\\Opgave 10.11\\")
file = open("scores.txt")

# maand lijst opslaan in een variabele regel1:
regel1 = file.readline().split()
regel1.remove("Naam")

maandnaam_input = input("Vul een maandnaam in (Let op, als je januari wilt intypen, type dan in de eerste drie letters! (=jan)): ")
voetballernaam_input = input("Vul een voetballernaam in: ")

maandnum = 0

# maandnaam converteren naar maandnum
for i in range(len(regel1)):
    if maandnaam_input == regel1[i]:
        maandnum = i + 1
        break

# zoek score num bij bijbehorende voetballer en maand
for zin in file.readlines():
    if voetballernaam_input in zin.split():
        print("score is: " + str(zin.split()[maandnum]))

file.close()



# Uitwerking:
'''
# b. Aanvulling op a.
voetballernaam = input('Vul de naam van de voetballer in: ')
maand = input('Vul de maandnaam in, afgekort dus als jan, feb of maa: ')

# Bepaal eerst in welke rij de voetballer staat, let op je begint met index 0.
def rijnr(naam):
    rij_nr = 0
    
    for rij in score_matrix:
        if rij[0] == naam:
            return rij_nr
        else:
            rij_nr = rij_nr + 1
            
# Bepaal eerst in welke kolom de maand staat, let op je begint met index 0.
def kolomnr(naam):
    kolom_nr = 0
    
    for kolom in score_matrix[0]:  # Op de eerste rij staan de maandnamen
        if kolom == naam:
            return kolom_nr
        else:
            kolom_nr = kolom_nr + 1

rij_index = rijnr(voetballernaam)
kolom_index = kolomnr(maand)

print(score_matrix[rij_index][kolom_index])



# Output:

Vul de naam van de voetballer in: Figo
Vul de maandnaam in, afgekort dus als jan, feb of maa: jan
3
'''