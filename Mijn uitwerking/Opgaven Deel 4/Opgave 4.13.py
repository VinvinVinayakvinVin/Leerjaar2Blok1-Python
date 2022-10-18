# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.13.py
@Time    :   2022/10/12 15:38:37
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
4.13¶
*** Abc-formule

Maak deze opgave in Spyder. Want in Spyder maak je je eindopdracht. Dus oefen er nu alvast mee.

Schrijf een programma dat als invoer drie variabelen, a, b en c heeft en de oplossing geeft van de kwadratische vergelijking:

𝑎𝑥2+𝑏𝑥+𝑐=0 
Je moet hiervoor de ABC-formule in Python programmeren. Let er wel op dat:

Er soms geen oplossingen zijn
Er soms maar 1 oplossing is
Of dat het een lineaire oplossing is als a = 0
M.a.w. als a = 0 moet je programma nog steeds de juiste oplossing voor x geven (maar dan dus niet m.b.v. de ABC-formule).

Als de discriminant kleiner is dan 0, dan moet je programma als uitvoer geven dat er geen oplossingen zijn.

Als de discriminant 0 is, dan moet je programma als uitvoer maar één oplossing geven.

Hint: In deze opgave moet je dus gebruik maken van if, elif, else.
'''

# a = float(input("Geeft een waarde voor a aan: "))
# b = float(input("Geeft een waarde voor b aan: "))
# c = float(input("Geeft een waarde voor c aan: "))

# discrimant = b ** 2 - 4 * a * c

# # If statement dat lost de oplossing op van een kwadratische uitdrukking die gelijk aan 0 is m.b.v abc formule.
# if discrimant < 0:
#     print("Geen oplossing...")
# elif discrimant == 0:
#     print("x =", (-b / (2 * a)))
# else:
#     print("x1 =", (-b + discrimant ** 2) / (2 * a))
#     print("x2 =", (-b - discrimant ** 2) / (2 * a))



'''
# Uitwerking:

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 12:37:43 2021

@author: dilrx
"""


def discriminant(a, b, c):
    """
    Berekent de discriminant van een kwadratische vergelijking.

    Parameters
    ----------
    a, b, c : float
        De coefficienten van een kwadratische vergelijking.

    Returns
    -------
    float
        De discriminant van deze vergelijking..

    """
    return b*b - 4*a*c

def vergelijking(a, b, c):
    return f"{a}x^2 {b:+}x {c:+} = 0"

def tekst_oplossingen(s, x1, x2):
    return f"""
    De vergelijking
      {s}
    heeft twee oplossingen:
    x1 = {x1}, en
    x2 = {x2}
    """
    
def abc_formule(a, b, c):
    s = vergelijking(a, b, c)
    disc = discriminant(a, b, c)
    # TO DO -- controleren of de
    # discriminant positief is
    x1 = (-b + disc**(1/2))/(2*a)
    x2 = (-b - disc**(1/2))/(2*a)
    print(tekst_oplossingen(s, x1, x2))


a = float(input('Geef a: '))
b = float(input('Geef b: '))
c = float(input('Geef c: '))


#4 mogelijkheden: a = 0 (lineaire vergelijking), discriminant < 0, discriminant > 0 en discriminant = 0
if a == 0:
   oplossing1 =  -c/b
   print('De oplossing van de vergelijking is: ' + str(oplossing1))
elif discriminant(a, b, c) < 0:
    print('Er zijn geen oplossingen')
elif discriminant(a, b, c) > 0:
    abc_formule(1, 2, -5)
else:
    oplossing1 = -b/(2*a)
    print ('De enige oplossing is : ' + str(oplossing1))
'''

# # Wat doet die f"{test:+}"? Waarbij test een variabel naam is.

# test = 4012312.12003
# print(f"{test:+}")
# print(f"{test:_}")
# print(f"{test:,}")
# print(f"{test:+,}")
# print(f"{test:+,}".replace(',', 'aaaa'))    # Ik ging hier testen hoe die replace function werkt bij string value.

'''
Mijn tweede poging om dit programma te bouwen!
'''

a = float(input("Vul waarde voor a: "))
b = float(input("Vul waarde voor b: "))
c = float(input("Vul waarde voor c: "))

def discriminant(a, b, c):
    """
    Dit berekent het discriminant van de abc-formule.
    """
    return pow(b, 2) - 4 * a * c

def abc_formule(a, b, c):
    """
    Dit berekent de twee oplossingen uit voor x m.b.v. de abc-formule.
    """
    print((-b + discriminant(a, b, c) ** (1/2)) / (2 * a))
    print((-b - discriminant(a, b, c) ** (1/2)) / (2 * a))


if a == 0:
    print(f"x = {-c/b}")
elif discriminant(a, b, c) < 0:
    print("Er zijn geen oplossingen!")
elif discriminant(a, b, c) == 0:
    print(f"Oplossing is: x = {-b/2}")
else:
    print("Er zijn twee oplossingen!")
    abc_formule(a, b, c)