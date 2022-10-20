# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.5.py
@Time    :   2022/10/20 15:13:54
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
5.¶
* For-loop met range() statement

a. Schrijf een programma dat ‘Hello, World!’ tienmaal onder elkaar uitprint. (Nu met een for-loop en de range() statement).
'''

for i in range(10):
    print("Hello, World!")

'''
b. Schrijf een programma met invoervariabele een geheel getal n en dat ‘Hello, World!’ n-maal onder elkaar uitprint.
'''

n = int(input("Vul een geheel getal in: "))

for i in range(n):
    print("Hello, World!")


'''
# Uitwerking a:

#a
#range(10) geeft een reeks van getallen van 0 t/m 9
for i in range(10):
    print('Hello, World!')


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


# Uitwerking b:
 
#b
n = int(input('Vul een geheel getal in\n'))

for i in range(n):
    print('Hello, World!')


# Output:

# Vul een geheel getal in
# 3
# Hello, World!
# Hello, World!
# Hello, World!
'''