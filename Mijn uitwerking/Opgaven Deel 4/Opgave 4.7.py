# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.7.py
@Time    :   2022/09/27 21:44:08
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
*** Boolean Expressions

We hebben vier variabelen a, b, c en d van het type boolean.
De (boolean) expressie a and b geeft als resultaat True als a en b beide True zijn, anders False.
Als we een (boolean) expressie willen opstellen die alleen True is als a True is en b False krijgen we dit: a and not b.

In deze opgave moet je een aantal boolean expressions opstellen. Dit mag ook met pen en papier.
Stel een boolean expressie op waarvoor geldt:

1. Als de variabele a False is dan moet de expressie True zijn, anders False.
2. Als minstens één van de variabelen a, b True is dan moet de uitvoer True zijn, anders False.
3. Als minstens één van de variabelen a, b, c True is dan moet de uitvoer True zijn, anders False.
4. Als beide variabelen a, b False zijn dan moet de uitvoer True zijn, anders False.
5. We gebruiken nu vier variabelen van type boolean, a, b, c en d. De uitvoer van de expressie moet zijn:

True als:
a en b zijn beide True én c en d zijn beide False
of
a en b zijn beide False én c en d zijn beide True

False als:
Alle andere varianten
'''

# Part 1:
# 1. Als de variabele a False is dan moet de expressie True zijn, anders False.
a = True
print("Part 1.\nDe waarde van niet a is:", not a)


# Part 2:
# 2. Als minstens één van de variabelen a, b True is dan moet de uitvoer True zijn, anders False.
a = False
b = True

print(f"Part 2.\n{a} or {b} == {a or b}")


# Part 3:
# 3. Als minstens één van de variabelen a, b, c True is dan moet de uitvoer True zijn, anders False.
a = False
b = False
c = True

print("Part 3.\n" + f"De waarde van {a} or {b} or {c} is", a or b or c)


# Part 4:
# 4. Als beide variabelen a, b False zijn dan moet de uitvoer True zijn, anders False.
a = False
b = False
print("Part 4.\n" + f"not ({a} or {b}) is " + str(not (a or b)))

# ⬆️ opmerking, ik koon ook (not a and not b) doen 💪🥸☝️

# Part 5:
# 5. We gebruiken nu vier variabelen van type boolean, a, b, c en d. De uitvoer van de expressie moet zijn:
# True als:
# a en b zijn beide True én c en d zijn beide False
# of
# a en b zijn beide False én c en d zijn beide True
# False als:
# Alle andere varianten
a = True
b = True
c = False
d = False

print("Part 5.\n" + f"a = {a}\nb = {b}\nc = {c}\nd = {d}.\n((a and b) and not(c or d)) or (not(a or b) and (c and d)) = ⬇️")
print(f"(({a} and {b}) and not({c} or {d})) or (not({a} or {b}) and ({c} and {d})) = ⬇️")
print(((a and b) and not (c or d)) or (not (a or b) and (c and d)))

# ⬆️ opmerking, net zoals bij vraag 4 van dit opgave, kon je ook die (not x and not y) methode gebruiken.
# uitwerking zegt: 'print('vraag 5: ' + str((a and b and not c and not d) or (not a and not b and c and d)))'.

'''
# Uitwerking:

#Zie voor deze opgave ook de slides van les 1.2 onder de kop 'waarheids waarden'

#1
a = False
print('vraag 1: ' + str(not a)) #als a False is moet de expressie True zijn. Expressie 'not a' geeft het tegenovergestelde van a

a = True
print('vraag 1: ' + str(not a)) #Probeer het wanneer a True is

#2
#Probeer zelf ook andere combinaties van true en false voor a en b en controleer of de expressie nog klopt
a = True
b = False

print('vraag 2: ' + str(a or b)) #a OF b is true als minstens een van de twee true is

#3
a = False
b = False
c = True

print('vraag 3: ' + str(a or b or c)) 


#4
#Probeer ook andere combinaties voor a en b
a = False
b = False

print('vraag 4: ' + str(not a and not b))

#5
a = False
b = False
c = True
d = True

print('vraag 5: ' + str((a and b and not c and not d) or (not a and not b and c and d)))


# Output:

# vraag 1: True
# vraag 1: False
# vraag 2: True
# vraag 3: True
# vraag 4: True
# vraag 5: True
'''