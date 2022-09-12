# -*-coding:utf-8 -*-
'''
@File    :   Opgave 2.8.py
@Time    :   2022/09/12 06:01:30
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
Voor gehele getallen is er nog een operator, de % (modulus). Die bepaald de modulus van twee getallen. (Modulus is in het Engels: remainder).

Voorbeeld 1: 23%6 geeft als resultaat 5. Want 6 gaat drie keer in 23 en dan blijft over 23 - 18 = 5.

Voorbeeld 2: 17%2 geeft als resultaat 1. Want 2 gaat acht keer in 17 en dan blijft over 17 - 16 = 1.

Voorbeeld 3: 16%2 geeft als resultaat 0. Want 2 gaat acht keer in 16 en dan blijft over 16 - 16 = 0.

Schrijf een programma dat als invoer twee gehele getallen a en b heeft en daarvan de modulus berekent en uitprint. Dus bereken a%b.

PS: Zorg dat je deze modulus goed leert beheersen, je gaat het vaker in opgaven nodig hebben!
'''

a = int(input("Vul eerste geheel getal in: "))
b = int(input("Vul tweede geheel getal in: "))
print("eerste getal % tweede getal = " + str(a % b))