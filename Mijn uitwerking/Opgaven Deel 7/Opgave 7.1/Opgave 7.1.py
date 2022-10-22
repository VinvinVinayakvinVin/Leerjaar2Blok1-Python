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

from regex import P

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
file = open("Tolkien.txt")
myfile = file.read()

print(file.readlines())

file.close()