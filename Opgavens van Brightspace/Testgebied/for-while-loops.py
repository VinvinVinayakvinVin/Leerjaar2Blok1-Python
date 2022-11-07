# -*-coding:utf-8 -*-
'''
@File    :   for-while-loops.py
@Time    :   2022/11/07 13:15:12
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

# for i in range(5):
#     print(i)

# i = 0
# while i < 5:
#     print(i)
#     i += 1  # i = i + 1

lijst = [2, 100, 4, 45]

def gemiddelde(lijst):
    """
    Dit berekent het gemiddelde van een lijst met getallen.

    Parameters
    ----------
    lijst: array type (met getallen als elementen)

    Returns
    -------
    gemiddelde: float type
    """

    som = 0
    n = len(lijst)

    for i in range(n):
        som += lijst[i]
    
    gemiddelde = som / n

    return gemiddelde

print(gemiddelde(lijst))


import math

print(math.pow(2,3))

print(100 // 3)
