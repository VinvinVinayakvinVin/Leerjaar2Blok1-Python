# -*-coding:utf-8 -*-
'''
@File    :   Opgave 6.1.py
@Time    :   2022/10/22 06:03:57
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
1.
* We hebben twee lijsten, een lijst met namen en een lijst met bijbehorende tentamencijfers programmeren.
voornamen = ['Ronald', 'Jasper', 'Freke', 'Anouar', 'Maaike', 'Tomas', 'Isabelle']
resultaten = [6, 5, 8, 9, 10, 8, 7]
'''

'''
a. Schrijf een programma waarbij een nieuwe lijst wordt gemaakt met daarin de namen en cijfers. 
Eerst komen de zeven namen en dan pas de zeven cijfers. Print deze lijst uit.
'''

def lijst_voornamen_maken():
    """
    Dit maakt een lijst voor voornamen.
    De waarden van de elementen van beide lijsten wordt bepaald door user input.

    Parameters
    ----------
    None

    Returns
    -------
    voornamen: array (lijst)

    """
    voornamen = []
    for i in range(7):
        voornamen.append(input("Vul een voornaam in: "))
    return voornamen

def lijst_cijfers_maken():
    """
    Dit maakt een lijst voor cijfers.
    De waarden van de elementen van beide lijsten wordt bepaald door user input.

    Parameters
    ----------
    None

    Returns
    -------
    cijfers: array (lijst)

    """
    cijfers = []
    for i in range(7):
        cijfers.append(float(input("Vul een cijfer in: ")))
    return cijfers

voornamen = lijst_voornamen_maken()
cijfers = lijst_cijfers_maken()

print(voornamen)
print(cijfers)

nwlijst = voornamen + cijfers
print(nwlijst)
nwlijst = voornamen
nwlijst.extend(cijfers)
print(nwlijst, end="\n\n\n")

'''
** b. Eigenlijk willen we dat in de nieuwe lijst eerst een naam staat en dan daarna het bijbehorende cijfer. Dus:

['Ronald', 6, 'Jasper', 5, 'Freke', 8, 'Anouar', 9, 'Maaike', 10, 'Tomas', 8, 'Isabelle', 7]

Schrijf een programma dat bovenstaande lijst genereert uit de lijsten 'voornamen' en 'resultaten'. 
Lukt het je om hier een ‘creatieve’ manier voor te bedenken?
'''

# Methode 1 (cheezy way) 😂
def lijst_maken():
    """
    Dit maakt een lijst voor voornamen en cijfers in één.
    De waarden van de elementen van beide lijsten wordt bepaald door user input.

    Parameters
    ----------
    None

    Returns
    -------
    lijst: array
    """
    lijst = []
    for i in range(7):
        lijst.append(input("Vul een voornaam in: "))
        lijst.append(float(input("Vul een cijfer in: ")))
    return lijst

lijst = lijst_maken()
print(lijst)

# Methode 2 (legit way)
def lijst_combineren(voornamen, cijfers):
    """
    Dit maakt een nieuwe lijst voor voornamen en cijfers in één.

    Parameters
    ----------
    voornamen: array (lijst)
    cijfers: array (lijst)

    Returns
    -------
    nieuwe_lijst: array
    """
    nieuwe_lijst = []
    for i in range(7):
        nieuwe_lijst.append(voornamen[i])
        nieuwe_lijst.append(cijfers[i])
    return nieuwe_lijst

nieuwe_lijst = lijst_combineren(voornamen, cijfers)
print(nieuwe_lijst)

'''
** c. Zie b, maar i.p.v. een programma, 
schrijf je een functie dat de twee (even grootte) lijsten als input inleest 
en de output is de lijst met de gecombineerde gegevens zoals in opgave b.
'''

# Gedaan (zie legit way) lmao.


'''
# Uitwerking voor a:

#a
voornamen = ['Ronald', 'Jasper', 'Freke', 'Anouar', 'Maaike', 'Tomas', 'Isabelle']
resultaten = [6, 5, 8, 9, 10, 8, 7]

overzichten = voornamen + resultaten

print(overzichten)

# Alternatief:

voornamen = ['Ronald', 'Jasper', 'Freke', 'Anouar', 'Maaike', 'Tomas', 'Isabelle']
resultaten = [6, 5, 8, 9, 10, 8, 7]

voornamen.extend(resultaten)

print(voornamen)


# # output:

# ['Ronald', 'Jasper', 'Freke', 'Anouar', 'Maaike', 'Tomas', 'Isabelle', 6, 5, 8, 9, 10, 8, 7]
# ['Ronald', 'Jasper', 'Freke', 'Anouar', 'Maaike', 'Tomas', 'Isabelle', 6, 5, 8, 9, 10, 8, 7]
'''

'''
# Uitwerking voor b:

#b
voornamen = ['Ronald', 'Jasper', 'Freke', 'Anouar', 'Maaike', 'Tomas', 'Isabelle']
resultaten = [6, 5, 8, 9, 10, 8, 7]

n = len(voornamen)

overzichten = []
for i in range(n):
    overzichten.append(voornamen[i])
    overzichten.append(resultaten[i])
    
print(overzichten)


# Output:

['Ronald', 6, 'Jasper', 5, 'Freke', 8, 'Anouar', 9, 'Maaike', 10, 'Tomas', 8, 'Isabelle', 7]
'''

'''
# Uitwerking voor c:

#c
voornamen = ['Ronald', 'Jasper', 'Freke', 'Anouar', 'Maaike', 'Tomas', 'Isabelle']
resultaten = [6, 5, 8, 9, 10, 8, 7]

def naam_cijfer(lijst1, lijst2):
    n = len(lijst1)
    overzichten = []
    
    for i in range(n):
        overzichten.append(lijst1[i])
        overzichten.append(lijst2[i])
    
    return overzichten
    
print(naam_cijfer(voornamen, resultaten))
'''