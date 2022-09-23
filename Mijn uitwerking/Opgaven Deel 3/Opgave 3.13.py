# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.13.py
@Time    :   2022/09/23 21:47:24
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* a. Maak een functie "constanten" aan die de waarden van  π ,  𝑒  en  τ  (tau) onder elkaar uitprint.
Hint: gebruik de math module
'''

from math import *


def constanten():      # functie definiëren.
    """Functie dat print de waarden, π, e en τ"""

    print(pi)
    print(e)
    print(tau)

constanten()    # functie roepen

'''
* b. En afrond op drie decimalen.
Hint: opgave 3.11
'''

def constanten_afgerond():
    """Zelfde als functie van constanten, 
        maar de waarden die uitgeprint worden zijn nu op 3 decimalen afgerond."""

    print(f"{pi:.3f}")
    print(round(e, 3))
    print(f"{tau:.3f}")

constanten_afgerond()

'''
Uitwerking:

# import math

def constanten():
    """Print de constanten pi, e en tau, afgerond op 3 decimalen."""
    
    print(round(math.pi, 3))
    print(round(math.e, 3))
    print(round(math.tau, 3))
    
constanten()

# output:
# 3.142
# 2.718
# 6.283
'''