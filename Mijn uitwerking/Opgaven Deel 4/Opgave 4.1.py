# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.1.py
@Time    :   2022/09/27 19:59:12
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* Schrijf een programma met invoer twee gehele getallen a en b en dat als uitvoer de waarde a∙b uitprint én als a en b gelijk zijn ook de volgende zin uitprint:

a en b zijn hetzelfde
'''

a = int(input("Vul een gehele getal in voor a: "))
b = int(input("Vul een gehele getal in voor b: "))

print("a * b = ", a * b)
if(a == b):
    print("a en b zijn gelijk.")


'''
# Uitwerking:

#geef de input a en b aan met input() en maak er gelijk een geheel getal van met int()
a = int(input('Vul getal a in: '))
b = int(input('Vul getal b in: '))

print('a * b: ' + str(a*b))
#printen kan ook op de volgende manier met een formatted string:
print(f'a * b: {a*b}')

#Om te controleren op gelijkheid, gebruik je de boolean operator ==
#a==b ❗is een boolean vergelijking❗ en is True als a gelijk is aan b en False als a ongelijk is aan b
#als a gelijk is aan b, dan is de if-statement True en 
#print dan 'a en b zijn hetzelfde'
if a==b:
    print('a en b zijn hetzelfde')


# output:
# Vul getal a in: 3
# Vul getal b in: 3
# a * b: 9
# a * b: 9
# a en b zijn hetzelfde
'''