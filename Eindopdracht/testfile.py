# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 21:35:37 2022

@author: vinay
"""

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


bingokaart = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18,19, 20], [21, 2, 23, 24, 25]]
trekkingslijst = [7, 4, 9, 5, 11, 17, 23, 2, 10, 14, 21, 24, 12, 16, 13, 6, 15, 25, 18, 22, 20, 8, 19, 3, 1]
laatste_trekgetal = -1

print("\n\nbingokaart:")
print(bingokaart, "\n\n")
stop = False

for trekgetal in trekkingslijst:
    for rij in range(5):
        for bingogetal in range(5):
            if bingokaart[rij][bingogetal] == trekgetal:
                if stop == False:
                    print(f"\n{trekgetal}")
                laatste_trekgetal = bingokaart[rij][bingogetal]
                bingokaart[rij][bingogetal] = ""
                for l in range(len(bingokaart)):
                    if stop == False:
                        print(bingokaart[l])
        if bingokaart[rij] == ['', '', '', '', ''] or transponeren(bingokaart)[rij] == ['', '', '', '', '']:
            print("BINGO!", laatste_trekgetal)
            stop = True
    if stop:
        break

bingokaarten = [bingokaart]
print(bingokaarten)
# print(bignokaarten)
print(transponeren(bingokaarten[0]))