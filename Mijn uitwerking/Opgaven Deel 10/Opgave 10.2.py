# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.2.py
@Time    :   2022/11/13 14:39:33
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
2. Lees par 8.4: String Slices¶
* a. Schrijf een programma dat van de volgende zin 'Netflixen en bingewatchen' alleen 'Netflixen' uitprint.

* b. Schrijf een programma dat van de volgende zin 'Netflixen en bingewatchen' alleen 'bingewatchen' uitprint.
'''

# a:
txt = 'Netflixen en bingewatchen'
print(txt.split()[0])

# b:
print(txt.split()[2])



# Uitwerking:
'''
# a.
#print de eerste 9 karakters van de string
print('Netflixen en bingewatchen'[:9])

# b.
#print vanaf het 13e karakter van de string
print('Netflixen en bingewatchen'[13:])



# # Output:
# Netflixen
# bingewatchen
'''

# a opnieuw:
print(txt[:9])  # 1=N, 2=e, 3=t, ..., 9=n, 10=" ".

# b opnieuw:
print(txt[13:])

# Wat nou als ik alleen het woord 'bingewatch' uit print, in plaats van 'bingewatchen':
print(txt[13:][:10])
print(txt[13:].replace("en", ""))