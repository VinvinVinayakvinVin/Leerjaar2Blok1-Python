# -*-coding:utf-8 -*-
'''
@File    :   Uitwerking 7.5.d.py
@Time    :   2022/11/07 12:03:27
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

#d
import math
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

def std(lijst):
    gemid = gemiddelde(lijst)
    n = len(lijst)
    som = 0
    for i in range(n):
        som = som + math.pow(lijst[i]-gemid, 2)
    return math.sqrt(som/n)
    
cijfers =[]

for line in lines:
    cijfer = int(line.split()[5]) 
    cijfers.append(cijfer)

print('Het gemiddelde cijfer is:',gemiddelde(cijfers))    
print('De standaarddeviatie is:', std(cijfers))
    
file.close



# Output:
'''
Het gemiddelde cijfer is: 6.891891891891892
De standaarddeviatie is: 1.9141547253649485
<function TextIOWrapper.close()>
'''