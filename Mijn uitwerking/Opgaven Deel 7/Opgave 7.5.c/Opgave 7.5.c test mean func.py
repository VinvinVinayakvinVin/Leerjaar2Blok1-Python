# -*-coding:utf-8 -*-
'''
@File    :   Opgave 7.5.c test mean func.py
@Time    :   2022/11/07 11:46:02
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

import statistics

lijst = [1,2,3,4,5,6,234,1,4,67,3]

print(statistics.mean(lijst))

som = 0
for i in range(len(lijst)):
    som += lijst[i]

print("gem: " + str(som/len(lijst)))