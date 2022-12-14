# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.7.py
@Time    :   2022/09/19 06:53:55
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* a. Een andere functie in de random module is uniform().
Zoek op internet wat deze functie doet.

Maak een programma dat een willkeurig getal tussen n en m print; n en m is invoer.
'''

import random

input1 = float(input("Vul een getal in: "))
input2 = float(input("Vul de tweede getal in: "))
x = random.uniform(input1, input2)
print(f"""Het willekeurige decimaal getal {x} zit tussen de getallen {input1} en {input2},
waarbij {input1} en {input2} inclusief in de domein liggen.""")

# The uniform() method returns a random floating number between two specified numbers (both included).
# Source: https://www.aw3schools.com/python/ref_random_uniform.asp

'''
# Uitwerking ⬇️

# import random 
# Een module hoeft maar 1 keer aangeroepen te worden in een notebook
# Dus als je het bij de vorige opgaven al hebt gerund, hoeft het niet nog eens.

n = float(input('Geef n: '))
m = float(input('Geef m: '))

print(random.uniform(n, m))

# output: ⬇️
# Geef n: .2
# Geef m: 10.5
# 0.9668816475392641
'''
