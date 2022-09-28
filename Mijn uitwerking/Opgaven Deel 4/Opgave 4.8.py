# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.8.py
@Time    :   2022/09/28 15:35:42
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
** Schrijf een programma dat als invoer drie gehele getallen a, b en c heeft en de uitvoer is True alleen als c tussen a en b ligt,
zo niet dan is de uitvoer False. De grenzen tellen mee, dus [a, b].

Probeer je code zo kort mogelijk te houden!
'''

a = int(input("Vul een geheel getal in voor a: "))
b = int(input("Vul een geheel getal in voor b: "))
c = int(input("Vul een geheel getal in voor c: "))

# If statement, als c tussen a en b ligt, dan print eruit "c ligt tussen a en b.", anders print het uit "c ligt niet tussen a en b."
if a <= c <= b or b <= c <= a:
    print("c ligt tussen a en b.")
else:
    print("c ligt niet tussen a en b.")

'''
# Uitwerking:

a = int(input('Vul getal a in: '))
b = int(input('Vul getal b in: '))
c = int(input('Vul getal c in: '))

print(a <= c <= b) # Je hoeft in je print-statement dus helemaal niet de woorden True of False te gebruiken! 
                   # De boolean expressie wordt zelf namelijk al True of False. Er is dus ook geen if-else nodig.


# Output:

# Vul getal a in: 6
# Vul getal b in: 1
# Vul getal c in: 3
# False
'''

# De uitwerking is inderdaad wat korter dan wat ik heb.
# Maar ik heb juist wat robuuster code 😁