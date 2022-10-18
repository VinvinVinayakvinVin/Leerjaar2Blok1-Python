# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.14.py
@Time    :   2022/10/18 11:32:19
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
4.14 ¶
*** Schrijf een programma met invoer een aantal minuten (een getal dus). 
De uitvoer is hoeveel dagen, resterende uren en resterende minuten hierin zitten.

vb: in 3.005 minuten zitten 2 dagen, 2 uur en 5 minuten. 
Laat je uitvoer ook zo een soortgelijke zin zijn.
'''

input_min = float(input("Vul aantal minuten in: "))     # Ik kon misschien beter gewoon de variabelnaam totaal_minuten noemen.
dagen = input_min // (24*60)
uren = (input_min - dagen * (24*60)) // 60
minuten = input_min - dagen * (24*60) - uren * 60

print(f"Aantal dagen = {dagen}")
print(f"Aantal uren = {uren}")
print(f"Aantal minuten = {minuten}")


'''
# Uitwerking:

totaal_minuten = int(input('Vul het aantal minuten in: '))

#manier 1:
dagen = int(totaal_minuten/(24 * 60))
uren = int((totaal_minuten - (dagen*24*60))/60)
minuten = int(totaal_minuten - (dagen * 24 * 60) - (uren * 60))

print(f'In {totaal_minuten} minuten zitten {dagen} dagen, {uren} uur en {minuten} minuten')

# output 1:

Vul het aantal minuten in: 3005
In 3005 minuten zitten 2 dagen, 2 uur en 5 minuten


totaal_minuten = int(input('Vul het aantal minuten in: '))

#manier 2:
dagen = totaal_minuten//(24*60)
uren = (totaal_minuten - (dagen * 24 * 60))//60
minuten = totaal_minuten%60

print(f'In {totaal_minuten} minuten zitten {dagen} dagen, {uren} uur en {minuten} minuten')


# output 2:

Vul het aantal minuten in: 3005
In 3005 minuten zitten 2 dagen, 2 uur en 5 minuten
'''