# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.12.py
@Time    :   2022/10/12 15:32:56
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
4.12
* Nested conditional

In plaats van elif te gebruiken kunnen we ook zogenaamde nested conditionals gebruiken.
Dat zijn if en else statements binnenin een andere if of else statement.
Meestal is dit onoverzichtelijker en gebruik je liever elif.
Hieronder een nested conditional.
'''

getal = float(input('Vul een getal in\n'))

if getal > 0:
    print('Het ingevulde getal is positief\n')
else: 
    if getal < 0:
        print('Het ingevulde getal is negatief\n')
    else:
        print('Het ingevulde getal is neutraal: niet positief, niet negatief\n')

# Kun jij bovenstaande code omzetten zonder nesting? Dus naar een structuur met if, elif en else?

getal = float(input('Vul een getal in\n'))

if getal > 0:
    print('Het ingevulde getal is positief\n')
elif getal < 0:
    print('Het ingevulde getal is negatief\n')
else:
    print('Het ingevulde getal is neutraal: niet positief, niet negatief\n')

'''
# Uitwerking:

getal = float(input('Vul een getal in \n'))

if getal > 0:
    print('Het ingevulde getal is positief \n')
elif getal < 0:
    print('Het ingevulde getal is negatief \n')
else:
    print('Het ingevulde getal is neutraal: niet positief, niet negatief \n')
'''