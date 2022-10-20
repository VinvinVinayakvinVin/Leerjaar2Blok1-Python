# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.18.py
@Time    :   2022/10/20 06:29:37
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
4.18¶
!! * pass statement en # TODO:

Tijdens het programmeren zijn er soms onderdelen van het programma die je later wil maken, afmaken of aanvullen.
Echter als je een programma uitvoert moet gelijk de hele code kloppen en kun je niet tot later wachten met afmaken.
Gelukkig zijn er manieren om dit toch te kunnen doen: m.b.v. het zogenaamde pass statement. Dit werkt o.a. bij if, elif en else.
Zie voorbeeld code hieronder:
'''

'''
getal = int(input('Vul een geheel getal in\n'))

if getal >0:
    print('Het ingevulde getal is positief\n')
elif getal == 0:
    pass #TODO: Uitzoeken of 0 positief of negatief of geen van beide is
else:
    print('Het ingevulde getal is negatief\n')
'''

'''
Misschien weet je niet of 0 als positief of negatief wordt beschouwd en wil je dit later uitzoeken.
Maar nu wil je controleren of de code werkt. Als je als invoer 0 opgeeft dan kom je uit bij de elif, want getal == 0.
De pass statement geeft de computer de instructie om bij die elif even niets uit te voeren
en door te gaan met de rest van de code (die hier niet is afgebeeld overigens). 
Dus ondanks dat je nog geen code hebt bedacht die bij de elif moet komen staan, 
kun je je programma dankzij de pass statement toch uitvoeren.

Opmerking: Als je later iets wil afmaken in je code, 
dan zet je achter het pass statement de comment # TODO: [en dan de taak die je hier wil doen/uitzoeken nog].

De # TODO: comment wel weghalen als je die taak later dan ook echt gedaan hebt!

Opdracht:
a. Neem de voorbeeldcode over en voer het programma uit.
b. Haal de pass statement weg en voer het programma uit. Wat gebeurt er nu?
'''

getal = int(input('Vul een geheel getal in\n'))

if getal >0:
    print('Het ingevulde getal is positief\n')
elif getal == 0:
    pass #TODO: Uitzoeken of 0 positief of negatief of geen van beide is
else:
    print('Het ingevulde getal is negatief\n')

# a: Als het getal groter dan 0 is, dan print het "Het ingevulde getal is positief".
#    Als het getal gelijk aan 0 is, dan print het niks uit.
#    Als het getal kleiner dan 0 is, dan print het "Het ingevulde getal is negatief".

# b: Als je pass statement weghaalt, dan krijg je een error. "IndentationError: expected an indented block"
#    Er moet wat ingevuld worden onder elif!


'''
# Uitwerking:

getal = int(input('Vul een geheel getal in\n'))

if getal >0:
    print('Het ingevulde getal is positief\n')
elif getal == 0:    
else:
    print('Het ingevulde getal is negatief\n')


# Output:

  File "<ipython-input-26-2e9bd7efe692>", line 6
    else:
    ^
IndentationError: expected an indented block
'''