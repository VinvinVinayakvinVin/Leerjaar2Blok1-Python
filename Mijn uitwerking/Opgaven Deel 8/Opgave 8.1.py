# -*-coding:utf-8 -*-
'''
@File    :   Opgave 8.1.py
@Time    :   2022/11/07 12:54:52
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
1.¶
* Schrijf een programma dat Hello, World! tienmaal onder elkaar uitprint (nu met een while-loop).
'''

i = 0
while i < 10:         # vanaf 1 t/m 10
    i = i + 1
    print("hi", i)

print()

j = 1
while j <= 10:        # vanaf 2 t/m 11
    j += 1
    print("hi", j)

print()

i = 1
while i <= 10:        # vanaf 1 t/m 10
  print('Hello, World!', i)
  i += 1



# Uitwerking:
'''
i = 1
while i <= 10:
  print('Hello, World!')
  i += 1



# Output:
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
'''