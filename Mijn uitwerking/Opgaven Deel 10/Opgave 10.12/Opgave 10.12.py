# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.12.py
@Time    :   2022/12/04 18:56:26
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
12.
Vermenigvuldiging matrixes en vectoren

Neem de volgende matrix en vector over:

matrix = [[1, 2, 3], [5, 7, 11], [13, 17, 19]]

vector = [2, 4, 8]

!! *** a. (Lastig) Schrijf een programma dat deze matrix en vector met elkaar vermenigvuldigd en print het resultaat (er komt dus een nieuwe vector uit, die print je dan uit. Zie lineaire algebra boek)

!! *** b. (Nog lastiger) Neem de tweede matrix hieronder ook over en bepaal de vermenigvuldiging van de twee matrixen (matrix x matrix2):

matrix2 = [[2, 4, 8], [3, 9, 27], [4, 16, 64]]
'''

matrix = [[1, 2, 3], [5, 7, 11], [13, 17, 19]]
vector = [2, 4, 8]

# a:
sum = 0
product = []
temp = []



# for j in range(len(vector)):
#     for i in range(len(matrix)):
#         sum += int(vector[i] * matrix[j][i])
#         temp.append(sum)
#         sum = 0
#     product.append(temp)
#     temp = []

# print(product)