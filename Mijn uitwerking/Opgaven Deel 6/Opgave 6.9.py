# -*-coding:utf-8 -*-
'''
@File    :   Opgave 6.9.py
@Time    :   2022/10/22 10:25:07
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
9.ΒΆ
*** Nested for-loops I: Sommaties

Schrijf een programma dat de volgende dubbele som berekent:

a.  β20π=1β20π=11 
b.  β20π=1β20π=1(π+π) 
c.  βππ=1βππ=112ππ  met  π  als input.
'''

# Opgave a:

from msilib.schema import UIText


uitkomst_a = 0

for i in range(1, 21):
    for j in range(1, 21):
        uitkomst_a += 1

print(uitkomst_a)

# Opgave b:

uitkomst_b = 0

for i in range(1, 21):
    for j in range(1, 21):
        uitkomst_b += (i + j)

print(uitkomst_b)

# Opgave c:

n = int(input("Vul een positief, geheel getal in voor n: "))

uitkomst_c = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        uitkomst_c += (1 / 2 ** (i * j))

print(uitkomst_c)



# Uitwerking voor a, b en c:
'''
#a
som = 0

for i in range(1, 21):
    for j in range(1, 21):
        som = som + 1

print(som)



# # Output:

# 400
'''

'''
#b
som = 0

for i in range(1, 21):
    for j in range(1, 21):
        som = som + i + j

print(som)



# Output:

8400
'''

'''
#c
import math

n = int(input('Vul geheel getal in\n'))

som = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        som = som + 1/math.pow(2, i * j)

print(som)



# # Output:

# Vul geheel getal in
# 20
# 1.6066932450660523
'''