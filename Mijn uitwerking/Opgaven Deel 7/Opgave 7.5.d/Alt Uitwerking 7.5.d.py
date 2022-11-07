# -*-coding:utf-8 -*-
'''
@File    :   Alt Uitwerking 7.5.d.py
@Time    :   2022/11/07 12:04:57
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

#En nu met bestaande functies

import statistics
import os

os.chdir(os.getcwd() + "\\Mijn uitwerking\\Opgaven Deel 7\\Opgave 7.5.c\\")
file = open('Klas.txt')

eersteregel = file.readline() # Eerst deze regel inlezen, want dat zijn de koppen
lines = file.readlines() # De koppen worden nu niet nog een keer gelezen!

cijfers =[]

for line in lines:
    cijfer = int(line.split()[5]) 
    cijfers.append(cijfer)

print('Het gemiddelde cijfer is:', statistics.mean(cijfers))    
print('De standaarddeviatie is:', statistics.stdev(cijfers))        # stdev gebruikt niet populatie, maar steekproef
                                                                    # Dus i.p.v N, wordt het n-1 in het formule gebruikt!
    
file.close



# Output:
'''
Het gemiddelde cijfer is: 6.891891891891892
De standaarddeviatie is: 1.9405581067738646
<function TextIOWrapper.close()>
'''