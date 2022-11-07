# -*-coding:utf-8 -*-
'''
@File    :   Uitwerking 7.4.py
@Time    :   2022/11/07 09:30:24
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

import os


def avoids(woord, verboden):
    """
    Bepaalt of er verboden letters voorkomen in een woord.

    Parameters
    ----------
    woord: string
    het woord dat gecontroleerd wordt op verboden letters
    
    verboden: string
    een string met verboden letters
        
    Returns
    -------
    boolean
        True als geen van de verboden letters voorkomen in het woord
        False als er wel verboden letters voorkomen in het woord
    """
    resultaat = True
    
    for letter in woord: #loop over de letters in het woord
        for verboden_letter in verboden: # loop over de verboden letters
            if letter == verboden_letter:
                resultaat = False
                break #Als een verboden letter voorkomt, kan de loop stoppen
                
    return resultaat

verboden_letters = input('Geef de verboden letters op: ')


os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.4\\")
file = open('words.txt')
lines = file.readlines()

aantal_woorden = 0

for line in lines:
    if avoids(line, verboden_letters):
        aantal_woorden += 1
        
print(aantal_woorden)