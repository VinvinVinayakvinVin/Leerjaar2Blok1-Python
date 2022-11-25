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

# maand lijst opslaan in een variabele regel1:
regel1 = file.readline().split()
regel1.remove("Naam")

maandnaam_input = input("Vul een maandnaam in (Let op, als je januari wilt intypen, type dan in de eerste drie letters! (=jan)): ")
voetballernaam_input = input("Vul een voetballernaam in: ")

maandnum = 0

while maandnaam_input not in regel1:
        maandnaam_input = input("Vul maandnaam nogmaals in (Je hebt het verkeerd gespeld: ")
# while voetballernaam_input not in zin.split():
#     print(zin.split())
#     input("Vul een voetballernaam CORRECT in: ")

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

# # zoek score num bij bijbehorende voetballer en maand
# for zin in file.readlines():    
#     while voetballernaam_input not in zin.split():
#         voetballernaam_input = input("Vul een voetballernaam CORRECT in: ")

#     if voetballernaam_input in zin.split():
#         print("score is: " + str(zin.split()[maandnum]))
#         break

file.close()