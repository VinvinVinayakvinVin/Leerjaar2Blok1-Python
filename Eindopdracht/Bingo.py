# -*-coding:utf-8 -*-
'''
@File    :   Bingo.py
@Time    :   2022/11/06 20:17:14
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''



file = open('test_input.txt')

# Deze statement kan je vervangen met test_input = file.read()
# Dit is de test_input tekst.
test_input = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

trekkingsgetallen = []
regelnum = 0
input = file.read().split("\n")
print(input, end="\n\n\n\n")
for num in input:
    # if num == "":
    #     break
    regelnum += 1
    if(regelnum == 1): 
        print(num.split(","))
        trekkingsgetallen = num.split(",")
    else:
        num.strip(",")
        print(num)

print("\n\n\n\n", trekkingsgetallen)
for getal in trekkingsgetallen:
    print(getal, end=" -> ")

# print(input, end="\n\n\n")

# for line in input.split(","):
#     if(line in "\n" == False):
#         trekkingsgetallen.append(line)
    
# print(trekkingsgetallen)




file.close