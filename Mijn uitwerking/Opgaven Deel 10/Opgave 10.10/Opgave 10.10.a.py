# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.10.py
@Time    :   2022/11/13 19:13:55
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
10.
Een matrix (nested list) zelf maken met input.

* a. Maak een matrix met twee rijen en twee kolommen. De waarden van de matrix moeten ingevuld worden via input. Print de matrix uit.

!! ** b. Zoals a, maar nu moet je eerst via input opgeven hoeveel rijen en kolommen de matrix moet hebben. Print de matrix uit.

* c. Zoals b, maar nu moet de input getallen zijn en de elementen van de matrix de kwadraten van de invoer.
'''

######################################################################################### opd10.10.a:

# len_lijst1 = int(input("Vul een geheel getal in voor de lengte voor lijst 1: "))
# len_lijst2 = int(input("Vul een geheel getal in voor de lengte voor lijst 2: "))
# len_lijst3 = int(input("Vul een geheel getal in voor de lengte voor lijst 3: "))
# len_lijst4 = int(input("Vul een geheel getal in voor de lengte voor lijst 4: "))
# len_lijst = [len_lijst1, len_lijst2, len_lijst3, len_lijst4]

# lijst = [[],[]]
# temp_lijst = []

# for i in range(len(len_lijst)):
#     for j in range(len_lijst[i]):
#         element = int(input("Vul een leuk geheel getal in: "))
#         temp_lijst.append(element)
#     if i == 0 or i == 1:
#         lijst[0].append(temp_lijst)
#     else:
#         lijst[1].append(temp_lijst)
#     temp_lijst = []

# print(lijst)

# Fout 😂
# Ik heb het driedimensionaal gemaakt.
# De twee rijen en twee kolommen bedoelen ze met dit:
# 2 rijen, als 2 elementen in één matrix.
# 2 kolommen, als 2 matrices.
#vb:
# [[1, 2],
#  [3, 4]]
#vb2:
# [['2', '4'], ['6', '8']]



######################################################################################### opd10.10.a opnieuw (tweede poging):

len_lijst1 = int(input("Vul een geheel getal in voor de lengte voor lijst 1: "))
len_lijst2 = int(input("Vul een geheel getal in voor de lengte voor lijst 2: "))
len_lijst = [len_lijst1, len_lijst2]

lijst = []
temp_lijst = []

for i in range(len(len_lijst)):
    for j in range(len_lijst[i]):
        temp_lijst.append(input("Vul een iets in: "))
    lijst.append(temp_lijst)
    temp_lijst = []

print(lijst)

# Uitwerking:
'''
# a.
matrix = [[input(), input()], [input(), input()]]

print(matrix)
'''