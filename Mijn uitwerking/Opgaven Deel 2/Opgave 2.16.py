# -*-coding:utf-8 -*-
'''
@File    :   Opgave 2.16.py
@Time    :   2022/09/14 16:32:12
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
a. * Iemand heeft geprobeerd om negen keer Hello, World! uit te printen. Zie de code hieronder.

    print("Hello World!")
    print("Hello World!")
    print("Hello World!)
    print("Hello World!")
    print("Hello World!")
    print("Hello World!"
    print("Hello World!")
    print("Hello World!")

Er staan echter drie fouten in. Wat zijn deze drie fouten? Waarom is het fout en wat voor soort fout is het (Syntax, Runtime, Semantic of Bug)?
'''

# print("Hello World!")
# print("Hello World!")
# # print("Hello World!)
# print("Hello World!")
# print("Hello World!")
# #print("Hello World!"
# print("Hello World!")
# print("Hello World!")

# 3e en 6e print: syntax error
# Er is ook een semantic error, er staan maar 8 prints in plaats van 9 prints❗

'''
Uitwerking zegt:
Dat het een bug is en niet semantic error is❓
'''

'''
b. * Hoe zou je de code om negen keer Hello, World! uit te printen beter kunnen doen t.o.v. de code hierboven (nadat je de fouten hebt hersteld)?

Met beter bedoelen we nu een kortere code.
'''

print("Hello World!\n"*9, end='')