# -*-coding:utf-8 -*-
'''
@File    :   Bingo.py
@Time    :   2022/11/06 20:17:14
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   Bingo spel :D
'''

def findindexnums(bingokaart, trekkingsgetal):
    """
    finds indexnum of 2d array

    Parameters
    ----------
    bingokaart: 2d array
    trekkingsgetal: int

    Returns
    -------
    indexnums: array
    """

    indexnums = []

    for i in range(len(bingokaart)):
        for j in range(len(bingokaart[i])):
            if trekkingsgetal == bingokaart[i][j]:
                indexnums.append(i)
                indexnums.append(j)
                break

    return indexnums

def transponeren(bingokaart):
    """
    Dit wisselt alle rijen met kolommen.

    Parameters
    ----------
    bingokaart: 2d array

    Returns
    -------
    transponeerde_kaart: 2d array
    """

    # per kolom printen:
    transponeerde_kaart = []
    teller = 0
    for i in range(5):
        transponeerde_kaart.append([])
        for j in range(5):
            transponeerde_kaart[teller].append(bingokaart[j][i])
        teller += 1
    return transponeerde_kaart


import os

# os.chdir(os.getcwd() + "\\Eindopdracht\\")
file = open("test_input.txt")

trekkingsgetallen = file.readline().replace(",", " ").split()
for i in range(len(trekkingsgetallen)):
    trekkingsgetallen[i] = int(trekkingsgetallen[i])
print(trekkingsgetallen)

bingokaarten = []
temp_lijst = []     # Dit wordt later vaak gebruikt om een rij in een bingokaart lijst toe te voegen.

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

print("\n" + str(bingokaarten))

file.close()

# Hier beneden gaat over de aanroepen van trekkingsgetallen.
# En het checken van bingokaarten, of daar een trekkingsgetal zit.

stop = False
laatste_trekgetal = -1
aantal_trekkingen = 0
aantal_bingos = 0
lijst_dat_bingo_heeft = []

for trekgetal in trekkingsgetallen:
    aantal_trekkingen += 1
    for bingokaart_num in range(len(bingokaarten)):
        for rij in range(5):
            for i in range(5):  # Dit is een getal uit een rij.
                if bingokaarten[bingokaart_num][rij][i] == trekgetal:
                    print(f"\n{trekgetal}")
                    laatste_trekgetal = bingokaarten[bingokaart_num][rij][i]
                    bingokaarten[bingokaart_num][rij][i] = ""
                    print(f"bingokaart: {bingokaart_num + 1}, aantal getallen getrokken: {aantal_trekkingen}")
                    for l in range(len(bingokaarten[bingokaart_num])):
                        # if stop == False:
                        print(bingokaarten[bingokaart_num][l])
        if bingokaarten[bingokaart_num][rij] == ['', '', '', '', ''] or transponeren(bingokaarten[bingokaart_num])[rij] == ['', '', '', '', '']:
            if bingokaart_num not in lijst_dat_bingo_heeft:
                print("BINGO!", laatste_trekgetal)
                lijst_dat_bingo_heeft.append(bingokaart_num + 1)
                # aantal_bingos += 1
