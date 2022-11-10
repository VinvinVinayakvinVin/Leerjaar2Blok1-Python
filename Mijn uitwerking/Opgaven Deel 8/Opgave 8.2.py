# -*-coding:utf-8 -*-
'''
@File    :   Opgave 8.2.py
@Time    :   2022/11/10 20:49:31
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
2.¶
** Schrijf een programma dat onder elkaar willekeurige getallen print tussen [0, 1) en afrondt op drie decimalen. 
Je programma stopt pas als er een getal wordt geprint dat groter is dan 0,9.
'''

import random

num = 0
while num <= 0.9:
    num = random.random()
    print(num)



# Uitwerking:
'''
import random

getal = 0

while getal <= 0.9:
    getal = random.random()
    print(getal)    



# Output:
0.7434041487196933
0.764931752270528
0.4114925243408746
0.4954520887499698
0.7718539072982958
0.35533195807506934
0.47435745873117463
0.5666347873234071
0.557476005411048
0.9118653256341802
'''