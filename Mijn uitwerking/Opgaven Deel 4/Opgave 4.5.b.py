# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.5.b.py
@Time    :   2022/09/27 20:47:38
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
Zie opgavens in de comment van Opgaven 4.5.py, of zie hieronder:
'''

'''
b. Zie a, maar gebruik de math module nu niet, maak zelf een programma dat de absolute waarde van een getal bepaalt.
Hint: iets met een if-statement.
'''

x = int(input("Type een getal in: "))   # <--- Ik kan ook een float gebruiken.

# if statement dat bekijkt of x een positief of negatief getal is.
# als getal x negatief is, dan print de x maal -1.
# anders print getal x.

if x < 0:
    print(f"Absolute waarde van {x} is: " + str(x * -1))
else:
    print(f"Absolute waarde van", x, "is: " + str(x))

'''
else statement is eigenlijk niet nodig.
Code is dubbel.
'''