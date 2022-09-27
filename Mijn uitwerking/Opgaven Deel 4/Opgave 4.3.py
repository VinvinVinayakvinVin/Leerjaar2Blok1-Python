# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.3.py
@Time    :   2022/09/27 20:12:51
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* Schrijf een programma dat als invoer drie gehele getallen a, b en c heeft en bepaalt of b tussen a en c ligt ([a, c]).

Als dat zo is print je uit: “[b] ligt tussen [a] en [c]” ,

anders print je uit “[b] ligt niet tussen [a] en [c]”.

Bijv. invoer is 1 9 7, dan uitvoer: “9 ligt niet tussen 1 en 7.”
'''

a = int(input("Vul een geheel getal in voor a: "))
b = int(input("Vul een geheel getal in voor b: "))
c = int(input("Vul een geheel getal in voor c: "))

# 1e methode
if a <= b <= c or c <= b <= a:
    print(f"{b} ligt tussen {a} en {c}")
else:
    print(f"{b} ligt niet tussen {a} en {c}")

# 2e methode
if (a <= b and b <= c) or (a >= b and b >= c):
    print(b, "ligt tussen", a, "en", c)
else:
    print(b, "ligt niet tussen", a, "en", c)


'''
# Uitwerking:

a = int(input('Vul getal a in: '))
b = int(input('Vul getal b in: '))
c = int(input('Vul getal c in: '))

if a <= b <= c:
    print(str(b) + ' ligt tussen ' + str(a) + ' en ' + str(c))
else:
    print(str(b) + ' ligt niet tussen ' + str(a) + ' en ' + str(c))


# Alternatief:
if a <= b <= c:
    print(f'{b} ligt tussen {a} en {c}')
else:
    print(f'{b} ligt niet tussen {a} en {c}')


# Output:

# Vul getal a in: 1
# Vul getal b in: 9
# Vul getal c in: 7
# 9 ligt niet tussen 1 en 7
# 9 ligt niet tussen 1 en 7
'''