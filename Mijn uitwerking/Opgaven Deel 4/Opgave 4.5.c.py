# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.5.c.py
@Time    :   2022/09/27 20:54:20
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
Zie opgavens in de comment van Opgaven 4.5.py, of zie hieronder:
'''

'''
c. Zie b, maar schrijf nu geen programma, 
maar een functie die hetzelfde doet (dus van een getal de absolute waarde maken) en noem die functie bijvoorbeeld absoluut.
'''

def absoluut():
    """Functie die berekent en print uit het absolute waarde van x."""
    x = int(input("Type een getal in: "))

    # if statement dat bekijkt of x een positief of negatief getal is.
    # als getal x negatief is, dan print de x maal -1.
    # anders print getal x.

    if x < 0:
        print(f"Absolute waarde van {x} is: " + str(x * -1))
    else:
        print(f"Absolute waarde van", x, "is: " + str(x))

absoluut()


# alternatieve code (van de uitwerking):
# getal = float(input('Vul een getal in: '))

# if getal < 0:
#     getal = -getal

# print('De absolute waarde met if-statement '+ str(getal))