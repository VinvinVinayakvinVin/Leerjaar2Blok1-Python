# -*-coding:utf-8 -*-
'''
@File    :   Opgave 9.2 Deel 4 (shorts).py
@Time    :   2022/11/13 13:34:24
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

# Short import statement:
from math import pi
print(pi)

# Short if statement:
x = 10
print(x if x > 100 else -x)
# print(x) if x > 100 else print(-x)

# Andere manier van short if statement:
x = 10 if x > 100 else 101
print(x)

# Shorts for list comprehension:
lijst = [i**2 for i in range(0, 10+1)]
print(lijst)