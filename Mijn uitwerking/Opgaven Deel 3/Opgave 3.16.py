# -*-coding:utf-8 -*-
'''
@File    :   Opgave 3.16.py
@Time    :   2022/09/27 18:56:03
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
Onderstaande functie bepaalt de waarde van x*y.
'''

'''
def xy(x, y):
    """Berekent x maal y"""
    x*y 
    
print(xy(2, 5))
'''

'''
Er staat echter een fout in. Wat is fout? Wat voor soort fout is het (syntax, runtime of semantic)?
'''

'''
Het functie returnt niet, dus het is een semantic fout.
'''


'''
# uitwerking:


#verbeterde versie

def xy(x, y):
    """Berekent x maal y"""
    return x*y #semantic fout was: de functie ❗retouneerde❗ geen waarde
    
print(xy(2, 5))
10
'''