# -*-coding:utf-8 -*-
'''
@File    :   Opgave 9.2 Deel 2.py
@Time    :   2022/11/13 12:48:23
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

txt = "a b c d e"
txt = txt.replace(" ", "")
print(txt)      # prints "abcde" out.

txt = "a b c d e"
nwtxt = ""
for char in txt:
    if char != " ":
        nwtxt += char
print(nwtxt)      # prints "abcde" out.