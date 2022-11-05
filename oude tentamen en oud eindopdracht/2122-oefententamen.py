# -*-coding:utf-8 -*-
'''
@File    :   2122-oefententamen.py
@Time    :   2022/11/05 11:52:25
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

# A = [[2,3],
#      [4,5]]

# B = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 0, 1, 2],
#      [3, 4, 5, 6]]

# def trace(A):
#     som = 0
#     for i in range(len(A)):
#         for j in range(len(A[i])):
#             if i == j:
#                 som += A[i][j]
#     return som


# # Uitwerking 1
# def trace(M):
#     return sum(M[i][i] for i in range(len(M)))

# print(trace(A))
# print(trace(B))

# print(sum(A[i][i] for i in range(len(A))))



# Correcte functie
import math

def maximum(xs):   # "def" ontbrak, de naam x was dubbel gebruikt, omdat de invoer een lijst is maken we het meervoud (xs)
    m = xs[0]      # anders werkt de functie niet voor een lijst van negatieve getallen
    for x in xs:   # lijst heet nu xs
        if x > m:  # ":" ontbrak en we berekenen het maximum, dus we zoeken elementen "groter dan" het laatst gevonden max
            m = x  # inspringen
    return m       # een functie heeft een returnwaarde

xs = [2, 100, 101, -10000, 10.1]
print(maximum(xs))