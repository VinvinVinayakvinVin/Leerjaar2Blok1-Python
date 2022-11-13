# -*-coding:utf-8 -*-
'''
@File    :   Opgave 9.4.py
@Time    :   2022/11/13 13:22:08
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

geslacht = input('Vul je geslacht in j/m: ')

if geslacht == 'j':
    print('Je geslacht is een jongen.')
else:
    print('Je geslacht is een meisje.')

# Hier heb ik het in één keer gezet!
print('Je geslacht is een jongen.' if geslacht == 'j' else 'Je geslacht is een meisje.')

# Uitwerking:
'''
geslacht = input('Vul je geslacht in j/m: ')

print('Je geslacht is een jongen.') if geslacht == 'j' else print('Je geslacht is een meisje.')
'''

# Uitwerking zegt dat je deze ook kan doen.
print('Je geslacht is een jongen.') if geslacht == 'j' else print('Je geslacht is een meisje.')