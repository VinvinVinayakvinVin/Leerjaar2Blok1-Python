# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.10.b.py
@Time    :   2022/11/22 15:25:45
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
!! ** b. Zoals a, maar nu moet je eerst via input opgeven hoeveel rijen en kolommen de matrix moet hebben.
Print de matrix uit.
'''

# Opd10.10.b:

aantal_rijen = int(input("Vul het aantal rijen die je in je matrix wilt hebben: "))
aantal_kolommen = int(input("Vul het aantal kolommen die je in je matrix wilt hebben: "))

lijst = []
# temp_lijst = []

for i in range(aantal_rijen):
    temp_lijst = []
    for j in range(aantal_kolommen):
        temp_lijst.append(input("Vul iets in: "))
    lijst.append(temp_lijst)
    # temp_lijst = []

print(lijst)



# Uitwerking:

'''
###### b.
n_rijen = int(input('Vul het aantal rijen in: '))
m_kolom = int(input('Vul het aantal kolommen in: '))

matrix = []

for i in range(n_rijen):
    rij = []
    for j in range(m_kolom):
        rij.append(input())
    matrix.append(rij)
    
print(matrix)
'''