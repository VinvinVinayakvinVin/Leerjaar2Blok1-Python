# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.17.py
@Time    :   2022/10/19 20:47:37
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
4.17¶
** Schrijf een programma met drie gehele getallen als invoervariabelen
en waarvan de output gelijk (dit woord print je dus) is als alle drie de getallen hetzelfde zijn,
anders is de output niet gelijk.

Opmerking: Houd de code zo kort mogelijk.
'''

a = int(input("Vul een geheel getal in voor a: "))
b = int(input("Vul een geheel getal in voor b: "))
c = int(input("Vul een geheel getal in voor c: "))

if a == b == c:
    print("het is gelijk...")
else:
    print("niet gelijk...")


'''
# Uitwerking

a = int(input('Geef a: '))
b = int(input('Geef b: '))
c = int(input('Geef c: '))

if a == b and b == c:
    print('gelijk')
else:
    print('niet gelijk')
    
# Alternatief:
if a == b == c:
    print('gelijk')
else:
    print('niet gelijk')


# # Output:
# Geef a: 4
# Geef b: 4
# Geef c: 4
# gelijk
# gelijk
'''