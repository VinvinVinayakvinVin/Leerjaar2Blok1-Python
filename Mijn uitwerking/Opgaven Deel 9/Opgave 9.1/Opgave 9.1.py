# -*-coding:utf-8 -*-
'''
@File    :   Opgave 9.1.py
@Time    :   2022/11/10 21:42:06
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
While loop oefening¶
1.  𝜋  benaderen
De volgende relatie geldt:

∑∞𝑘=11𝑘2=𝜋26 
Hieruit kunnen we dus de waarde van  𝜋  benaderen:

∑𝑛𝑘=11𝑘2=1+14+19+...+1𝑛2≈𝜋26 
** a. Hoeveel termen moeten we optellen zodat  𝜋26  voldoende goed is benaderd? Als de nieuwe term  1𝑛2  voldoende klein is tellen we er geen termen meer bij op. Wat we voldoende klein vinden, kunnen we zelf bepalen. Bijvoorbeeld, als de term  1𝑛2<0.00001  dan worden er geen termen meer bij opgeteld.

In het algemeen geldt dus  1𝑛2<𝑒𝑟𝑟𝑜𝑟 , waarbij error dan een vooraf bekende kleine waarde is.

Bepaal nu de som  ∑𝑛𝑘=11𝑘2  en tel net zolang termen op totdat  1𝑛2<𝑒𝑟𝑟𝑜𝑟 . Geef de variabele error zelf een waarde.
'''

import math


error = 0.0000000001
teller = 0
term = 1
som = 0

while term > error:
    teller += 1
    term = 1 / teller**2
    som += term

print("Benadering:", som)
print("Teller staat op:", teller)
print("Math module: ", (math.pi ** 2 / 6))



# Uitwerking:
'''
import math

err = 0.0000000001

som = 0
k = 1
term = 1

while term > err:
    term = 1/(k*k)
    som = som + term
    k = k + 1
'''



'''
* b. Bepaal daarna ook de benaderde waarde voor  𝜋
'''

print("Benaderde pi waarde:", (som*6)**(1/2))
print("Pi waarde vanuit math module:", math.pi)



# Uitwerking:
'''
pi = math.sqrt(som*6)

print('pi benadering     :', pi) 
print('pi uit math module:', math.pi)
'''