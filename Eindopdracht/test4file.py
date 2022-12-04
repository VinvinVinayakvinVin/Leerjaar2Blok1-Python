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
       
aantal_rijen = len(alle_kaarten)
aantal_kaarten = int(aantal_rijen/6)

# def check_vert_bingo(matrix):
#     temp_lijst = []
#     global bingo
#     for i in range(5):
#         for j in range(5):
#             if matrix[j][i] == "X":
#                 temp_lijst.append("Y")
#                 if len(temp_lijst) == 5:
#                     if "X" not in temp_lijst:
#                         if bingo == False:
#                             print("(verticaal) Bingo!!!")
#                             print(temp_lijst)
#                             print(matrix)
#                             bingo = True
#             else:
#                 temp_lijst.append("X")
#         temp_lijst = []

# def check_hori_bingo(matrix):
#     temp_lijst = []
#     global bingo
#     for i in range(5):
#         for j in range(5):
#             if matrix[i][j] == "X":
#                 temp_lijst.append("Y")
#                 if len(temp_lijst) == 5:
#                     if "X" not in temp_lijst:
#                         if bingo == False:
#                             print("(horizontaal) Bingo!!!")
#                             print(temp_lijst)
#                             print(matrix)
#                             bingo = True

#             else:
#                 temp_lijst.append("X")
#         temp_lijst = []
        
teller = 1
while teller < aantal_rijen:
    kaarten_splitsen(teller, enkele_kaart)
    print(enkele_kaart)
    print(teller)
    # counter = 0
    # for i in opgeroepen_cijfers:
    #     for j in range(5):
    #         for k in range(5):
    #             if enkele_kaart[j][k] == i:
    #                 enkele_kaart[j][k] = "X"
    #                 teller += 1
    #                 print("\n" + str(teller))
    #                 check_hori_bingo(enkele_kaart)
    #                 check_vert_bingo(enkele_kaart)
    enkele_kaart.clear()
    teller += 6