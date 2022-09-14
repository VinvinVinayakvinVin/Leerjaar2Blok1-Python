# -*-coding:utf-8 -*-
'''
@File    :   Opgave 2.12.py
@Time    :   2022/09/13 06:07:01
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
a): Zorg ervoor dat je met één print() statement het volgende overzicht print (tussen het eerste woord van elke regel en ~~Michiel~~ zit een tab):

Hallo!  Michiel
Hello!  Michiel
Goedendag!      Michiel
'''
# Methode 1
print(f"""
    {'Hallo!':<8}{'Michiel'}
    {'Hallo!':<8}{'Michiel'}        # 2 spaties = :<8
    {'Goedendag!':<16}{'Michiel'}   # 6 spaties = :<16
""")

# Methode 2
print("""
    Hallo!  Michiel
    Hallo!  Michiel
    Goedendag!      Michiel
""")

'''
b): Dit is natuurlijk niet mooi uitgelijnd.
    Dat kan wel door bij de eerste twee regels twee tabs te hebben ipv één tab.
    Pas je programma aan zodat het overzicht als volgt wordt:

Hallo!          Michiel
Hello!          Michiel
Goedendag!      Michiel
'''

# Methode 1
print("""
    Hallo!\t\tMichiel
    Hallo!\t\tMichiel
    Goedendag!\t\tMichiel
""")

# Methode 2.a
print(f"""
    {'Hallo!':<20}{'Michiel'}
    {'Hallo!':<20}{'Michiel'}
    {'Goedendag':<20}{'Michiel'}
""")

# Methode 2.b (andere waarde dan 20)
print(f"""
    {'Hallo!':<12}{'Michiel'}
    {'Hallo!':<12}{'Michiel'}
    {'Goedendag':<12}{'Michiel'}
""")

# Side note, je kon ook een variabel gebruiken in plaats van steeds Michiel te typen 😎
naam = "Vinayak"
print (f"""
    {'Hallo':<20}{naam}{'!'}
""")