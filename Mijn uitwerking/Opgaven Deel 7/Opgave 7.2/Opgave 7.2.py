# -*-coding:utf-8 -*-
'''
@File    :   Opgave 7.2.py
@Time    :   2022/10/23 09:19:50
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
2. Opgave 9.1 uit het boek.¶
** Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).

words.txt is van Brightspace te downloaden.
'''

import os


os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.2\\")
file = open("words.txt")

lines = file.readlines()
for word in lines:
    if len(word) > 20:
        print(word.strip())

file.close()

# Uitwerking:
'''
file = open('words.txt')
lines = file.readlines()

for line in lines:
    if len(line) > 20:
        print(line)
        
file.close()



# # Output:

# counterdemonstration

# counterdemonstrations

# counterdemonstrators

# hyperaggressivenesses

# hypersensitivenesses

# microminiaturization

# microminiaturizations

# representativenesses
'''