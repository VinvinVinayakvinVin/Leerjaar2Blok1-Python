# -*-coding:utf-8 -*-
'''
@File    :   Uitwerking 7.5.c.py
@Time    :   2022/11/07 11:41:51
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

#c
import os


os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.5.c\\")
file = open('Klas.txt')

eersteregel = file.readline() # Eerst deze regel inlezen, want dat zijn de koppen
lines = file.readlines() # De koppen worden nu niet nog een keer gelezen!

def gemiddelde(lijst):
    som = 0
    n = len(lijst)
    for i in range(n):
        som = som + lijst[i]
    return som / n

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

        
print('Het aantal jongens is:', jteller)
print('Gemiddelde leeftijd van de jongens is: ', gemiddelde(jleeftijden))
print('Gemiddelde lengte van de jongens is: ', gemiddelde(jlengtes))
print('Gemiddelde gewicht van de jongens is: ', gemiddelde(jgewichten))
print('Gemiddelde cijfer van de jongens is: ', gemiddelde(jcijfers), '\n')

print('Het aantal meisjes is:', mteller)
print('Gemiddelde leeftijd van de meisjes is: ', gemiddelde(mleeftijden))
print('Gemiddelde lengte van de meisjes is: ', gemiddelde(mlengtes))
print('Gemiddelde gewicht van de meisjes is: ', gemiddelde(mgewichten))
print('Gemiddelde cijfer van de meisjes is: ', gemiddelde(mcijfers))
    
file.close



# Output:
'''
Het aantal jongens is: 18
Gemiddelde leeftijd van de jongens is:  19.0
Gemiddelde lengte van de jongens is:  178.33333333333334
Gemiddelde gewicht van de jongens is:  78.0
Gemiddelde cijfer van de jongens is:  7.222222222222222 

Het aantal meisjes is: 19
Gemiddelde leeftijd van de meisjes is:  19.68421052631579
Gemiddelde lengte van de meisjes is:  170.57894736842104
Gemiddelde gewicht van de meisjes is:  61.1578947368421
Gemiddelde cijfer van de meisjes is:  6.578947368421052
<function TextIOWrapper.close()>
'''