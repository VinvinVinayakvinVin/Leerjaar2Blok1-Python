# -*-coding:utf-8 -*-
'''
@File    :   10.11.c (stukje code).py
@Time    :   2022/12/03 13:24:43
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

import os

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 10\\Opgave 10.11\\")
file = open("scores.txt")

# maand lijst opslaan in een variabele regel1:
regel1 = file.readline().split()
regel1.remove("Naam")

# maandnaam_input = input("Vul de eerste drieletters van een maandnaam in: ")
# voetballernaam_input = input("Vul een voetballernaam in: ")

maandnum = 0

while maandnaam_input not in regel1:
        maandnaam_input = input("Vul maandnaam nogmaals in (Je hebt het verkeerd gespeld: ")

# maandnaam converteren naar maandnum
for i in range(len(regel1)):
    if maandnaam_input == regel1[i]:
        maandnum = i + 1
        break

alle_scores = []
namen = []

for zin in file.readlines():
    individu_scores = zin.split()
    namen.append(individu_scores[0])
    del individu_scores[0:1]
    alle_scores.append(individu_scores)

Ronaldo = alle_scores[0]
Maradonna = alle_scores[1]
Figo = alle_scores[2]
Zidane = alle_scores[3]
Muller = alle_scores[4]
Gullit = alle_scores[5]
Cruijf = alle_scores[6]
Rijkaard = alle_scores[7]

for naam in namen:
    print(naam)

file.close()