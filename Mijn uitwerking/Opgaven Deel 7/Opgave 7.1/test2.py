# -*-coding:utf-8 -*-
'''
@File    :   test2.py
@Time    :   2022/10/22 19:54:59
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

import os


os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.1\\")
file = open("Tolkien.txt", "r")
for i in range(5):
    line = file.readline().strip().upper()
    print(line)
    
file.close