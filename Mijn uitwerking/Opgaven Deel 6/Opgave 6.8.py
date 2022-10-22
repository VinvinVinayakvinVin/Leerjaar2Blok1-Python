# -*-coding:utf-8 -*-
'''
@File    :   Opgave 6.8.py
@Time    :   2022/10/22 10:17:02
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
8.¶
* Handigheidje 1: print() statement

De print() statement kan meerdere inputs hebben. Elke input wordt gescheiden door een komma.

print(‘Hello’, ‘World’, ‘I’).

I.p.v. de + operator te gebruiken (samenvoegen / concatenate) kun je dus ook samenvoegen met komma’s. Voordeel is dat je nu makkelijk ook waardes met verschillende datatypes kan samenvoegen.

Bijv. print(‘Woorden’, ‘En cijfers door elkaar’, 8, 9, True).

Je hoeft dan niet meer de datatypes om te zetten naar één soort datatype.

Schrijf een programma dat de drie onderstaande variabelen samenvoegt en in één zin uitprint:

tekst = 'Verschillende datatypes samenvoegen'
getal = 56.9
boolean = True

a. Doe dit met de + operator:
b. Doe dit met de komma’s in de print statement.
'''

# a:

tekst = 'Verschillende datatypes samenvoegen'
getal = 56.9
boolean = True

nw_tekst = tekst + " " + str(getal) + " " + str(boolean)
print(nw_tekst)

# b:

print(tekst, getal, boolean)



# Uitwerking voor a ⬇️
'''
#a
tekst = 'Verschillende datatypes samenvoegen'
getal = 56.9
boolean = True

print(tekst + ' ' + str(getal) + ' '+ str(boolean))



# # Output:

# Verschillende datatypes samenvoegen 56.9 True
'''

# Uitwerking voor b ⬇️
'''
#b
tekst = 'Verschillende datatypes samenvoegen'
getal = 56.9
boolean = True

print(tekst, getal, boolean)



# # Output:

# Verschillende datatypes samenvoegen 56.9 True
'''