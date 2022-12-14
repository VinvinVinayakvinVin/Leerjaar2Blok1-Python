# -*-coding:utf-8 -*-
'''
@File    :   Γpgaven 6.7.py
@Time    :   2022/10/22 10:06:12
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
7.ΒΆ
**  π  benaderen

De volgende vergelijking is bekend:

ββπ=11π6=π6945 
Dus kunnen wij  π6945  benaderen door:

βππ=11π6βπ6945 
a. Schrijf een programma, met input n, dat de volgende som berekend:  βππ=11π6
'''


import math


n = int(input("Vul een positief geheel getal in die groter dan 1 is voor n: "))
approx_sum = 0

for i in range(1, n + 1):
    approx_sum = approx_sum + (1 / pow(i, 6))

print("De benaderde uitkomst is: " + str(approx_sum))
print(f"Nu met deze: {pow(math.pi, 6) / 945}")

# De uitkomsten zijn vrijwel hetzelfde.



# Uitwerking voor a β¬οΈ:
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

# Opgave voor b β¬οΈ:
'''
b. Vul je programma aan en bepaal de benaderde waarde van Ο.
ps: vergelijk het eens met je math.pi voor verschillende invoer van n.
'''

pi = pow(approx_sum * 945, 1/6)
print("Benaderde pi waarde:", pi)
print("math.pi:" + str(math.pi))



# Uitwerking voor b β¬οΈ:
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