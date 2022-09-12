# -*-coding:utf-8 -*-
'''
@File    :   Opgave 2.5.py
@Time    :   2022/09/12 05:34:02
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
De waarde die bij input() wordt ingelezen wordt standaard gezien als tekst (string datatype), 
ook als je een getal hebt ingetypt! 
Als je wilt rekenen met getallen, 
moet je eerst de ingelezen input omzetten naar een getal met behulp van int() of float().

a. In onderstaand programma moet een getal als input opgeven worden. Dan wordt er geprint. Als je 3 intypt wat zal dan de uitkomst zijn denk je?

getal = input("Vul een getal in: ")
print(getal + getal)

Je moet dus eerst de ingelezen '3' omzetten naar een getal. Bijv. met float().

b. Waarom staat er 6.0 en niet 6?
'''

# Opd2.5.a)
# getal = input("Vul een getal in: ")     # Als je het getal 3 invult, dan komt er (een String) uit "33". <- (zonder aanhalingstekens natuurlijk)
# print(getal + getal)

#Opd2.5.b)
getal = input("Vul een getal in: ")
print(float(getal) + float(getal))      # Let op, we gebruiken float datatype, dus het uitkomst komt op een decimaal neer.

# Ik kon ook dit doen:
# getal = float(input("Vul een getal in: "))
# print(getal + getal)

'''
We zien dus, dat het 3.0 + 3.0 berekent.
Uitwerking zegt, het wordt als kommagetal uitgeprint, omdat het float gebruikt.
'''
