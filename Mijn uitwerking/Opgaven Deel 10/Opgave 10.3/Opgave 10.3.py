# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.3.py
@Time    :   2022/11/13 14:49:46
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
3. Lees par 8.6: Searching¶
!! ** Schrijf een programma dat van elk element in de volgende lijst:

emailAdressen = ['Happy@gmail.com', 'Vrolijk@gmail.com', 'Frohlichgmail.com'] bepaald op welke plek 
het @ staat (dus het hoeveelste character).

Ja, in het derde element ontbreekt de @, je programma moet hier mee om kunnen gaan.

Hint: Schrijf eerst een functie waarmee je een karakter opzoekt in een string. 
De input is dan een string en een karakter en de output is de index van het karakter in de string.
'''

emailAdressen = ['Happy@gmail.com', 'Vrolijk@gmail.com', 'Frohlichgmail.com']

def findIndex(txt, char):
    """
    Dit geeft het positie aan, waar een bepaalde char zit in een txt.

    Parameters
    ----------
    txt: string
    char: string

    Returns
    -------
    indexNum = int
    """

    indexNum = -1

    if char in txt:
        indexNum = 0
        for letter in txt:
            indexNum += 1
            if letter == char:
                break
            

    return indexNum

for email in emailAdressen:
    if findIndex(email, "@") != -1:
        print("Index nummer van " + email + "is: " + str(findIndex(email, "@")))
    else:
        print("Index nummer van " + email + "is er helaas niet.")



# Uitwerking:
'''
emailAdressen = ['Happy@gmail.com', 'Vrolijk@gmail.com', 'Frohlichgmail.com']

def find(woord, symbool):
    """
    Zoekt een karakter op in een string.
    
    Parameters
    ----------
    woord: string
           de string waarin wordt gezocht naar een speciaal karakter
    symbool: string
           het karaker om op te zoeken in 'woord'
       
    Returns
    -------
    index: int
        index van de string waar het karakter zit
        -1 als karakter niet voorkomt in string
    """
    index = 0
    
    while index < len(woord):
        if woord[index] == symbool:
            return index
        index = index + 1
        
    return -1

for woord in emailAdressen:
    index = find(woord, '@')
    if index == -1:
        print('@ zit niet in het emailadres.')
    else:
        print('Character nummer', index + 1)



# Output:

Character nummer 6
Character nummer 8
@ zit niet in het emailadres.
'''