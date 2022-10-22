# -*-coding:utf-8 -*-
'''
@File    :   test.py
@Time    :   2022/10/22 15:21:25
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

import os

# os.chdir('Tolkien.txt')
# print("\n\n\n", os.getcwd())

# os.chdir(str(os.getcwd) + "\Opgaven Deel 7\Opgave 7.1\\")

print("\n\n\n")

test = str(os.getcwd())
print(test)
script_dir = os.path.dirname(__file__)
print(script_dir)

# fin = open(os.getcwd() + "\Opgaven Deel 7\Opgave 7.1\Tolkien.txt")
# fin = open(path + "\\Tolkien.txt")
# for line in fin:
#     word = line.strip()
#     print(word)


# file = open('Tolkien.txt')
# myfile = file.read()

# print(myfile)

# file.close

# script_dir = os.path.dirname(__file__)
# rel_path = "\Tolkien.txt"
# abs_file_path = os.path.join(script_dir, rel_path)
# print(abs_file_path)

# script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
# rel_path = "2091/data.txt"
# abs_file_path = os.path.join(script_dir, rel_path)

# file = open('Opgave 7.1\Tolkien.txt')
# myfile = file.read()
# print(myfile)
# file.close