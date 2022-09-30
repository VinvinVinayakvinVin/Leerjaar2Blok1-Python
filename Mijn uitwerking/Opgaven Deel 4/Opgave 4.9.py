# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.9.py
@Time    :   2022/09/30 14:21:13
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
** Schrijf een functie met twee parameters, a en b van het type int. De functie bepaald of a deelbaar is door b.
De return waarde van de functie moet een boolean zijn. Kies een geschikte naam voor je functie en voorkom overbodige code.
Zie par 6.4 voor tips.

Hint: Gebruik %.
'''

# a = int(input("Type een geheel getal in voor a: "))
# b = int(input("Type een geheel getal in voor b: "))

# def ab(a, b):
#     """Functie bekijkt of a deelbaar is door b."""
#     isDividable = True
#     if a % b == 0:      # Als rest gelijk is aan 0, dan is het deelbaar.
#         isDividable = True
#     else:
#         isDividable = False
    
#     return isDividable

# print(ab(a,b))


'''
# Uitwerking:

def deelbaar(a, b):
    return a%b == 0  #als de restwaarde van a/b gelijk is aan 0

print(deelbaar(10, 3))


# Output:

# False
'''

def deelbaar(a, b):
    return a % b == 0

print(deelbaar(10, 2))