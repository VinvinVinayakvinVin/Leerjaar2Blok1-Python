# -*-coding:utf-8 -*-
'''
@File    :   Alt Uitwerking 7.5.c.py
@Time    :   2022/11/07 11:43:27
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

#Nu zonder de zelfgemaakte functie en een andere print statement.
#Er bestaat ook een functie om het gemiddelde van een list te bepalen. Gebruik de mean functie uit de statistics module.

import os
import statistics

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.5.c\\")
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

jteller = 0
mteller = 0

for line in lines:
    geslacht = line.split()[1]
    leeftijd = int(line.split()[2])
    lengte = int(line.split()[3])
    gewicht = int(line.split()[4])
    cijfer = int(line.split()[5])  
    if geslacht == 'jongen':
        jteller = jteller + 1
        jleeftijden.append(leeftijd)
        jlengtes.append(lengte)
        jgewichten.append(gewicht)
        jcijfers.append(cijfer)
    else:
        mteller = mteller + 1
        mleeftijden.append(leeftijd)
        mlengtes.append(lengte)
        mgewichten.append(gewicht)
        mcijfers.append(cijfer)

print(f"""
Het aantal jongens is                : {jteller},
Gemiddelde leeftijd van de jongens is: {statistics.mean(jleeftijden)},
Gemiddelde lengte van de jongens is  : {statistics.mean(jlengtes)},
Gemiddelde gewicht van de jongens is : {statistics.mean(jgewichten)},
Gemiddelde cijfer van de jongens is  : {statistics.mean(jcijfers)}.""") 

print(f"""
Het aantal meisjes is                : {mteller},
Gemiddelde leeftijd van de meisjes is: {statistics.mean(mleeftijden)},
Gemiddelde lengte van de meisjes is  : {statistics.mean(mlengtes)},
Gemiddelde gewicht van de meisjes is : {statistics.mean(mgewichten)},
Gemiddelde cijfer van de meisjes is  : {statistics.mean(mcijfers)}.""") 
    
file.close



# Output:
'''
Het aantal jongens is                : 18,
Gemiddelde leeftijd van de jongens is: 19,
Gemiddelde lengte van de jongens is  : 178.33333333333334,
Gemiddelde gewicht van de jongens is : 78,
Gemiddelde cijfer van de jongens is  : 7.222222222222222.

Het aantal meisjes is                : 18,
Gemiddelde leeftijd van de meisjes is: 19.68421052631579,
Gemiddelde lengte van de meisjes is  : 170.57894736842104,
Gemiddelde gewicht van de meisjes is : 61.1578947368421,
Gemiddelde cijfer van de meisjes is  : 6.578947368421052.
<function TextIOWrapper.close()>
'''