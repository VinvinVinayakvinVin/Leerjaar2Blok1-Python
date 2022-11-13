# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.8.py
@Time    :   2022/11/13 18:19:40
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
!! * 8. Paragraaf 10.8 aanvulling: Deleting¶
Lees deze paragraaf. We gebruiken de volgende lijst:

elementen = ['Flamingo', 'Caspian', 'Boek', 'Zed', 14, 25, 'Barbara Elsborg', 'Drama', 'Happy End', 'The Story of Us']

a. Delete het 3e element en print dan de nieuwe lijst en het gewiste element. Gebruik de pop() functie.

b. Delete het 5e en 6e element (dus de getallen 14 en 25). Dat is dus index 4 en 5 van de lijst. Gebruik de del methode.

c. Delete het woord 'Flamingo' en 'Drama' uit de lijst. Gebruik remove().
'''


# a:

elementen = ['Flamingo', 'Caspian', 'Boek', 'Zed', 14, 25, 'Barbara Elsborg', 'Drama', 'Happy End', 'The Story of Us']
elementen.pop(3-1)
print(elementen)

# b:
del elementen[3]
del elementen[3]

print(elementen)

# c:
elementen.remove("Flamingo")
elementen.remove("Drama")
print(elementen)



# Uitwerking:
'''
# a.
elementen = ['Flamingo', 'Caspian', 'Boek', 'Zed', 14, 25, 'Barbara Elsborg', 'Drama', 'Happy End', 'The Story of Us']

x = elementen.pop(2)
print(elementen)
print(x)


# # Output:

# ['Flamingo', 'Caspian', 'Zed', 14, 25, 'Barbara Elsborg', 'Drama', 'Happy End', 'The Story of Us']
# Boek



# b.
elementen = ['Flamingo', 'Caspian', 'Boek', 'Zed', 14, 25, 'Barbara Elsborg', 'Drama', 'Happy End', 'The Story of Us']

del elementen[4:6] # 6 telt niet mee

print(elementen)



# # Output:

# ['Flamingo', 'Caspian', 'Boek', 'Zed', 'Barbara Elsborg', 'Drama', 'Happy End', 'The Story of Us']



# c.
elementen = ['Flamingo', 'Caspian', 'Boek', 'Zed', 14, 25, 'Barbara Elsborg', 'Drama', 'Happy End', 'The Story of Us']

elementen.remove('Flamingo')
elementen.remove('Drama')

print(elementen)



# # Output:

# ['Caspian', 'Boek', 'Zed', 14, 25, 'Barbara Elsborg', 'Happy End', 'The Story of Us']
'''

