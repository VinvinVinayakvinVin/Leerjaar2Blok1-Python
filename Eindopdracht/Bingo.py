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

bingokaart = []
temp_lijst = []

for line in file.readlines():
    element = [line.strip()][0].split()
    # if line.split() != []:
    #     temp_lijst.append(int(element))
    if element != []:               # element is hierbij een lijst!?!?!!? vb -> element = ['22', '13', '17', '11', '0']
        print(element)
        for i in element:
            temp_lijst.append(int(i))
        bingokaart.append(temp_lijst)
        temp_lijst = []

print(bingokaart)

file.close()
