# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 21:35:37 2022

@author: vinay
"""

# # Deze statement kan je vervangen met test_input = file.read()
# test_input = """
# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
# """

# print(test_input)

# for line in test_input.split():
#     print(line)




# import os


# print(os.getcwd())

# file = open('test_input.txt')
# # lines = file.readlines()
# # i = 0
# # bingo_num = 0

# # # bingo = [[[]]]

# # # Deze for loop print de eerste bingokaart.
# # for line in lines:
# #     i += 1
# #     if (3 <= i <= 7):
# #         for woord in line.split():
# #             print(woord, end="\t")
# #         print("\n")    

# # bingo_num += 1    
# # print(f"Bord {bingo_num}")
# txt = file.read()
# print(txt)
# file.close


# nummers = "22 13 17 11 0"
# print(nummers.split())
# for cijfer in nummers.split():
#     print(cijfer, end="\t")
# print("\n")

# print(12312313)


# test = "\n\n, 5"
# print("\n" in test)
# print("4" in test)


input = """1,2,3,4,5"""

lijst = []
for num in input.split(","):
    lijst.append(num)
    
print("lijstje voor 1,2,3,4,5 -> ", lijst, end="\n\n")



input = "1,2,3,    4"
input.strip()

print(input)

# for lines in input:
#     cropped_input


