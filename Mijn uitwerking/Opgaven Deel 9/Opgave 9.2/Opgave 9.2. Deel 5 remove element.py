# -*-coding:utf-8 -*-
'''
@File    :   Opgave 9.2. Deel 5 remove element.py
@Time    :   2022/11/13 18:54:02
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
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