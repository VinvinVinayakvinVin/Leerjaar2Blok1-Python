# -*-coding:utf-8 -*-
'''
@File    :   Opgave 6.3.py
@Time    :   2022/10/22 08:38:32
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
3.¶
!! ** Kopie van een lijst maken

We hebben de volgende lijst 'wiccas' = ['Vuur', 'Aarde', 'Lucht']

We willen een programma schrijven dat een kopie maakt van deze lijst. De kopie wordt 'wiccas2'. 
Daarna wordt 'wiccas2' aangevuld met het element 'Water'. 
Vervolgens worden beide lijsten uitgeprint zodat we kunnen controleren of de lijst 'wiccas2' goed is aangevuld met 
'Water' t.o.v. de originele lijst 'wiccas'.

Zie hiervoor het volgende programma:
'''

'''
wiccas = ['Vuur', 'Aarde', 'Lucht']

wiccas2 = wiccas
wiccas2.append('Water')

print(wiccas2)
print(wiccas)
'''

'''
a. Wat valt je op als we op deze manier een kopie maken van 'wiccas'? (Draai het programma eens).
'''

wiccas = ['Vuur', 'Aarde', 'Lucht']

wiccas2 = wiccas
wiccas2.append('Water')

print(wiccas2)
print(wiccas)   # Het valt op, dat wiccas ook het element 'water' heeft.



'''
Bij a heb je gezien dat veranderen van wiccas2 ook de originele lijst wiccas verandert! 
Bij een kopie wil je dat eigenlijk niet! Om dit te voorkomen moet je de functie .copy() gebruiken. 
Om wiccas te kopiëren gebruik je wiccas2 = wiccas.copy()

Zie onderstaande code:
'''

'''
wiccas = ['Vuur', 'Aarde', 'Lucht']

wiccas2 = wiccas.copy()
wiccas2.append('Water')

print(wiccas2)
print(wiccas)
'''

'''
b. Blijft wiccas nu wel onveranderd, als je wiccas2 verandert?
'''

wiccas = ['Vuur', 'Aarde', 'Lucht']

wiccas2 = wiccas.copy()
wiccas2.append('Water')

print(wiccas2)
print(wiccas)   # Nu is wiccas onveranderd, het heeft geen element 'water' en dat is goed!



'''
In onderstaande code hebben we 'Aarde' vervangen door een lijstje ['Aarde', 'Magma']. 
We krijgen dan een zogenaamde nested list (komt in een latere les nog uitgebreider aan bod).

In het programma kopiëren we wiccas naar wiccas2 en passen we wiccas2 aan: we veranderen 'Aarde' in 'Steen':
'''

'''
wiccas = ['Vuur', ['Aarde', 'Magma'], 'Lucht']

wiccas2 = wiccas.copy()
wiccas2[1][0] = 'Steen'

print(wiccas2)
print(wiccas)
'''

'''
c. Blijft wiccas nu nog steeds onveranderd, als je wiccas2 verandert?
'''

wiccas = ['Vuur', ['Aarde', 'Magma'], 'Lucht']

wiccas2 = wiccas.copy()
wiccas2[1][0] = 'Steen'

print(wiccas2)
print(wiccas)       # Het is onveranderd, maar de originele is niet behouden, de aarde is naar steen veranderd en dat is niet goed.
# Fout, Het is *veranderd*! aarde is naar steen veranderd 😂


'''
Om wiccas alsnog onverandert te laten hebben we de deepcopy() nodig. 
Hiervoor hebben we de copy module nodig. Zie onderstaande code:
'''

'''
import copy

wiccas = ['Vuur', ['Aarde', 'Magma'], 'Lucht']

wiccas2 = copy.deepcopy(wiccas)
wiccas2[1][0] = 'Steen'

print(wiccas2)
print(wiccas)
'''

import copy

wiccas = ['Vuur', ['Aarde', 'Magma'], 'Lucht']

wiccas2 = copy.deepcopy(wiccas)
wiccas2[1][0] = 'Steen'

print(wiccas2)
print(wiccas)




'''
Blijft wiccas nu wel onveranderd als je wiccas2 aanpast? (Draai het programma).
'''

# wiccas is nu wel onveranderd! Het is nu goed gegaan m.b.v copy.deepcopy() functie. (Let op, hierbij moet je copy module importeren!)



'''
!! Bovenstaande heeft te maken dat python werkt met references naar objects. Lees par 10.11 en 15.6 eens uit het boek. 
Het is belangrijk dat je dit weet! Anders loop je later tegen problemen op, eventueel bij de eindopdracht.
'''


# Uitwerkingen hier beneden ⬇️:

'''
wiccas = ['Vuur', 'Aarde', 'Lucht']

wiccas2 = wiccas
wiccas2.append('Water')

print(wiccas2)
print(wiccas)

# Als je dit programma draait dan zie je dat wiccas en wiccas2 hetzelfde zijn. 
# Dat verwachte je misschien niet: wiccas2 werd veranderd (water werd toegevoegd)
# Maar blijkbaar werd wiccas zelf ook aangepast.


# # Output:

# ['Vuur', 'Aarde', 'Lucht', 'Water']
# ['Vuur', 'Aarde', 'Lucht', 'Water']
'''

'''
wiccas = ['Vuur', 'Aarde', 'Lucht']

wiccas2 = wiccas.copy()
wiccas2.append('Water')

print(wiccas2)
print(wiccas)

# Ja, zie de output als je dit programma draait.


# # Output:

# ['Vuur', 'Aarde', 'Lucht', 'Water']
# ['Vuur', 'Aarde', 'Lucht']
'''

'''
wiccas = ['Vuur', ['Aarde', 'Magma'], 'Lucht']

wiccas2 = wiccas.copy()
wiccas2[1][0] = 'Steen'

print(wiccas2)
print(wiccas)

# Nee! 
# Blijkbaar verandert wiccas nu ook weer als we een element in een lijst uit een lijst veranderen!


# # Output:

# ['Vuur', ['Steen', 'Magma'], 'Lucht']
# ['Vuur', ['Steen', 'Magma'], 'Lucht']
'''

'''
import copy

wiccas = ['Vuur', ['Aarde', 'Magma'], 'Lucht']

wiccas2 = copy.deepcopy(wiccas)
wiccas2[1][0] = 'Steen'

print(wiccas2)
print(wiccas)

# Ja.


# # Output:

# ['Vuur', ['Steen', 'Magma'], 'Lucht']
# ['Vuur', ['Aarde', 'Magma'], 'Lucht']
'''