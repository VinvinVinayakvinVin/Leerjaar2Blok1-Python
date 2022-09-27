# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.17.py
@Time    :   2022/09/27 19:00:18
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
!! * Variabelen in een functie zijn local:
    ze hebben alleen betekenis in de functie zelf.
    Buiten de functie bestaan die variabelen niet.
Zie onderstaand programma.
'''

'''
import math

def printen():
    """print Hallo x-keer onder elkaar uit"""
    x = 5
    return 'Hallo\n' * x

print(printen()) 

print(x) 
'''

'''
Wat zal de output zijn als je dit programma draait? Run de code. Kun je de uitkomst verklaren?
'''

# import math

# def printen():
#     """print Hallo x-keer onder elkaar uit"""
#     x = 5
#     return 'Hallo\n' * x

# print(printen()) 

# print(x)

'''
Dit geeft een error:

NameError: name 'x' is not defined
'''

'''
Verbeterde versie hieronder ⬇️
'''

import math

x = 10

def printen():
    """print Hallo x-keer onder elkaar uit"""
    x = 5
    return 'Hallo\n' * x

print(printen()) 

print(x) 

# of:

import math

x = float(input("Type een getal in: "))

def printen():
    """print Hallo x-keer onder elkaar uit"""
    x = 5
    return 'Hallo\n' * x    # x (locale x) neemt het getal 5 en niet van de globale x waarde.

print(printen()) 

print(x)


'''
# Uitwerking:

import math

def printen():
    """print Hallo x-keer onder elkaar uit"""
    x = 5
    return 'Hallo\n' * x

print(printen()) #roept de functie 'printen' aan

print(x) #x = 5 bestaat alleen in de functie 'printen' en kan niet daarbuiten gebruikt worden. 
#Als er hier voor x een waarde wordt uitgeprint, komt dat omdat er in de opgaven hierboven een 
#waarde is gegeven aan x (opgave 3.12).

# output: 

Hallo
Hallo
Hallo
Hallo
Hallo

10000.0
'''