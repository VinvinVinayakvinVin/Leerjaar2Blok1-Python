# -*-coding:utf-8 -*-
'''
@File    :   Opgave 7.5.a.py
@Time    :   2022/11/07 09:48:29
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
5.¶
Open handmatig de file Klas.txt (download eerst van Brightspace). En bekijk de inhoud. 
De gegevens in deze file gaan we onderzoeken/verwerken.

* a. Schrijf een stuk code dat de file Klas.txt opent, inleest en uitprint.
'''

import os

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.5.a\\")
file = open("Klas.txt")
lines = file.readlines()

for line in lines:
    print(line)

file.close()