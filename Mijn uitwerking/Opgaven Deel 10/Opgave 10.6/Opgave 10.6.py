# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.6.py
@Time    :   2022/11/13 18:10:44
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
6. Paragraaf 10.6 aanvulling: sort()
!! * a. Lees deze paragraaf en sorteer de volgende twee lijsten:

woorden = ['Kat', 'Hond', 'Papegaai', 'Konijn', 'Cavia']

cijfers = [-40, 5.8, 10, 1, -3]

* b. kun je de sort() ook gebruiken op een gemixte lijst:

doorelkaar = ['woorden', 4, -9.0, 'cijfers', True]
'''

# a:

woorden = ['Kat', 'Hond', 'Papegaai', 'Konijn', 'Cavia']

cijfers = [-40, 5.8, 10, 1, -3]

woorden.sort()
cijfers.sort()

print("woordenlijst alfabetisch sorteren: ", woorden)
print("cijfers of volgorde zetten: ", cijfers)


# b:

doorelkaar = ['woorden', 4, -9.0, 'cijfers', True]
# doorelkaar.sort()     # dit kan niet, je krijgt dan typeerror, omdat je int en str met elkaar mengt en sorteerd...
# print(doorelkaar)




# Uitwerking:
'''
# a.
woorden = ['Kat', 'Hond', 'Papegaai', 'Konijn', 'Cavia']
cijfers = [-40, 5.8, 10, 1, -3]

woorden.sort()
print(woorden)

cijfers.sort()
print(cijfers)


# # Output:
# ['Cavia', 'Hond', 'Kat', 'Konijn', 'Papegaai']
# [-40, -3, 1, 5.8, 10]


# b.
doorelkaar = ['woorden', 4, -9.0, 'cijfers', True]

doorelkaar.sort()
print(doorelkaar)

# nee dus, dit lukt niet


# # Output:
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-9-294ec3bea5d6> in <module>
#       2 doorelkaar = ['woorden', 4, -9.0, 'cijfers', True]
#       3 
# ----> 4 doorelkaar.sort()
#       5 print(doorelkaar)
#       6 

# TypeError: '<' not supported between instances of 'int' and 'str'
'''