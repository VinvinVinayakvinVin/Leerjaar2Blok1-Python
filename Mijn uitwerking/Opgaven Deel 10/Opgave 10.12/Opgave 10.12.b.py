# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.12.b.py
@Time    :   2022/12/05 09:21:04
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

# b:

matrix = [[1, 2, 3], [5, 7, 11], [13, 17, 19]]
matrix2 = [[2, 4, 8], [3, 9, 27], [4, 16, 64]]

product = []
temp = []
sum = 0

m = len(matrix)
n = len(matrix2)
l = len(matrix2[0])

for i in range(m):
    product.append([])
    
for i in range(l):
    for j in range(m):
        for k in range(n):
            sum += (matrix[j][k] * matrix2[k][i])
        product[j].append(sum)
        sum = 0

print(product)



# Uitwerking:
'''
# b.
matrix = [[1, 2, 3], [5, 7, 11], [13, 17, 19]]
matrix2 = [[2, 4, 8], [3, 9, 27], [4, 16, 64]]

vectorOutput = []

for i in range(len(matrix)): # aantal rijen matrix 1  
    rij = []
    
    for j in range(len(matrix2[0])):  # aantal kolommen matrix 2
        som = 0
        for k in range(len(matrix2)): # aantal rijen matrix 2
            som = som + matrix[i][k]*matrix2[k][j]
        rij.append(som)
    vectorOutput.append(rij)
    
print(vectorOutput)
'''

# Alternatief:
'''
#zelfde als b maar met list comprehensions
matrix = [[1, 2, 3], [5, 7, 11], [13, 17, 19]]
matrix2 = [[2, 4, 8], [3, 9, 27], [4, 16, 64]]

matrixOutput = [[[sum(a*b for a,b in zip(matrix_row, matrix2_col))] for matrix2_col in zip(*matrix2)] for matrix_row in matrix]
    
# matrixOutput = []
    
print(matrixOutput)
'''

# Output:
'''
[[[20], [70], [254]], [[75], [259], [933]], [[153], [509], [1779]], [[200], [650], [2234]]]
'''