# -*-coding:utf-8 -*-
'''
@File    :   Opgave 9.1.py
@Time    :   2022/11/10 21:42:06
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
While loop oefeningΒΆ
1.  π  benaderen
De volgende relatie geldt:

ββπ=11π2=π26 
Hieruit kunnen we dus de waarde van  π  benaderen:

βππ=11π2=1+14+19+...+1π2βπ26 
** a. Hoeveel termen moeten we optellen zodat  π26  voldoende goed is benaderd? Als de nieuwe term  1π2  voldoende klein is tellen we er geen termen meer bij op. Wat we voldoende klein vinden, kunnen we zelf bepalen. Bijvoorbeeld, als de term  1π2<0.00001  dan worden er geen termen meer bij opgeteld.

In het algemeen geldt dus  1π2<πππππ , waarbij error dan een vooraf bekende kleine waarde is.

Bepaal nu de som  βππ=11π2  en tel net zolang termen op totdat  1π2<πππππ . Geef de variabele error zelf een waarde.
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
* b. Bepaal daarna ook de benaderde waarde voor  π
'''

print("Benaderde pi waarde:", (som*6)**(1/2))
print("Pi waarde vanuit math module:", math.pi)



# Uitwerking:
'''
pi = math.sqrt(som*6)

print('pi benadering     :', pi) 
print('pi uit math module:', math.pi)
'''