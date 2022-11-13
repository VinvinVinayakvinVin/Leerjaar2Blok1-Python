# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.5.py
@Time    :   2022/11/13 17:49:59
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
5. Lees 8.10: String Comparisons¶
** Schrijf een programma dat bepaald of een ingevuld woord (via input()) 
eerder of later in alfabetische orde staat dan het woord 'Science-fiction'.

Test o.a. met de woorden: 'aandacht', 'Wiskunde', 'PS5' en 'Science-fiction'
'''

# lijst = ['aandacht', 'Wiskunde', 'PS5', 'Science-fiction']

# txt = input("type een woord in:")
# lijst.append(txt)

# alf_lijst = lijst.sort()    # Let op, als je sort function gebruikt, dan is hoofdletter wel gevoelig, qua alfabetisch volgorde.
# print(lijst)



woord = input('Vul een woord in: ')

if woord.lower() < 'science-fiction': # dus alles met kleine letter
    print('Het woord, ' + woord + ', komt voor science-fiction.')
elif woord.lower() > 'science-fiction':
    print('Het woord, ' + woord + ', komt na science-fiction.')
else:
    print('Je hebt hetzelfde woord ingevuld als Science-fiction')

# Uitwerking:
'''
woord = input('Vul een woord in: ')

if woord.lower() < 'science-fiction': # dus alles met kleine letter
    print('Het woord, ' + woord + ', komt voor science-fiction.')
elif woord.lower() > 'science-fiction':
    print('Het woord, ' + woord + ', komt na science-fiction.')
else:
    print('Je hebt hetzelfde woord ingevuld als Science-fiction')



# Output:
Vul een woord in: Wiskunde
Het woord, Wiskunde, komt na science-fiction.
'''