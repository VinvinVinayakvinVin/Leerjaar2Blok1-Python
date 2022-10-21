# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.15.py
@Time    :   2022/10/21 18:13:30
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
15.¶
!! *** Taylorreeks

De e-macht is uit te drukken in een zogenaamde Taylorreeks (krijg je later dit jaar bij Calculus):

𝑒𝑥=∑∞𝑛=0𝑥𝑛𝑛!=1+𝑥+𝑥22+𝑥36+... 
Als we alleen N-termen meenemen, dan krijgen we de Ne Taylorbenadering voor de e-macht. Dus:

𝑒𝑥≈∑𝑁−1𝑛=0𝑥𝑛𝑛!=1+𝑥+𝑥22+𝑥36+...+𝑥𝑁−1(𝑁−1)! 
Schrijf een programma met invoervariabelen x en N dat de Ne Taylorbenadering voor de e-macht bepaalt en uitprint. 
Print ook de e-macht uit die je berekent met math.exp(). Zijn de verschillen groot?

Hint: Schrijf eerst een functie die de faculteit bepaalt van n. Hoe kun je n! in een for-loop bepalen?
'''

import math

x = float(input("Vul een getal in voor x: "))
n = int(input("Vul een geheel getal in voor n: "))

print(f"als x = {x}, dan is e^x = {pow(math.e, x)}")

def faculteit(n):
    """
    Dit berekent het faculteit van n.

    Parameters
    ----------
    n: integer
    
    Returns
    -------
    uitkomst: integer
    """
    uitkomst = 1
    for i in range(1, n+1):
        uitkomst *= i
    return uitkomst

approx_ex = 0
for i in range(0, n):
    approx_ex = approx_ex + (pow(x, i) / faculteit(i))

print(f"als x = {x}, dan is e^x ongeveer {approx_ex}")


'''
# Uitwerking:

import math

def faculteit(n):
    """
    Bereken n faculteit
    
    Parameters
    ----------
    n: int 
       
    Returns
    -------
    int
        n faculteit
    """
    facul = 1
    
    if n == 0:
        return 1
    else:
        for i in range(n):
            facul = facul * (i + 1)  
        return facul                

x = float(input('Vul een geheel getal in\n'))
n = int(input('Vul een geheel getal in\n'))

som = 0

for i in range(n):    
    som = som + math.pow(x, i) / faculteit(i)

print('Benadering   ' + str(som))
print('Uitkomst math ' + str(math.exp(x))) 


# # Output:

# Vul een geheel getal in
# 1
# Vul een geheel getal in
# 6
# Benadering   2.7166666666666663
# Uitkomst math 2.718281828459045
'''

'''
# Uitwerking over faculteit berekenen:

# Alternatief voor faculteit (korter)

def faculteit(n):
    facul = 1
    for i in range(1, n + 1):
        facul = facul * (i + 1)  
    return facul 
'''