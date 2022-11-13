# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.1.py
@Time    :   2022/11/13 13:51:28
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
1. Lees par 8.2: len() functie¶
* a. Schrijf een programma dat van de volgende woorden/zinnen bepaalt hoeveel characters (letters en symbolen) het heeft:

'Borgcube'

'Netflixen en bingewatchen'

'Happy@gmail.com'

Hint: len()

* b. Worden symbolen geteld (zoals @ en .) en ook spaties?
'''

lijst = ['Borgcube', 'Netflixen en bingewatchen', 'Happy@gmail.com', '🩳']
for i in lijst:
    print(len(i))
# symbolen worden meegeteld.



# Uitwerking:
'''
#a
print(len('Borgcube'))
print(len('Netflixen en bingewatchen'))
print(len('Happy@gmail.com'))

#b
#Ja, speciale tekens en spaties worden ook geteld



# # Output:
# 8
# 25
# 15
'''