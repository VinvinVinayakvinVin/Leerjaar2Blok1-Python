# -*-coding:utf-8 -*-
'''
@File    :   Opgave 7.4.py
@Time    :   2022/11/07 09:01:32
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
4. Opgave 9.3 uit het boek.
*** (LEUK) Write a function named avoids 
that takes a word and a string of 
forbidden letters, 
and that returns True if the word doesn’t 
use any of the forbidden letters.

Write a program that prompts the user to 
enter a string of forbidden letters and 
then prints the number of words 
(uit words.txt) that don’t contain 
any of them.
'''

import os


def avoids(woord, char):
    """
    Functie dat bekijkt een woord, of die een verboden karakter (karakter ➡️ letter) bevat.

    Parameters
    ----------
    woord: string
    char: string

    Returns
    -------
    not bevat_letter: boolean
    """

    bevat_letter = False

    # ⬇️ deze niet gebruiken!
    # if char in woord:
    #     bevat_letter = True
    # ⬆️ deze niet gebruiken!

    # ⬇️ zie waarom 'in' geen goed gebruik is voor dit opdracht!
    # fruits = ["apple", "banana", "cherry"]

    # if "b" in fruits:
    #     print("yes")
    # else:
    #     print("no")
    # ⬆️ zie waarom 'in' geen goed gebruik is voor dit opdracht!

    for letter in woord:
        for verboden_letter in char:    # let op, char kan meerdere letters bevatten, daarom neem ik verboden_letter, die pakt letter voor letter!
            if verboden_letter == letter:
                # print(woord)
                bevat_letter = True
                break   # stop de loop als het een verboden karakter heeft gevonden in het woord.

    return (False == bevat_letter)


char = input("Type een letter in voor het verboden karakter: ")

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.4\\")
file = open('words.txt')

words = file.read().split("\n")     # Dit is een lijst met woorden, waarbij elk woord een element is.
tel = 0
for woord in words:
    if avoids(woord, char):
        tel += 1

print("Er zijn " + str(tel) + " woorden die geen", f"{char} hebben in de woorden.")
file.close