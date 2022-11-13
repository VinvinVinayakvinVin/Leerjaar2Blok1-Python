# -*-coding:utf-8 -*-
'''
@File    :   Bingo.py
@Time    :   2022/11/06 20:17:14
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

import os

os.chdir(os.getcwd() + "\\Eindopdracht\\")

file = open("test_input.txt")

file.readline() # skip/overslaan eerste regel van die trekkingsgetallen.

bingokaarten = []
bingokaart1 = []
bingokaart2 = []
bingokaart3 = []
temp_lijst = []

teller = 0
aantal_bingos_maken = 0

for line in file.readlines():               # line is als vb: line = ['zin_1', 'zin_2', ..., 'zin_n']
    # Het onderstaande code over rij = ..., zet een string type naar een lijst type.
    # Het rij ziet er bv zouit: ['2', '0', '12', '3', '7']
    rij = [line.strip()][0].split()
    if rij != []:
        for i in rij:
            temp_lijst.append(int(i))   # een tijdelijke lijstje, die voegt een getal erin van een rij.

        if teller % 5 == 0:
            bingokaarten.append([])
            aantal_bingos_maken += 1

        bingokaarten[aantal_bingos_maken - 1].append(temp_lijst)

        teller += 1
        temp_lijst = []

print(bingokaarten)

file.close()

file = open("test_input.txt")

trekkingsgetallen = file.readline().replace(",", " ").split()
for i in range(len(trekkingsgetallen)):
    trekkingsgetallen[i] = int(trekkingsgetallen[i])
print(trekkingsgetallen)

file.close()