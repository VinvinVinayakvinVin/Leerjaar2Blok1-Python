# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.11.py
@Time    :   2022/10/06 06:45:26
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* Schrijf een programma dat als invoer twee decimale getallen x en y heeft en dan de volgende functiewaarden berekent en uitprint onder elkaar:

𝑓(𝑥,𝑦)=𝑙𝑛(𝑥)∗𝑦⎯⎯√𝑣𝑜𝑜𝑟𝑥>0𝑒𝑛𝑦≥0 
𝑔(𝑥,𝑦)=𝑙𝑛(𝑥)∗𝑦⎯⎯√⎯⎯⎯⎯⎯⎯√𝑣𝑜𝑜𝑟𝑥>0𝑒𝑛𝑦≥0 
ℎ(𝑥,𝑦)=𝑙𝑛(𝑥)∗𝑦⎯⎯√⎯⎯⎯⎯⎯⎯√⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√𝑣𝑜𝑜𝑟𝑥>0𝑒𝑛𝑦≥0 

Laat je programma een foutmelding geven als er geen geschikte x en/of y waarde is ingevuld. 
(Met een foutmelding bedoelen we dat je programma iets uitprint over wat je fout doet of fout hebt ingevuld in de commandprompt). 
Hint: bijv y < 0?
'''

from math import sqrt
from sympy import ln


x = float(input("Vul een decimaal getal in voor x: "))
y = float(input("Vul een decimaal getal in voor y: "))

# Als x kleiner of gelijk is aan 0 óf y is kleiner dan 0, dan print er een foutmelding uit.
if x <= 0 or y < 0:
    print("Je hebt verkeerde waarde ingevuld voor x of y.")
else:
    print("f(x, y) = ln(x) * sqrt(y) voor x > 0 en y >= 0")
    print(f"f({x}, {y}) = ln({x}) * sqrt({y}) = " + str(ln(x) * sqrt(y)))

    print("g(x, y) = ln(x) * sqrt(sqrt(y)) voor x > 0 en y >= 0")
    print(f"g({x}, {y}) = ln({x}) * sqrt(sqrt({y})) = " + str(ln(x) * sqrt(sqrt(y))))

    print("h(x, y) = ln(x) * sqrt(sqrt(y)) voor x > 0 en y >= 0")
    print(f"h({x}, {y}) = ln({x}) * sqrt(sqrt(sqrt({y}))) = " + str(ln(x) * sqrt(sqrt(sqrt(y)))))

'''
# Uitwerking:

x = float(input('Vul x in: '))
y = float(input('Vul y in: '))

#controleer of x>0 en y>=0
if x <= 0 or y < 0:
    print('Ongeldige waarde voor x en/of y!')
else:
    print('f(x, y) = ' + str(math.log(x) * math.sqrt(y)))
    print('g(x, y) = ' + str(math.log(x) * math.sqrt(math.sqrt(y))))
    print('h(x, y) = ' + str(math.log(x) * math.sqrt(math.sqrt(math.sqrt(y)))))


# output:
# Vul x in: 3
# Vul y in: 10
# f(x, y) = 3.4741170976416185
# g(x, y) = 1.953639612554237
# h(x, y) = 1.465023032576925
'''
