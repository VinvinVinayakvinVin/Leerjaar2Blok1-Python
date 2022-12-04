# -*-coding:utf-8 -*-
'''
@File    :   test3file.py
@Time    :   2022/11/25 13:31:34
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

import os

os.chdir(os.getcwd() + "\\Eindopdracht\\")
file = open("test_input.txt", "r")
opgeroepen_cijfers = file.readline().strip().split(",")
alle_kaarten = file.readlines()

file.close()

#Hieronder maak ik een nested lijst voor mijn bingo kaarten
enkele_kaart = []
matrix = []
bingo = False

aantal_rijen = len(alle_kaarten)
aantal_kaarten = int(aantal_rijen/6)

for line in alle_kaarten: 
    lijst=[]  
    for element in line.strip().split(","):
        lijst.append(element)
    matrix.append(lijst)

def kaarten_splitsen (rij1, bestand):
    for i in range(rij1,rij1+5):
        for rij in matrix[i]:
            lijst = []
            for element in rij.strip().split():
                lijst.append(element)
            bestand.append(lijst)
    return bestand

def check_vert_bingo(matrix):
    temp_lijst = []
    global bingo
    for i in range(5):
        for j in range(5):
            if matrix[j][i] == "X":
                temp_lijst.append("Y")
                if len(temp_lijst) == 5:
                    if "X" not in temp_lijst:
                        if bingo == False:
                            print("(verticaal) Bingo!!!")
                            # print(temp_lijst)
                            print(matrix)
                            bingo = True
            else:
                temp_lijst.append("X")
        temp_lijst = []

def check_hori_bingo(matrix):
    temp_lijst = []
    global bingo
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == "X":
                temp_lijst.append("Y")
                if len(temp_lijst) == 5:
                    if "X" not in temp_lijst:
                        if bingo == False:
                            print("(horizontaal) Bingo!!!")
                            # print(temp_lijst)
                            print(matrix)
                            bingo = True

            else:
                temp_lijst.append("X")
        temp_lijst = []

teller = 1
def checkbingo():
    global teller
    kaarten_splitsen(teller, enkele_kaart)
    for i in opgeroepen_cijfers:
        for j in range(5):
            for k in range(5):
                while 6 * (teller // 6) + 1 < aantal_rijen:
                    print(teller)
                    if 6 * (teller // 6) + 1 == teller:
                        kaarten_splitsen(teller, enkele_kaart)
                        print(enkele_kaart)
                    if enkele_kaart[j][k] == i:
                        enkele_kaart[j][k] = "X"
                        check_hori_bingo(enkele_kaart)
                        check_vert_bingo(enkele_kaart)
                        print("test")
                    teller += 6
                    print(enkele_kaart[j][k])
                    enkele_kaart.clear()

# for i in range(30):
#     print(6 * (i // 6) + 1)

checkbingo()

# teller = 1
# while teller < aantal_rijen:
#     kaarten_splitsen(teller, enkele_kaart)
#     print(enkele_kaart)
#     print(teller)
#     enkele_kaart.clear()
#     teller += 6