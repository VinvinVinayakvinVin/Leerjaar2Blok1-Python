# -*-coding:utf-8 -*-
'''
@File    :   Bingo.py
@Time    :   2022/11/06 20:17:14
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

import os

# oude_lijst = ['7', '4', '9', '5', '11', '17', '23', '2', '0', '14', '21', '24', '10', '16', '13', '6', '15', '25', '12', '22', '18', '20', '8', '19', '3', '26', '1\n']
# nieuwe_lijst = []

# for i in oude_lijst:
#     nieuwe_lijst.append(int(oude_lijst[i].strip("\n")))

# print(nieuwe_lijst)

# txt = "Hoi ik ga slapen"
# lijst = txt.split()
# print(lijst)

os.chdir(os.getcwd() + "\\Eindopdracht\\")

file = open("test_input.txt")
# nummers = file.readline()
# print(nummers)
# lijst = nummers.split()
# print(lijst)

txt = file.readline()
print(txt)
txt = txt.replace(",", " ")
print(txt)
lijst = txt.split()
print(lijst)

for i in range(len(lijst)):
    lijst[i] = int(lijst[i])

print(lijst)

file.close()