# -*-coding:utf-8 -*-
'''
@File    :   test2file.py
@Time    :   2022/11/25 03:42:08
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

opgeroepen_cijfers = ['7', '4', '9', '5', '11', '17', '23', '2', '0', '14', '21', '24', '10', '16', '13', '6', '15', '25', '12', '22', '18', '20', '8', '19', '3', '26', '1']
lijst = [['22', '13', '17', '11', '0'], ['8', '2', '23', '4', '24'], ['21', '9', '14', '16', '7'], ['6', '10', '3', '18', '5'], ['1', '12', '20', '15', '19']]

is_bingo = False

def check_vert_bingo():
    temp_lijst = []
    global is_bingo
    for i in range(5):
        for j in range(5):
            if lijst[j][i] == "x":
                temp_lijst.append("JAAA")
                if len(temp_lijst) == 5:
                    if "NEee" not in temp_lijst:
                        if is_bingo == False:
                            print("(verticaal) Bingo!!!")
                            print(temp_lijst)
                            print(lijst)
                            is_bingo = True

            else:
                temp_lijst.append("NEee")
        temp_lijst = []

def check_hori_bingo():
    temp_lijst = []
    global is_bingo
    for i in range(5):
        for j in range(5):
            if lijst[i][j] == "x":
                temp_lijst.append("JAAA")
                if len(temp_lijst) == 5:
                    if "NEee" not in temp_lijst:
                        if is_bingo == False:
                            print("(horizontaal) Bingo!!!")
                            print(temp_lijst)
                            print(lijst)
                            is_bingo = True

            else:
                temp_lijst.append("NEee")
        temp_lijst = []

teller = 0

for i in opgeroepen_cijfers:
    for j in range(5):
        for k in range(5):
            if lijst[j][k] == i:
                lijst[j][k] = "x"
                teller += 1
                print("\n" + str(teller))
                check_hori_bingo()
                check_vert_bingo()

print(lijst)