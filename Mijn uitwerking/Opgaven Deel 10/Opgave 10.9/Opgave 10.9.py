# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.9.py
@Time    :   2022/11/13 18:56:24
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
Nested lists¶
Hieronder volgen een aantal opgaven over nested lists. Belangrijke opgaven!

9.
Zie de volgende nested-list cubes:

cubes = [[0, 1, 8], [1, 8, 27], [8, 27, 64]]

Schrijf een programma dat:

* a. Het cijfer print in de tweede rij en derde kolom (dus index rij is 1 en index kolom is 2)

* b. Het cijfer print in de n-de rij en m-de kolom. n en m zijn input variabelen.

* c. De hele n-de rij print. n is een input variabele.

** d. Print van elke rij de som uit.

!! ** e. Print van de totale nested list (matrix) de som uit. Wat is het grote verschil in uitwerking tussen opgave d en e?

** f. Bepaal ook het gemiddelde van de matrix.
'''

# a:
cubes = [[0, 1, 8], [1, 8, 27], [8, 27, 64]]
print(cubes[2-1][3-1])

# Uitwerking:
'''
cubes = [[0, 1, 8], [1, 8, 27], [8, 27, 64]]

# a.
print(cubes[1][2])

# # Output:
# 27
'''

# b:
n = int(input("Vul geheel getal in voor n:"))
m = int(input("Vul geheel getal in voor m:"))
print(cubes[n-1][m-1])

# Uitwerking:
'''
# b.
n = int(input('Vul geheel getal in tussen 1 en 3: '))
m = int(input('Vul geheel getal in tussen 1 en 3: '))

print(cubes[n-1][m-1])

# # Output:
# Vul geheel getal in tussen 1 en 3: 1
# Vul geheel getal in tussen 1 en 3: 1
# 0
'''

# c:
print(cubes[n-1])


# Uitwerking:
'''
# c.
n = int(input('Vul geheel getal in tussen 1 en 3: '))

print(cubes[n-1])

# Output:
Vul geheel getal in tussen 1 en 3: 2
[1, 8, 27]
'''

# d:

for i in range(len(cubes)):
    print(sum(cubes[i]))

# Uitwerking:
'''
# d.
n_rijen = len(cubes)

for i in range(n_rijen): #loop voor elke rij
    som = 0
    
    for j in cubes[i]: #loop over de kolommen
        som = som + j
        
    print('De som van rij ' + str(i + 1) + ' is: ' + str(som))   


# Output:
De som van rij 1 is: 9
De som van rij 2 is: 36
De som van rij 3 is: 99
'''


# e:

lijst_som = []
for i in range(len(cubes)):
    lijst_som.append(sum(cubes[i]))

print(sum(lijst_som))

# Uitwerking:
'''
# e.
n_rijen = len(cubes)
som = 0

for i in range(n_rijen):
    for j in cubes[i]:
        som = som + j
        
print('De som van de matrix is: ' + str(som)) 
'''

# f:
totale_som = sum(lijst_som)
aantal_elementen = 0

for i in range(len(cubes)):
    for j in range(len(cubes[i])):
        aantal_elementen += 1

print("gem: " + str(totale_som / aantal_elementen))


# Uitwerking
'''
# f.
n_rijen = len(cubes)
som = 0
n_elementen = 0

for i in range(n):
    for j in cubes[i]:
        som = som + j
        n_elementen = n_elementen + 1
        
print('De som van de matrix is: ' + str(som)) 

gemiddelde = som / n_elementen
print('Gemiddelde is:', gemiddelde)


# # Output:
# De som van de matrix is: 144
# Gemiddelde is: 16.0
'''