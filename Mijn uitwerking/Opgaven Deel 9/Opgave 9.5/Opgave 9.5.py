# -*-coding:utf-8 -*-
'''
@File    :   Opgave 9.5.py
@Time    :   2022/11/13 13:30:32
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

zin = "Hallo, ik ga nu naar buiten wat doen... :D"

# Korte versie
lijst = [element for element in zin]
print(lijst)

# Lange versie
lijst = []
for element in zin:
    lijst.append(element)
print(lijst)



# Uitwerking:
'''
zin = 'Dit is een kortere manier en wordt List Comprehension genoemd'

lijst = [letter for letter in zin]

print(lijst)
'''