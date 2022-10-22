# -*-coding:utf-8 -*-
'''
@File    :   Opgave 6.4.py
@Time    :   2022/10/22 08:58:38
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
4.¶
** append() en extend() zelf als functie maken

a. Maak zelf een functie dat de append() functie nabootst. 
De input van deze zelfgeschreven functie is een lijst en een element dat je wilt toevoegen aan de lijst. 
Maak gebruik van de + operator. Test ook de functie.

b. Maak zelf een functie, die de .extend() functie nabootst. 
De input van deze zelfgeschreven functie bestaat uit 2 lijsten en de output is de gecombineerde lijst. 
Maak gebruik van + operator. Test ook de functie.
'''

def append(lijst, input):
    """
    Zelfgecreërde append functie.
    Dit zorgt ervoor dat je elementen kan toevoegen aan je lijst.

    Parameters
    ----------
    lijst: array
    input: any primary type

    Returns
    -------
    nw_lijst: array
    """

    nw_lijst = lijst + [input]
    return nw_lijst

def extend(oud_lijst, lijst):
    """
    Dit zorgt ervoor dat je oude_lijst kan uitbreiden m.b.v nog een lijst.

    Parameters
    ----------
    oude_lijst: array
    lijst: array

    Returns
    -------
    nw_lijst: array
    """

    nw_lijst = oud_lijst + lijst
    return nw_lijst

input = input("Vul iets in: ")
lijst = []
nw_lijst = append(lijst, input)
# nw_lijst = append(nw_lijst, input)    # Even uit testen als je nog een keer de functie roept en nw_lijst invult.
print(nw_lijst)

test_lijstje = ['Hoi', True, 1000000000]
nw_lijst = extend(nw_lijst, test_lijstje)
print(nw_lijst)


# Uitwerking ⬇️
'''
#a
def eigen_append(lijst, element):
    element = [element] #de + werkt alleen als 'element' ook een list is
    return lijst + element

fruit = ['banaan', 'druif', 'peer']
print(eigen_append(fruit, 'appel')) 

#met de .append() functie
fruit = ['banaan', 'druif', 'peer']
fruit.append('appel')
    
print(fruit)



# # Output:

# ['banaan', 'druif', 'peer', 'appel']
# ['banaan', 'druif', 'peer', 'appel']
'''

'''
#b
def eigen_extend(lijst1, lijst2):
    return lijst1 + lijst2

fruit = ['banaan', 'druif', 'peer']
fruit2 = ['appel', 'mandarijn', 'pruim', 'aardbei', 'kiwi']
print(eigen_extend(fruit, fruit2)) 

#met de extend() functie
fruit.extend(fruit2)
print(fruit) 



# # Output:

# ['banaan', 'druif', 'peer', 'appel', 'mandarijn', 'pruim', 'aardbei', 'kiwi']
# ['banaan', 'druif', 'peer', 'appel', 'mandarijn', 'pruim', 'aardbei', 'kiwi']
'''