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