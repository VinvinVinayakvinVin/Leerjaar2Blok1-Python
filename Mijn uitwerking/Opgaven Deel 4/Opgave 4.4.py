# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.4.py
@Time    :   2022/09/27 20:30:19
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
!! ** Schrijf een programma met invoer een geheel getal. 
Je programma bepaalt of dit getal een even of oneven getal is.
Print het resultaat. Hint: gebruik de % operator (modulus).
'''

x = int(input("Type een geheel getal in: "))

# Als x een getal is die deelbaar is door 2, dan is het getal x een even geheel getal, anders niet.
if x % 2 == 0:
    print(str(x) + " is een even geheel getal.")
else:
    print(str(x) + " is een oneven geheel getal.")


'''
# Uitwerking:

getal = int(input('Vul een geheel getal in: '))

#Als getal/2 een restwaarde van 0 heeft, dan is het een even getal
#getal%2 geeft de restwaarde van getal/2
if getal%2 == 0:
    print(f'{getal} is een even getal')
else:
    print(f'{getal} is een oneven getal')


# Output:


# Vul een geheel getal in: 7
# 7 is een oneven getal
'''

# Vergeet niet om #-teken te gebruiken en om comments te schrijven wat de programma doet
# (ook al is het voor mij heel makkelijk te begrijpen).