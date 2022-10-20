# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.1.py
@Time    :   2022/10/20 06:57:30
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
1.
* Maak in Python de volgende lijst (handmatig) aan:

[‘Amerikaanse Zeearend’, ‘Zeearend’, ‘Steenarend’, ‘Apenarend’, ‘Kip’, ‘Buizerd’]

Noem deze lijst arenden.

a. Print de lijst arenden uit.
b. Print het 3e element van de lijst arenden uit.
c. Iemand heeft een fout gemaakt in de lijst: een kip is geen arend. I.p.v. kip had er Kroonarend moeten staan.
Zorg ervoor dat je met een statement ‘Kip’ vervangt door de naam ‘Kroonarend’.

Print arenden nogmaals uit en controleer of de lijst juist is aangepast.

Hint: arenden[…] = …
'''

# a:
arenden = ['Amerikaanse Zeearend', 'Zeearend', 'Steenarend', 'Apenarend', 'Kip', 'Buizerd']

print("#a")
for i in arenden:
    print(i)

# b:
print("\n#b\n"+arenden[3-1]) # Dit print "Zeearend" uit.

# c:
arenden[5-1] = "Kroonarend"
print("\n#c\n" + arenden[4])

# (soort van d):
print("\n#d")
for i in arenden:
    print(i)


'''
# Uitwerking:

#maak de lijst
arenden = ['Amerikaanse Zeearend', 'Zeearend', 'Steenarend', 'Apenarend', 'Kip', 'Buizerd']

#a
print(arenden)

#b
print(arenden[2]) # Index is eentje lager omdat indices vanaf 0 beginnen te tellen

#c
arenden[4] = 'Kroonarend' # Lijsten zijn 'mutable' (veranderlijk, je kunt ze aanpassen)
print(arenden)


# # Output:

# ['Amerikaanse Zeearend', 'Zeearend', 'Steenarend', 'Apenarend', 'Kip', 'Buizerd']
# Steenarend
# ['Amerikaanse Zeearend', 'Zeearend', 'Steenarend', 'Apenarend', 'Kroonarend', 'Buizerd']
'''

# Ik kon ook zonder de for loop gebruiken 😂
arenden = ['Amerikaanse Zeearend', 'Zeearend', 'Steenarend', 'Apenarend', 'Kip', 'Buizerd']
print("\n" + str(arenden))  # Let op, arenden is een list type, niet string type. Vandaar dat ik het str function heb gebruikt.
arenden[5-1] = "Kroonarend"
print(arenden[4])
print(arenden)