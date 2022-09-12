# -*-coding:utf-8 -*-
'''
@File    :   Opgave 2.7.py
@Time    :   2022/09/12 05:56:14
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
Schrijf een programma dat als invoer twee getallen heeft en waarvan het eerste getal een geheel getal is en het tweede een decimaal getal. 
Je programma print dan de onderstaande zin:

“Ik heb het getal [getal1] en het getal [getal2] ingetypt.”
'''

eerste_getal = int(input("Type een geheel getal in: "))
tweede_getal = float(input("Type nu een decimaal getal in: "))
print(f"Ik heb het getal {eerste_getal} en het getal {tweede_getal} ingetypt.")
# print("Ik heb het getal " + str(eerste_getal) + " en het getal " + str(tweede_getal) + " ingetypt.")  # Ik kon ook deze doen, maar wat ik heb is sneller.
