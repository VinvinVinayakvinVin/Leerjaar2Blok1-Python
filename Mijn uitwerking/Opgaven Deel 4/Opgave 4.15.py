# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.15.py
@Time    :   2022/10/18 12:45:19
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
4.15
** Belasting. Schrijf een programma met invoer een salaris (een getal).
De uitvoer is hoeveel belasting je jaarlijks over dit salaris moet afdragen volgens onderstaande tabel.

Salaris	Belastingtarief     # Dit moet een tabel voorstellen.
< €25.142	18,65%
€25.142 - €33.994	22,95%
€33.994 - €68.507	40,85%
> €68.507	51,95%


Het belastingtarief is het tarief dat je aan belasting moet betalen over alleen het bijbehorende salarisdeel.
Over de andere salarisdelen betaal je de andere bijbehorende tarieven.
Voorbeeld: iemand met een salaris van € 30.000 betaald aan belasting:
25.142∗18,65%+(30.000–25.142)∗22,95%=5.803,89
'''

salaris = float(input("Vul je salaris in: "))

if salaris < 25142:
    belasting = salaris * 0.1865
elif 25142 <= salaris < 33994:
    belasting = 25142 * 0.1865 + (salaris - 25142) * 0.2295
elif 33994 <= salaris < 68507:
    belasting = 25142 * 0.1865 + (33994 - 25142) * 0.2295 + (salaris - 33994) * 0.4085
else:
    belasting = 25142 * 0.1865 + (33994 - 25142) * 0.2295 + (68507 - 33994) * 0.4085 + (salaris - 68507) * 0.5195

print("Het te betalen belasting: " + str(belasting))

# Ik kon die opsommingen in variabelen zetten, nu staat er een heel lange statement bij else statement.
# Zie uitwerking wat ik boven bedoel. (zie maxtariefen in uitw.)

'''
# Uitwerking:

salaris = float(input('Geef het salaris: '))

maxtarief1 = 25142*18.65/100 #totale belasting t/m de eerste grens
maxtarief2 = maxtarief1 + (33994 - 25142)*22.95/100 #totale belasting t/m de tweede grens
maxtarief3 = maxtarief2 + (68507 - 33994)*40.85/100 #totale belasting t/m de derde grens

if salaris < 25142:
    print(salaris*18.65/100)
elif salaris < 33994:
    print(maxtarief1 + (salaris - 25142)*22.95/100)
elif salaris < 68507:
    print(maxtarief2 + (salaris - 33994)*40.85/100)
else:
    print(maxtarief3 + (salaris - 68507)*51.95/100)


# Output:
Geef het salaris: 30000
5803.894
'''