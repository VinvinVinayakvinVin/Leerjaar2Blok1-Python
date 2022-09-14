# -*-coding:utf-8 -*-
'''
@File    :   Opgave 2.18.py
@Time    :   2022/09/14 16:44:36
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
Dit is een opgave uit het boek:

Exercise 2.1: Repeating my advice from the previous chapter, 
whenever you learn a new feature, you should try it out and make errors on purpose to see what goes wrong.

We've seen that n = 42 is legal. What about 42 = n?
How about x = y = 1?
In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?
What if you put a period at the end of a statement?
In math notation you can multiply x and y like this: xy. What happens if you try that in Python?
PS: Lees ook de error meldingen, zodat je ze in de toekomst herkent en je je errors sneller kunt oplossen.
'''

# print(4);   # no error 😁
x = 10
y = 8
# print(xy)   # xy not defined!

x = y = 1   # dit kan gewoon (～￣▽￣)～
print(x, y)

# 42 = n  # SyntaxError: cannot assign to literal

naam = "Vinayak". # SyntaxError: invalid syntax (komt door de punt aan het einde!)