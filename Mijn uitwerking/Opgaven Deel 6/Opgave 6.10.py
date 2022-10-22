# -*-coding:utf-8 -*-
'''
@File    :   Opgave 6.10.py
@Time    :   2022/10/22 10:35:51
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
10.¶
*** Nested for-loops II. Tabel

Hieronder staat een tabel. Helemaal links staan de getallen 0 t/m 10 onder elkaar. 
Rechts ervan worden die getallen tot de macht 0, 1, 2, 3, 4 en 5 genomen. 
De derde regel bijv.: links het getal 2, rechts daarnaast:
2^0=1,2^1=2,2^2=4,2^3=8,2^4=16,2^5=32 

Schrijf een programma dat deze tabel namaakt. 
Hint: misschien handig om \t (of zelfs een betere manier) en % te gebruiken voor de uitlijning. 
Uiteraard heb je een nested for-loop nodig.
'''

# Het eenvoudigste manier om dit te maken ⬇️
# for i in range(11):
#     print(f"{i}\t{i ** 0}\t{i ** 1}\t{i ** 2}\t{i ** 3}\t{i ** 4}\t{i ** 5}")

# Nu maken hoe de opdracht het wilt 😅
for i in range(11):
    print(i, end="\t")

    for j in range(6):
        print(i ** j, end="\t")

        if j == 5:
            print()




# Uitwerking:
'''
import math

#Er moet 2 keer gelooped worden, 1 keer over de rijen en 1 keer over de kolommen
#In de uitwerking gaat i loopen over de rijen en j over de kolommen

#eerste loop is om de eerste kolom helemaal links te printen: 0, 1, 2,...,10
#dit wordt niet in 1 keer uitgeprint maar gaat eerst 0 uitprinten (linksboven in de tabel) en dan de
#machten 0, 1, ..., 5 uitprinten. De machten worden geprint in de tweede loop.
#Daarna wordt op de volgende regel 1 uitgeprint en vervolgens weer de machten.
for i in range(11):
    print(i, end = '\t')
    
    for j in range(6): #tweede loop gaat voor een gegeven regel i steeds de macht per kolom printen
        print(int(math.pow(i, j)), end = '\t')
        
        if (j+1)%6 == 0: #het einde van de regel gebeurt bij de zesde j index maar j loopt van 0,...,5 
            print()      #dus als j+1 een veelvoud is van 6 ((j+1)%6 == 0), ga dan naar de volgende regel


# # Output:
# 0	1	0	0	0	0	0	
# 1	1	1	1	1	1	1	
# 2	1	2	4	8	16	32	
# 3	1	3	9	27	81	243	
# 4	1	4	16	64	256	1024	
# 5	1	5	25	125	625	3125	
# 6	1	6	36	216	1296	7776	
# 7	1	7	49	343	2401	16807	
# 8	1	8	64	512	4096	32768	
# 9	1	9	81	729	6561	59049	
# 10	1	10	100	1000	10000	100000	
'''