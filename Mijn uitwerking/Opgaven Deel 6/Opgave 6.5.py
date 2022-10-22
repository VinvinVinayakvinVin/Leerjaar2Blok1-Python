# -*-coding:utf-8 -*-
'''
@File    :   Opgave 6.5.py
@Time    :   2022/10/22 09:34:33
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
5.¶
* extend() met een string

Een string is iteraarbaar (iterable). 
Daarmee bedoelen we dat we de karakters van het stukje tekst één voor één langs (kunnen) gaan.

Stel we hebben de lijst fruit = ['banaan', 'druif', 'peer'] en we willen 'appel' toevoegen. 
Dat gaat goed met de .append() functie. 
Als we de .extend() gebruiken wordt 'appel' gezien als een "iterable", elk letter wordt als een element gezien. 
Dus aan de lijst fruit wordt niet 'appel' toegevoegd, maar de letters ervan 'a', 'p', 'p', 'e', 'l'.

Maak nu een programma waarin je de lijst fruit aanmaakt en daarna uitbreidt met 
'appel' via de .append() functie en afzonderlijk met de .extend() functie. Zie je het verschil?
'''

fruit = ['banaan', 'druif', 'peer']
print(fruit)
fruit.append("appel")
print(fruit, end="\n\n")

# Output:

# ['banaan', 'druif', 'peer']
# ['banaan', 'druif', 'peer', 'appel']



fruit = ['banaan', 'druif', 'peer']
print(fruit)
fruit.extend("appel")
print(fruit)

# Output:

# ['banaan', 'druif', 'peer']
# ['banaan', 'druif', 'peer', 'a', 'p', 'p', 'e', 'l']




# Uitwerking ⬇️

'''
fruit = ['banaan', 'druif', 'peer']
fruit.append('appel')
    
print(fruit) 

# Output ⬇️
['banaan', 'druif', 'peer', 'appel']


fruit = ['banaan', 'druif', 'peer']
fruit.extend('appel')
    
print(fruit) 

# Output ⬇️
['banaan', 'druif', 'peer', 'a', 'p', 'p', 'e', 'l']
'''