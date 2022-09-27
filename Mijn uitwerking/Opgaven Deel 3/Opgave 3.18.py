# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.18.py
@Time    :   2022/09/27 19:13:03
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
** Onderstaand programma moet 7x ‘Hallo’ onder elkaar printen, echter er wordt ook ‘None’ geprint.
'''

'''
import math

def printen(x):
    """print Hallo x-keer onder elkaar uit"""
    
    return print('Hallo\n' * x)

print(printen(7))
'''

'''
Hoe kan dat? Waar ligt dit aan en hoe kun je dit oplossen? Run bovenstaand programma dus ook.
'''

import math

def printen(x):
    """print Hallo x-keer onder elkaar uit"""
    
    return print('Hallo\n' * x)

print(printen(7))

# Komt omdat het datatype van print ook wordt geprint.
# print is een functie die tekst in de console/terminal uitprint.
# Het is niet zo'n datatype waarbij je een int/float/String/double/boolean etc retourneert.

'''
# uitwerking: 

import math

def printen(x):
    """print Hallo x-keer onder elkaar uit"""
    
    return print('Hallo\n' * x)

print(printen(7))

#De functie geeft nu geen waarde terug maar laat alleen de uitvoer van de print functie zien. 
#Functies zonder return statement of een return zonder een argument (dat speelt nu), krijgen
#een impliciete return None

#verbeterde versie
def printen(x):
    """print Hallo x-keer onder elkaar uit"""
    
    print('Hallo\n' * x)

printen(7)

# output:

# Hallo
# Hallo
# Hallo
# Hallo
# Hallo
# Hallo
# Hallo

# None
# Hallo
# Hallo
# Hallo
# Hallo
# Hallo
# Hallo
# Hallo
'''

'''
Antwoord in mijn woorden:

Als je een functie zonder iets returnt print, dan krijg je in je Terminal/Console "None" uitgeprint.
'''

'''
⬇️ code om te testen wat er gebeurt bij verschillende situaties (onderwerp 'geen return')
'''

# import math

# def printen(x):
#     """print Hallo x-keer onder elkaar uit"""
    
#     return print('Hallo\n' * x)

# print(printen(7))

# def hoi():                  # Ik heb de documentatie niet gezet, omdat het onnodig werk is voor mij.
#     return                  # Dit is toch om te testen hoe die functies zonder return werkt.

# def hoi_1():
#     print(1)

# def hoi_2():
#     return print(2)

# print(hoi())
# print(hoi_1())
# print(hoi_2())