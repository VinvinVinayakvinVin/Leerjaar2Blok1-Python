# -*-coding:utf-8 -*-
'''
@File    :   test.py
@Time    :   2022/10/22 11:32:22
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   Vreemde decimalen in de lijst, wanneer je grote n, of m waarde aangeeft.
                Neem bijvoorbeeld n, m = 10.
'''

n = int(input("Het aantal balkjes op de x-as: "))
m = int(input("Het aantal balkjes op de y-as: "))

x_i = []
y_j = []

diepte = (4 - 2) / n
breedte = (6 - 2) / m

# Alle x'tjes verzamelen
for i in range(0, n):
    x_i.append(2 + i * diepte)

# Alle y'tjes verzamelen
for j in range(0, m):
    y_j.append(2 + j * breedte)

print(x_i)
print(y_j)