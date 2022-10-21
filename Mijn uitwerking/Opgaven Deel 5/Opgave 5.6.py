# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.6.py
@Time    :   2022/10/20 15:45:46
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
6.¶
* a. Schrijf een programma dat de getallen 1 t/m 25 onder elkaar uitprint (mbv een for-loop).
'''

for i in range(1, 26):  # 1 inclusief, 26 exclusief => 25 inclusief.
    print(i)



'''
* b. Schrijf een programma dat de getallen 1 t/m n onder elkaar uitprint. De invoer is de variabele n .
'''

n = int(input("Vul een geheel getal in voor n, waarbij n groter dan n is: "))
if n > 1:
    for i in range(1, n+1):  # 1 inclusief, 26 exclusief => 25 inclusief.
        print(i)
else:
    print("Je hebt een waarde ingevuld die kleiner gelijk aan 1 is.")



'''
** c. Schrijf een programma dat de getallen 1 t/m n onder elkaar uitprint, maar alleen de oneven getallen. De invoer is de variabele n .
Hint: zie opgave 4.4 van Opgaven Deel 4 en dan nog iets met if?
'''

n = int(input("Vul een geheel getal in voor n, waarbij n groter dan n is: "))
if n > 1:
    for i in range(1, n+1):  # 1 inclusief, 26 exclusief => 25 inclusief.
        if i % 2 == 1:
            print(i)
        else:
            pass
else:
    print("Je hebt een waarde ingevuld die kleiner gelijk aan 1 is.")



'''
** d. Als c, maar nu alleen de even getallen.
'''

n = int(input("Vul een geheel getal in voor n, waarbij n groter dan n is: "))
if n > 1:
    for i in range(1, n+1):  # 1 inclusief, 26 exclusief => 25 inclusief.
        if i % 2 == 0:
            print(i)
        else:                # dit else statement kan gewoon weg, omdat het toch niks doet.
            pass
else:
    print("Je hebt een waarde ingevuld die kleiner gelijk aan 1 is.")



'''
# Uitwerking a:
#a
for i in range(25):
    print(i+1) #i loopt van 0 t/m 24 dus tel 1 erbij op

# # output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25

#a kan ook met
for i in range(1, 26):
    print(i)
'''

'''
# Uitwerking b:
#b
n = int(input('Vul een geheel getal in\n'))

for i in range(n):
    print(i+1)
'''

'''
# Uitwerking c:
#c
n = int(input('Vul een geheel getal in\n'))

for i in range(n):
    if (i+1)%2 == 1: #als getal/2 een restwaarde heeft van 1, dan is het getal oneven
        print(i+1)
'''

'''
# Uitwerking d:
#d
n = int(input('Vul een geheel getal in\n'))

for i in range(n):
    if (i+1)%2 == 0: #restwaarde = 0, dan even
        print(i+1)
'''