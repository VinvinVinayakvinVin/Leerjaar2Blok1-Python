# -*-coding:utf-8 -*-
'''
@File    :   Opgave 9.2 Deel 3.py
@Time    :   2022/11/13 12:55:55
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

# Hieronder uittesten om het aantal woorden te tellen van een txt string, die geen verboden string bevat:
def avoid(woord, char):
    """
    check if words does not contain a forbidden string.

    Parameters
    ----------
    woord: str
    char: str

    Returns
    -------
    result: boolean
    """

    result = True

    for letter in woord:
        for verbodenletter in char:
            if letter == verbodenletter:
                result = False
                break
    
    return result

txt = """appel
banaan
peer
sinaasappel
zeer
schrift
pencil
"""

teller = 0
for woord in txt.split():
    if avoid(woord.strip(), "ale"):
        teller += 1

print(teller)