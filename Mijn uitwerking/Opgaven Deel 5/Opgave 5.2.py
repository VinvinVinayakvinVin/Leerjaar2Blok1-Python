# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.2.py
@Time    :   2022/10/20 07:11:29
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
2.¶
* Schrijf een programma met als invoervariabele een geheel getal n en maak in je programma (handmatig) de volgende lijst aan:

cijfers = [5.0, 6.5, 1.0, 5.5, 2.5]

Je programma print het n-de element van deze lijst uit. Bijvoorbeeld: 'Het 2e element is 6.5.'

Als je een n invoert groter dan 5 of kleiner dan 0, dan moet er een melding komen dat n ligt tussen [1, 5].
'''

n = int(input("Vul een geheel getal in: "))     # Ik zou dit veranderen naar -> "Vul een geheel getal in tussen 1 t/m 5".
cijfers = [5.0, 6.5, 1.0, 5.5, 2.5]

if 1 <= n <= 5:
    print(cijfers[n-1])
else:
    print("Getal n zit niet tussen 1 en 5 (inclusief grensen).")


'''
# Uitwerking:

#Maak de lijst
cijfers = [5.0, 6.5, 1.0, 5.5, 2.5]

#Geef een geheel getal op
n = int(input('Vul een geheel getal in tussen 1 tm 5\n'))

#Als n in [1, 5] ligt, print dan het n-de element anders, geef een melding 
if 1 <= n <= 5:
    print(cijfers[n-1])
else:
    print('Je getal moet tussen 1 en 5 zitten en geheel zijn.\n')


# # Output:

# Vul een geheel getal in tussen 1 tm 5
# 4
# 5.5    
'''