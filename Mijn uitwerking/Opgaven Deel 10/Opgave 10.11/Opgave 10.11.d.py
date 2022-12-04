# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.11.d.py
@Time    :   2022/12/04 16:23:42
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

################################################################################################## 10.11.d:

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

gem = 0
for i in range(len(namen)):
    if dictionary[i][1] == naaminput:
        for j in range(len(maanden)):
            gem += int(scores[dictionary[i][0] - 1][j])
            if maandInput == maanden[j]:
                print(scores[dictionary[i][0] - 1][j])

gem = gem / 12                
print("De gemiddelde score van voetballer " + naaminput + " is: " + str(gem))
        
file.close()


# Uitwerking:
'''
#d. Aanvulling
score = []

for i in range(1, 13):
    score.append(int(score_matrix[rij_index][i])) # Van string getallen '3' getallen maken 3.
    
gemiddelde = sum(score)/12    
print(gemiddelde)
'''

# Output:
'''
7.0
'''