# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.9.py
@Time    :   2022/10/21 11:14:13
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
9.¶
** Optellen

Schrijf een programma met één invoervariabele n. De uitvoer is de optelsom van: 1 + 2 + 3 + 4 + … + n.

Bijv. voor n = 1 is de uitkomst 1 en voor n = 7 is dat 28.
'''

# Methode 1:
n = int(input("Vul een geheel getal in voor n: "))
uitkomst = 0

for i in range(n):
    uitkomst += n - i

print(uitkomst)


# Methode 2:
uitkomst = 0

for i in range(n):
    uitkomst += (i + 1)

print(uitkomst)

'''
# Uitwerking:

n = int(input('Vul een geheel getal in\n'))

#maak een variabele om de som op te slaan
som = 0

for x in range(n):
    som = som + (x + 1)  #tel steeds het volgende getal bij 'som' op. Vergeet de + 1 niet omdat x begint bij 0. 

print(som)


# # Output:

# Vul een geheel getal in
# 7
# 28
'''