# -*-coding:utf-8 -*-
'''
@File    :   Opgave 7.5.b.py
@Time    :   2022/11/07 10:10:39
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
*** b. De gegevens willen we sorteren in acht lijstjes. Voor beide geslachten vier lijstjes:
Lijst met leeftijden. Lijst met lengte. Lijst met gewicht. Lijst met cijfer.

Maak deze lijstjes aan en sla de informatie per regel in de juiste lijsten op. Print daarna alle acht lijstjes uit. 
Je zult de informatie per regel dus moeten splitsen.

Hint: je zult nodig hebben, for-loops, if-else conditionals, .append(), .split() etc.
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
    
    # line.split() zorgt er voor dat de opstelling nu dit wordt: ['woord_1', 'woord_2', ..., 'woord_n']
    leeftijd = int(line.split()[2])
    lengte = int(line.split()[3])
    gewicht = int(line.split()[4])
    cijfer = int(line.split()[5])

    if line.split()[1] == "jongen":
        j_leeftijden.append(leeftijd)
        j_lengtes.append(lengte)
        j_gewichten.append(gewicht)
        j_cijfers.append(cijfer)
    else:
        m_leeftijden.append(leeftijd)
        m_lengtes.append(lengte)
        m_gewichten.append(gewicht)
        m_cijfers.append(cijfer)

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