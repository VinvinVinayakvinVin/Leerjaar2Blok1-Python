# -*-coding:utf-8 -*-
'''
@File    :   Opgave 5.11.py
@Time    :   2022/10/21 11:53:15
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
11.¶
** Gek woord

Schrijf een programma met drie invoervariabelen woord (string), letter (string) en n (int).
De uitvoer is het woord met links en rechts ervan n-maal de letter.

(Bijv. invoer: plantje R 5. De uitvoer is dan RRRRRplantjeRRRRR).
'''

n = int(input("Vul een geheel getal voor n in: "))
letter = input("Type een letter in: ")
woord = input("Type een woord in: ")

def gek_woord(woord, letter, n):
    """
    Dit print uit het woord met links en rechts n maal het letter om het woord heen. (vreemd...).
    """
    
    print(letter*n, end="")
    print(woord, end="")
    print(letter*n)

gek_woord(woord, letter, n)


'''
# Uitwerking:

woord = input('type een woord in\n')
letter = input('type een letter in\n')
n = int(input('Vul een geheel getal in\n'))

for i in range(n):
    woord = letter + woord + letter

print(woord)
'''

# Kleine toelichting over de uitwerking:
    # eerste loop:
        # k + Jan + k       => kJank
    # tweede loop:
        # k + kJank + k     => kkJankk
    # derde loop:
        # k + kkJankk + k   => kkkJankkk