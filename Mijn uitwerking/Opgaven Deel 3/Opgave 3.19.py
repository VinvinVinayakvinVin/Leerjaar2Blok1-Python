# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.19.py
@Time    :   2022/09/27 19:38:36
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
** Onderstaand programma verlangt een inputwaarde en zoveel maal zal ‘Hallo’ worden geprint.
'''

'''
def printen(x):
    """print Hallo x-maal onder elkaar uit"""
    
    print('Hallo\n' * x)

x = input()
print(printen(x))
'''

'''
Echter er staat een fout in. Wat is er fout en is het een syntax, runtime of semantic error? Hoe los je dit op?
'''

# Er is een runtime error, omdat x een String waarde heeft en niet een integer waarde heeft.
# De return statement staat ook niet erbij, dit geeft geen error, maar is wel belangrijk om wel erbij te zetten als je het later toch nodig hebt.
# Stel x heeft een integer waarde, dan gaat er iets ook erbij uitprinten. En dat is "None".

# def printen(x):
#     """print Hallo x-maal onder elkaar uit"""
    
#     print('Hallo\n' * x)

# x = input()
# print(printen(x))

'''
⬆️ TypeError: can't multiply sequence by non-int of type 'str'
Ofwel syntaxerror❗
'''

# def printen(x):
#     """print Hallo x-maal onder elkaar uit"""
    
#     print('Hallo\n' * x)

# x = int(input("Type een geheel getal in: "))
# print(printen(x))

# ⬆️ Dit geeft als nog een semantic error, want het print None uit en dat is niet de bedoeling.

def printen(x):
    """print Hallo x-maal onder elkaar uit"""
    
    print('Hallo\n' * x)

x = int(input("Type een geheel getal in: "))
printen(x)

# ⬆️ Dit is nu de juiste code.


'''
# Uitwerking: 

def printen(x):
    """print Hallo x-maal onder elkaar uit"""
    
    return print('Hallo\n' * x)

# x = input() #syntax error; x is hier nog een string

#verbeterde versie
x = int(input())

print(printen(x))
'''