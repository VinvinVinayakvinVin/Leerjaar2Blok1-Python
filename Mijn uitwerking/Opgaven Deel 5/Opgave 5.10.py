# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.10.py
@Time    :   2022/10/21 11:23:05
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
10.¶
!! *** Rij van Fibonacci

De rij van Fibonacci bestaat uit de getallen: 1, 1, 2, 3, 5, 8, 13, 21, 34, etc. Ofwel element  𝑎𝑛=𝑎𝑛−2+𝑎𝑛−1 , waarbij  𝑎1=𝑎2=1 .
Schrijf een programma dat de n-de term van de rij van Fibonacci uitprint.

De zevende term is bijvoorbeeld 13. Je invoervariabele is n.
'''

# n = int(input("Vul een geheel getal in voor n: "))
# a = 1
# b = 1

# # Fibonacci code:

# print(a)
# print(b)

# for i in range(n-2):
#     uitkomst = a + b
#     print(uitkomst)
#     a = b
#     b = uitkomst

# ⬆️ Ik heb de hele lijst laten uitprinten, maar ik moet ÉÉN term uitprinten!

'''
# Uitwerking:

#Variabelen voor de eerste 2 termen
a1 = 1
a2 = 1

n = int(input('Vul een geheel getal in\n'))

for x in range(3, n+1):
    an = a1 + a2 #de n-de term is de som van de 2 voorgaande termen
    #schuif de eerste 2 termen nu een plek verder voor de volgende loop
    #Nog onduidelijk? Schrijf op papier uit hoe a1, a2 en an veranderen voor bv 4 loops
    a1 = a2 
    a2 = an

if n == 1 or n == 2:
    print(1)
else:
    print(an)


# # Output:

# Vul een geheel getal in
# 7
# 13
'''

# Mijn tweede poging ⬇️:

n = int(input("Vul een geheel getal in voor n: "))
a = 1
b = 1

for i in range(3, n+1):
    uitkomst = a + b
    a = b
    b = uitkomst

if n == 1 or n == 2:
    print(1)
else:
    print(uitkomst)