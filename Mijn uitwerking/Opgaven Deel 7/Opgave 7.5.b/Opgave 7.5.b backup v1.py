# -*-coding:utf-8 -*-
'''
@File    :   Opgave 7.5.b backup v1.py
@Time    :   2022/11/07 10:31:27
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

# file = open("Klas.txt")
# lines = file.read()
# print("\n\n", lines)
# file.close()

import os

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.5.b\\")
file = open("Klas.txt")
lines = file.read().split()

Namen = []
Geslachten = []
Leeftijden = []
Lengtes = []
Gewichten = []
Cijfers = []

i = 0
for line in lines:
    i += 1
    if i > 6:
        if i % 6 == 1:
            Namen.append(line)
        elif i % 6 == 2:
            Geslachten.append(line)
        elif i % 6 == 3:
            Leeftijden.append(line)
        elif i % 6 == 4:
            Lengtes.append(line)
        elif i % 6 == 5:
            Gewichten.append(line)
        else:
            Cijfers.append(line)

print(Namen)
print("\n\n", Geslachten)
print("\n\n", Leeftijden)
print("\n\n", Lengtes)
print("\n\n", Gewichten)
print("\n\n", Cijfers)
file.close()