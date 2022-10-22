# -*-coding:utf-8 -*-
'''
@File    :   Opgave 6.6.py
@Time    :   2022/10/22 09:43:18
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
For-loops
Hieronder volgen een aantal opgaven over for-loops.

6.
In opgave 5 zagen we dat een string een iterable is. 
Een string kunnen we dus lezen alsof het een lijst is (strict gezien is dit niet zo, dat komt later in de cursus aan bod). 
En de elementen in die lijst zijn de letters van de tekst. Deze kennis gaan we nu combineren met een for-loop.

* a. Voer onderstaande code uit.

ps: voor letter had je ook i of x kunnen zetten. Echter voor overzicht/duidelijkheid is de naam letter geschikter. 
Je gaat in principe ook echt elke letter langs van het woord ‘appel’.
'''

# effectief manier om te doen.
for letter in 'appel':
    print(letter)
print("\n")

# alternatief.
woord = "appel"
for i in range (len("appel")):
    print(woord[i])
print("\n\n\n")

# Uitwerking voor a ⬇️
'''
for letter in 'appel':
    print(letter)


# # Output:

# a
# p
# p
# e
# l
'''

# Opdracht b ⬇️
'''
* b. Print elke letter van de volgende zin onder elkaar uit:
'De koopkracht stijgt het komende jaar gemiddeld met 0,1 procent, 
volgens de ramingen van het ministerie van Sociale Zaken en Werkgelegenheid.'
'''

zin = """De koopkracht stijgt het komende jaar gemiddeld met 0,1 procent, 
volgens de ramingen van het ministerie van Sociale Zaken en Werkgelegenheid."""

for letter in zin:
    print(letter)

# Uitwerking voor b ⬇️

'''
zin = 'De koopkracht stijgt het komende jaar gemiddeld met 0,1 procent, volgens de ramingen van het ministerie van Sociale Zaken en Werkgelegenheid.'

for letter in zin:
    print(letter)

# # Output:

# D
# e
 
# k
# o
# o
# p
# k
# r
# a
# c
# h
# t
 
# s
# t
# i
# j
# g
# t
 
# h
# e
# t
 
# k
# o
# m
# e
# n
# d
# e
 
# j
# a
# a
# r
 
# g
# e
# m
# i
# d
# d
# e
# l
# d
 
# m
# e
# t
 
# 0
# ,
# 1
 
# p
# r
# o
# c
# e
# n
# t
# ,
 
# v
# o
# l
# g
# e
# n
# s
 
# d
# e
 
# r
# a
# m
# i
# n
# g
# e
# n
 
# v
# a
# n
 
# h
# e
# t
 
# m
# i
# n
# i
# s
# t
# e
# r
# i
# e
 
# v
# a
# n
 
# S
# o
# c
# i
# a
# l
# e
 
# Z
# a
# k
# e
# n
 
# e
# n
 
# W
# e
# r
# k
# g
# e
# l
# e
# g
# e
# n
# h
# e
# i
# d
# .
'''

# Opdracht c ⬇️
'''
** c. Maak een nieuw programma dat bepaalt hoe vaak de letter e in de zin bij 6b zit.
Hint: if statement nodig en een variabele (teller) die telt hoeveel e’s er zijn.
'''

teller = 0
for letter in zin:
    if letter == 'e':
        teller = teller + 1
        # teller += 1     # Zelfde als teller = teller + 1
        # teller =+ 1     # <-- Dit is fout, hier wordt gezegd, dat teller is gelijk aan 1, (misschien kan dit goed zijn, als zin 1 letter 'e' bevat).
print("Er zijn", teller, "e's in de zin.")



# Uitwerking voor c ⬇️

'''
zin = 'De koopkracht stijgt het komende jaar gemiddeld met 0,1 procent, volgens de ramingen van het ministerie van Sociale Zaken en Werkgelegenheid.'

teller = 0

for letter in zin:
    if letter == 'e':
        teller = teller + 1

print(teller)   



# Output:
# output is er niet in de uitwerking...

'''

# Opdracht d ⬇️

'''
** d. Breid 6c uit met dat je als input meegeeft welke letter (of symbool) geteld wordt. Dus niet standaard de letter e meer.
'''

which_letter = input("Vul een letter die je wilt laat tellen :D\n")
teller = 0
for letter in zin:
    if letter == which_letter:
        teller = teller + 1
        # teller += 1     # Zelfde als teller = teller + 1
        # teller =+ 1     # <-- Dit is fout, hier wordt gezegd, dat teller is gelijk aan 1, (misschien kan dit goed zijn, als zin 1 letter 'e' bevat).
print("Er zijn", teller, f"{which_letter}'s in de zin.")



# Uitwerking voor d ⬇️
'''
zin = 'De koopkracht stijgt het komende jaar gemiddeld met 0,1 procent, volgens de ramingen van het ministerie van Sociale Zaken en Werkgelegenheid.'

invoer_letter = input('Type letter of symbool in\n')

#teller om bij te houden hoe vaak de opgegeven letter voorkomt
teller = 0

for letter in zin:
    if letter == invoer_letter:
        teller = teller + 1 #verhoog de teller met 1 als de huidige letter gelijk is aan de opgegeven letter

print(invoer_letter + ' komt ' + str(teller) + ' keer voor in de zin')   
'''