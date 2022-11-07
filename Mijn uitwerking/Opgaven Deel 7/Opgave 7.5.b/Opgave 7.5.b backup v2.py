# -*-coding:utf-8 -*-
'''
@File    :   Opgave 7.5.b backup v2.py
@Time    :   2022/11/07 11:07:23
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

import os

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.5.b\\")
file = open("Klas.txt")
file.readline() # skip eerste line.

# j voor jongens
j_leeftijden = []
j_lengtes = []
j_gewichten = []
j_cijfers = []

# m voor meisjes
m_leeftijden = []
m_lengtes = []
m_gewichten = []
m_cijfers = []

lines = file.readlines()    # lines is nu zo opgesteld: ['zin_1', 'zin_2', ..., 'zin_n']
for line in lines:
    # for woord in line.split():  # line.split() is nu zo opgesteld ['woord_1', 'woord_2', ..., 'woord_n']
        # print(woord)
    
    # leeftijd = int(line.split()[2])
    # lengte = int(line.split()[3])
    # gewicht = int(line.split()[4])
    # cijfer = int(line.split()[5])

    if line.split()[1] == "jongen":
        j_leeftijden.append(int(line.split()[2]))
        j_lengtes.append(int(line.split()[3]))
        j_gewichten.append(int(line.split()[4]))
        j_cijfers.append(int(line.split()[5]))
    else:
        m_leeftijden.append(int(line.split()[2]))
        m_lengtes.append(int(line.split()[3]))
        m_gewichten.append(int(line.split()[4]))
        m_cijfers.append(int(line.split()[5]))

print("lijsten van jongens:")
print("j_leeftijden:", j_leeftijden)
print("j_lengtes:", j_lengtes)
print("j_gewichten:", j_gewichten)
print("j_cijfers:", j_cijfers, end="\n\n")

print("lijsten van meisjes:")
print("m_leeftijden:", m_leeftijden)
print("m_lengtes:", m_lengtes)
print("m_gewichten:", m_gewichten)
print("m_cijfers:", m_cijfers)

file.close()


# regel = "Kunnen we dit opbreken naar een lijst met deze woorden?"
# print(regel.split())