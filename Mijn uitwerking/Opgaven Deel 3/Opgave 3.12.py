# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.12.py
@Time    :   2022/09/23 21:37:17
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
** Rentenieren II. Iemand wil bij een bank sparen. Over n jaar wil de persoon een bedrag van x euro ontvangen. 
De vaste rekenrente is r (in procenten, dus r = 2,5 betekent 2,5%). 
Schrijf een programma met drie invoervariabelen n, x en r en dat daarna de contante waarde berekent op t = 0 en uitprint.

Opmerking: Deze opgave krijgt ** sterren, omdat je wiskundig eerst moet bepalen wat je überhaupt moet doen.
'''

n = float(input("Vul het aantal jaren, wanneer je je bedrag ontvangt: "))
x = float(input(f"Vul nu het bedrag in, die je over {n} jaar ontvangt: "))
r = float(input("Als laatste, vul de rekenrente in percentage (De percentage teken zet je hierbij niet): "))
berekening = x/(1+r/100)**n
print(f"Op tijdstip 0, is de bedrag {berekening} waard.")
# ⬆️ Ik heb hierbij niet veel opgelet op het maken van de tekst [    ik luister muziek ;)    ]

'''
Uitwerking:

n = int(input('Geef het aantal jaren n: '))  # float() gebruiken als je ook niet gehele jaren wil invoeren!
x = float(input('Geef het te bereiken doel x: '))
r = float(input('Geef de rekenrente in procenten r: '))

CW = x/(1.0 + r/100.0) ** n

print(CW)

# uitkomst:
# Geef het aantal jaren n: 5
# Geef het te bereiken doel x: 10000
# Geef de rekenrente in procenten r: 2
# 9057.30809829916
'''