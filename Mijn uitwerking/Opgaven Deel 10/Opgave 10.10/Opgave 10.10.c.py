# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.10.c.py
@Time    :   2022/11/22 16:06:04
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* c. Zoals b, maar nu moet de input getallen zijn en de elementen van de matrix de kwadraten van de invoer.
'''

############################################################################################################### Opg.10.10.c:

aantal_rijen = int(input("Vul het aantal rijen die je in je matrix wilt hebben: "))
aantal_kolommen = int(input("Vul het aantal kolommen die je in je matrix wilt hebben: "))

lijst = []

for i in range(aantal_rijen):
    temp_lijst = []
    for j in range(aantal_kolommen):
        temp_lijst.append(int(input("Vul een geheel getal in: "))**2)
    lijst.append(temp_lijst)

print(lijst)



# Uitwerking:
'''
# c.
n_rijen = int(input('Vul het aantal rijen in: '))
m_kolom = int(input('Vul het aantal kolommen in: '))

matrix = []

for i in range(n_rijen):
    rij = []
    for j in range(m_kolom):
        waarde = float(input())
        rij.append(waarde*waarde)
    matrix.append(rij)
    
print(matrix)



# Output:

# Vul het aantal rijen in: 2
# Vul het aantal kolommen in: 2
# 4
# 2
# 7
# 5
# [[16.0, 4.0], [49.0, 25.0]]
'''