# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.12.b uitw.py
@Time    :   2022/12/06 12:45:33
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

# #zelfde als b maar met list comprehensions
# matrix = [[1, 2, 3], [5, 7, 11], [13, 17, 19]]
# matrix2 = [[2, 4, 8], [3, 9, 27], [4, 16, 64]]

# # matrixOutput = [[[sum(a*b for a,b in zip(matrix_row, matrix2_col))] for matrix2_col in zip(*matrix2)] for matrix_row in matrix]

# # matrixOutput = [      [   sum(    a*b for a,b in zip(matrix_row, matrix2_col)     )    ]                for matrix2_col in zip(*matrix2)]                          for matrix_row in matrix
    
# matrixOutput = tuple(zip(*matrix, *matrix2))
# test = 1

# print(a*b for a,b in zip(matrix_row, matrix2_col))

matrix = [[1, 2, 3], [5, 7, 11], [13, 17, 19]]
matrix2 = [[2, 4, 8], [3, 9, 27], [4, 16, 64]]

# step 1
x = 0
print([x for matrix2_col in zip(*matrix2)])

# step 2
print([[x for matrix2_col in zip(*matrix2)] for matrix_row in matrix])

# step 3
print([[    sum(a*b for a,b in zip(matrix_row, matrix2_col))    for matrix2_col in zip(*matrix2)] for matrix_row in matrix])

# step 4 (test) (fail)
# print([[    sum(a*b for a,b in zip(matrix2_col, matrix_row))    for matrix_row in zip(*matrix)] for matrix2_col in matrix2])

# step 5 (test)
print([a for a in zip(*matrix)])

# step 6 (test)
print([a for a in zip(*matrix)][2][2])

# step 7 (list comprehension test2)
for matrix_row in matrix:
    for matrix2_col in matrix2:
        print(matrix_row, matrix2_col)
print("test 7 👆\n")

# # test 8 test2 (fail)
# for matrix_row in matrix:
#     for matrix2_col in matrix2:
#         print(tuple(zip(matrix_row, matrix2_col)))
# print("test 8 👆\n")

# test 9 test2
for matrix_row in matrix:
    for matrix2_col in zip(*matrix2):
        print(tuple(zip(matrix_row, matrix2_col)))
print("test 9 👆\n")

# test 10 test2
for matrix_row in matrix:
    for matrix2_col in zip(*matrix2):
        print(sum(a*b for a,b in zip(matrix2_col, matrix_row)))
print("test 10 👆\n")

print("transponeerde matrix: " + str(tuple(zip(*matrix))))