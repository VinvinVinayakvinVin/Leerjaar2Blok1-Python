# -*-coding:utf-8 -*-
'''
@File    :   Òpgaven 6.7.py
@Time    :   2022/10/22 10:06:12
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
7.¶
**  𝜋  benaderen

De volgende vergelijking is bekend:

∑∞𝑘=11𝑘6=𝜋6945 
Dus kunnen wij  𝜋6945  benaderen door:

∑𝑛𝑘=11𝑘6≈𝜋6945 
a. Schrijf een programma, met input n, dat de volgende som berekend:  ∑𝑛𝑘=11𝑘6
'''


import math


n = int(input("Vul een positief geheel getal in die groter dan 1 is voor n: "))
approx_sum = 0

for i in range(1, n + 1):
    approx_sum = approx_sum + (1 / pow(i, 6))

print("De benaderde uitkomst is: " + str(approx_sum))
print(f"Nu met deze: {pow(math.pi, 6) / 945}")

# De uitkomsten zijn vrijwel hetzelfde.



# Uitwerking voor a ⬇️:
'''
#a
import math

n = int(input('Vul een geheel getal in\n'))

som = 0

for i in range(1, n + 1):
    som = som + 1/math.pow(i, 6)
    
print(som) 



# # Output:

# Vul een geheel getal in
# 7
# 1.0173348160677427
'''

# Opgave voor b ⬇️:
'''
b. Vul je programma aan en bepaal de benaderde waarde van π.
ps: vergelijk het eens met je math.pi voor verschillende invoer van n.
'''

pi = pow(approx_sum * 945, 1/6)
print("Benaderde pi waarde:", pi)
print("math.pi:" + str(math.pi))



# Uitwerking voor b ⬇️:
'''
#b
import math

n = int(input('Vul een geheel getal in\n'))

som = 0

for i in range(1, n + 1):
    som = som + 1/math.pow(i, 6)

#Dit is de benadering van pi. pi kun je herleiden uit de sommatie dat in de opgave is gegeven.
pi_ben = math.pow(som*945, 1/6)    
    
print(pi_ben) 
print(math.pi)



# # Output:

# Vul een geheel getal in
# 9
# 3.141591341408046
# 3.141592653589793
'''