# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.2.py
@Time    :   2022/09/27 20:06:50
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* Schrijf een programma met invoer je leeftijd als een geheel getal en dat als uitvoer de volgende tekst geeft:

Als je leeftijd kleiner is dan 12: “Je bent een pupil.”

Als je leeftijd gelijk of groter is dan 12 maar kleiner dan 18: “Je bent een junior.”

Voor de overige leeftijden: “Je bent een senior.”
'''

leeftijd = int(input("Vul je leeftijd in: "))

if leeftijd < 12:
    print("Je bent een pupil.")
elif 12 <= leeftijd < 18:           # Ik kan ook code gebruiken van: 'elif leeftijd >= 12 and leeftijd < 18'❗
    print("Je bent een junior.")
else:
    print("Je bent een senior.")


'''
# Uitwerking:

#Geef leeftijd als input en maar daar een geheel getal van
leeftijd = int(input('Leeftijd: '))

if leeftijd < 12:                       #als leeftijd < 12
    print('Je bent een pupil.')         #print dan 'pupil'
elif leeftijd >= 12 and leeftijd < 18:  #anders, als 12 <= leeftijd <= 18
    print('Je bent een junior.')        #print dan 'junior'
else:                                   #in alle andere gevallen
    print('Je bent een senior.')        #print dan 'senior'


# Output:

Leeftijd: 21
Je bent een senior.
'''