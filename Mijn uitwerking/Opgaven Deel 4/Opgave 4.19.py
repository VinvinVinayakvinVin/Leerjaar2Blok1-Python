# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.19.py
@Time    :   2022/10/20 06:39:04
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
4.19
** Hieronder staat een programma, met daarin een functie gelijk.
'''

'''
def gelijk(x, y):
    if x = y:      
        print('x en y zijn gelijk')
    else:
        if x < y:    
            print('x is groter dan y')
        else:
            print('x is kleiner dan y')
            
gelijk(2,3)
'''

'''
a. In de code staan twee fouten, welke twee? Syntax? Runtime? Semantic? Herstel ze.
b. Herschrijf de code zonder nesting.

PS: Dat er geen comments bijstaan is ook fout eigenlijk, maar geen codefout. Dus die fout zoeken we niet!
'''

def gelijk(x, y):
    if x == y:      
        print('x en y zijn gelijk')
    else:
        if x < y:    
            print('x is kleiner dan y')
        else:
            print('x is groter dan y')
            
gelijk(2,3)

# 1e fout: if x = y moet x == y zijn!
# 2e fout: bij de 2e if statement bij print statement staat er "x is groter dan y", maar moet "x is kleiner dan y" zijn.
        # (3e fout): Natuurlijk is dat ook bij de tweede else statment, daar staat "x is kleiner dan y", maar moet "x is groter dan y" zijn.

# 1e fout: is een syntaxerror.
# 2e (ook 3e) fout: is een semanticerror.

# Er moet ook comments erbij zijn, maar wordt gezegd dat dat geen code fout is.
# Maar wel belangrijk om dat erbij te zetten!


'''
# Uitwerking:
def gelijk(x, y):
    if x = y:       #SYNTAX FOUT: 2 variabelen vergelijken doe je met ==
        print('x en y zijn gelijk')
    else:
        if x < y:    #Semantic: hier test je of x < y maar het tegenovergestelde wordt uitgeprint
            print('x is groter dan y')
        else:
            print('x is kleiner dan y')
            
gelijk(2,3)


#verbeterde versie
def gelijk(x, y):
    if x == y:      
        print('x en y zijn gelijk')
    elif x > y:
        print('x is groter dan y')
    else:
        print('x is kleiner dan y')
            
gelijk(2,3)
'''