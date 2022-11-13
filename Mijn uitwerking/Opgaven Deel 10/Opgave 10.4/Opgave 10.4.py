# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.4.py
@Time    :   2022/11/13 17:39:03
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
!! ** 4. Lees par 8.7: Counting¶
a. Schrijf een programma dat bepaald hoeveel e's er in de langste plaatsnaam van Nederland zitten:

Westerhaar-Vriezenveensewijk

b. Bepaal hoevel letters/tekens deze plaatsnaam heeft.

c. Bepaal hoeveel klinkers (a, e, i, o, u en y) er in de volgende zin zitten: 'Ik wou dat de afwas af was'

d. Bepaal hoeveel klinkers er in het tekstbestand quotes.txt zitten (zie Brightspace) en zet dus eerst de file in de juiste map en lees daarna in.
'''

# a
txt = 'Westerhaar-Vriezenveensewijk'
teller = 0
for char in txt:
    if char == 'e':
        teller += 1

print("a: ", teller)



# b
print("b", len(txt))



# c
txt = 'Ik wou dat de afwas af was'
teller = 0
for char in txt.lower():
    if char == 'e' or char == 'a' or char == 'i' or char == 'o' or char == 'u' or char == 'y':
        teller += 1

print("c", teller)



# d
import os

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 10\\Opgave 10.4\\")
file = open("quotes.txt")

teller = 0
for line in file.readlines():
    for char in line.strip().lower():
        if char == 'e' or char == 'a' or char == 'i' or char == 'o' or char == 'u' or char == 'y':
            teller += 1

print("d: " + str(teller))

file.close()



# Uitwerking:
'''
plaatsnaam = 'Westerhaar-Vriezenveensewijk'

# a.
teller = 0

for letter in plaatsnaam:
    if letter == 'e':
        teller = teller + 1
print(teller)

# # Output:
# 7



# b.
print(len(plaatsnaam))



# # Output
# 28



# c.
zin = 'Ik wou dat de afwas af was'
teller = 0

for letter in zin.lower(): # Wat gebeurt er als je .lower() er niet bij zet? 
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y':
        teller = teller + 1
        
print(teller)



# # Output:
# 9



# d.
file = open('quotes.txt')
myFile = file.readlines()

teller = 0

for zin in myFile:    
    for letter in zin.lower(): 
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y':
            teller = teller + 1
            
print(teller)



# # Output
# 71
'''