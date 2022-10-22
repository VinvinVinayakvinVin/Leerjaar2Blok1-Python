# -*-coding:utf-8 -*-
'''
@File    :   Opgave 7.1.py
@Time    :   2022/10/22 11:47:53
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
1.¶
Openen, lezen en printen. En sluiten [naam file].close

* a. Schrijf een programma waarin je de file Tolkien.txt opent, leest en print.

Hint: open() functie, .read() functie en print() functie gebruiken.

Let op aanhalingstekens en de .txt extensie (niet vergeten). Sluit de file op het eind weer met [naam file].close
'''

import os


# De code die ik met '#' beneden heb gezet, is belangrijk hoe ik die path heb gezet, om te begrijpen 
# (niet om code uit te voeren, het doet namelijk niks natuurlijk omdat het gecommend is).

# print("\n\n\n")
# for f in os.listdir(os.getcwd()):
#     print(f)

# os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.1\\")

# print("\n\n")
# for f in os.listdir(os.getcwd()):
#     print(f)

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.1\\")
file = open('Tolkien.txt')
myfile = file.read()
print(myfile)
file.close

# Uitwerking voor a ⬇️
'''
file = open('Tolkien.txt')
myfile = file.read()

print(myfile)

file.close



# Output:

Faithless is he that says farewell when the road darkens.  The Fellowship of the Ring
I will not say, do not weep, for not all tears are an evil.  The Fellowship of the Ring
All we have to decide is what to do with the time that is given us.  The Fellowship of the Ring
I warn you, if you bore me, I shall take my revenge.
If more of us valued food and cheer and song above hoarded gold, it would be a merrier world.
Short cuts make long delays.
Its the job thats never started as takes longest to finish.
I will not walk backward in life.
Even the smallest person can change the course of the future.
Darkness must pass / A new day will come / And when the sun shines / It will shine out the clearer
Courage is found in unlikely places
<function TextIOWrapper.close()>
'''


# Opgave b
'''
* b. Schrijf een programma waarin je de file Tolkien.txt opent, elke regel inleest en in een list zet en print.

Hint: open() functie, .readlines() functie

Sluit de file op het eind weer met [naam file].close
'''

print("\n\n")
# nwpath = os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))
# print(nwpath)
# os.chdir(nwpath + "\\Mijn Uitwerking\\Opgaven Deel 7\\Opgave 7.1\\")

file = open("Tolkien.txt", "r")     # Bij default, hoef je die "r" niet erbij te zetten. Ik heb hier expliciet erbij gezet.
# print(file.readline(), end="")
# print(file.readline())
print(file.readlines())
file.close()



# Uitwerking voor b ⬇️
'''
file = open('Tolkien.txt')
myfile = file.readlines()

print(myfile)

file.close



# # Output:

# ['Faithless is he that says farewell when the road darkens.  The Fellowship of the Ring\n', 'I will not say, do not weep, for not all tears are an evil.  The Fellowship of the Ring\n', 'All we have to decide is what to do with the time that is given us.  The Fellowship of the Ring\n', 'I warn you, if you bore me, I shall take my revenge.\n', 'If more of us valued food and cheer and song above hoarded gold, it would be a merrier world.\n', 'Short cuts make long delays.\n', 'Its the job thats never started as takes longest to finish.\n', 'I will not walk backward in life.\n', 'Even the smallest person can change the course of the future.\n', 'Darkness must pass / A new day will come / And when the sun shines / It will shine out the clearer\n', 'Courage is found in unlikely places']
# <function TextIOWrapper.close()>
'''


# Opgave c
'''
* c. Schrijf een programma waarin je de file Tolkien.txt opent en alleen de eerste vijf regels inleest en print.

Hint: for-loop. Sluit de file op het eind weer met [naam file].close
'''

print("\n\n\nOpgave c:\n")
file = open("Tolkien.txt")
for i in range(5):
    print(file.readline(), end="")
file.close()



# Uitwerking voor c ⬇️
'''
file = open('Tolkien.txt')

for i in range(5):
    line = file.readline()
    print(line)

file.close



# # Output:

# Faithless is he that says farewell when the road darkens.  The Fellowship of the Ring

# I will not say, do not weep, for not all tears are an evil.  The Fellowship of the Ring

# All we have to decide is what to do with the time that is given us.  The Fellowship of the Ring

# I warn you, if you bore me, I shall take my revenge.

# If more of us valued food and cheer and song above hoarded gold, it would be a merrier world.

# <function TextIOWrapper.close()>
'''


# Opgave d
'''
* d. Schrijf een programma waarin je alleen de eerste n characters van de Tolkien.txt inleest.

Hint: .readfile(n)
'''

print("\n\n\nOpgave d:\n")
n = int(input("Vul een geheel getal in voor n: "))
file = open("Tolkien.txt")
# print(file.readline(n))
print(file.read(n))             # Deze is beter, dan readline(n), deze pakt het hele bestand, i.p.v één regel tekst.
file.close()



# Uitwerking voor d ⬇️
'''
file = open('Tolkien.txt')

n = int(input('Vul een geheel getal in\n'))

myfile = file.read(n)
print(myfile)

file.close



# # Output:

# Vul een geheel getal in
# 15
# Faithless is he
# <function TextIOWrapper.close()>
'''


# Opgave e
'''
!! * e. Bij 1c zie je dat er witte regels staan tussen de regels van Tolkien.txt. 
Dat komt omdat in de tekstfile een zin steeds op een nieuwe regel staat. 
Bij het inlezen van een zin staat er bij elke zin daarom de nieuwe regel instructie \n. 
Die \n is ook duidelijk te zien in 13b. 
De \n kunnen we weghalen door de .strip() functie: 
Een regel inlezen doe je met .readline() en de \n weghalen dan met: .readline().strip().

Doe 13c nogmaals maar nu mogen er geen witte regels zijn in de uitvoer. Sluit de file op het eind weer met [naam file].close
'''

print("\n\n\nOpgave e:\n")
file = open("Tolkien.txt")

# for i in range(5):
#     print(file.readline())

for i in range(5):
    line = file.readline().split("\n")
    print(line[0])

    # Deze 3 regels onder, doet raar...
    # print(file.readline().split("'\n'"))
    # line = file.readline().split("\n")
    # print(line)

file.close()

# Uitwerking voor e ⬇️
'''
file = open('Tolkien.txt')

for i in range(5):
    line = file.readline().strip()
    print(line)
    
file.close



# # Output:

# Faithless is he that says farewell when the road darkens.  The Fellowship of the Ring
# I will not say, do not weep, for not all tears are an evil.  The Fellowship of the Ring
# All we have to decide is what to do with the time that is given us.  The Fellowship of the Ring
# I warn you, if you bore me, I shall take my revenge.
# If more of us valued food and cheer and song above hoarded gold, it would be a merrier world.
# <function TextIOWrapper.close()>
'''


# Opgave f
'''
!! * f. Er zijn meer functies die je achter zo een ingelezen regel kunt zetten. 
Je kunt bijv. alle letter UPPERCASE (hoofdletters) maken, of juist lowercase (kleine letters). 
Bijv. readline().lower() of readline().strip().lower()

Vul 13d aan met dat de uitvoer allemaal hoofdletters zijn. Sluit de file op het eind weer met [naam file].close
'''

