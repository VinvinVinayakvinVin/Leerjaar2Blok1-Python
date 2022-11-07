# -*-coding:utf-8 -*-
'''
@File    :   Uitwerking 7.5.py
@Time    :   2022/11/07 10:24:46
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

#b
file = open('Klas.txt')

eersteregel = file.readline() # Eerst deze regel inlezen, want dat zijn de koppen
lines = file.readlines() # De koppen worden nu niet nog een keer gelezen!

jleeftijden = []
jlengtes = []
jgewichten = []
jcijfers =[]

mleeftijden = []
mlengtes = []
mgewichten = []
mcijfers =[]

for line in lines:
    geslacht = line.split()[1]
    leeftijd = int(line.split()[2])
    lengte = int(line.split()[3])
    gewicht = int(line.split()[4])
    cijfer = int(line.split()[5]) 
    if geslacht == 'jongen':
        jleeftijden.append(leeftijd)
        jlengtes.append(lengte)
        jgewichten.append(gewicht)
        jcijfers.append(cijfer)
    else:
        mleeftijden.append(leeftijd)
        mlengtes.append(lengte)
        mgewichten.append(gewicht)
        mcijfers.append(cijfer)

print(jleeftijden)
print(jlengtes)
print(jgewichten)
print(jcijfers)

print(mleeftijden)
print(mlengtes)
print(mgewichten)
print(mcijfers)
    
file.close


# Output:
'''
[17, 19, 19, 17, 21, 20, 20, 18, 19, 18, 20, 21, 17, 20, 21, 20, 17, 18]
[171, 172, 194, 165, 167, 183, 176, 198, 178, 195, 186, 175, 170, 175, 167, 169, 169, 200]
[67, 63, 71, 99, 96, 65, 61, 81, 68, 75, 74, 96, 98, 54, 99, 70, 84, 83]
[10, 6, 8, 8, 8, 4, 8, 5, 7, 5, 10, 7, 9, 5, 7, 6, 10, 7]
[18, 21, 19, 21, 21, 21, 18, 18, 17, 20, 18, 20, 21, 20, 21, 18, 21, 21, 20]
[160, 167, 185, 161, 185, 157, 158, 176, 167, 181, 171, 173, 176, 161, 169, 177, 179, 156, 182]
[78, 70, 79, 51, 54, 45, 72, 58, 55, 73, 59, 65, 59, 70, 51, 60, 56, 52, 55]
[8, 8, 10, 7, 6, 7, 6, 8, 4, 7, 6, 6, 4, 4, 10, 10, 5, 5, 4]
<function TextIOWrapper.close()>
'''