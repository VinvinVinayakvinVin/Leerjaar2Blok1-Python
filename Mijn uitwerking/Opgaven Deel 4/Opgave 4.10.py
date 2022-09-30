# -*-coding:utf-8 -*-
'''
@File    :   Opgave 4.10.py
@Time    :   2022/09/30 20:23:57
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
** Hieronder staat een programma dat de getallen a en b vermenigvuldigt en het resultaat print.
'''

'''
1egetal = Float(input('Vul getal 1 in/n")) 
2egetal = Float(input('Vul getal 2 in/n"))
               
maal = 1egetal * 2egetal
                      
print('De vermenigvuldiging is: " + maal)
'''

'''
In de code staan echter fouten! Zie jij welke fouten er allemaal in staan?
'''

# variabelnaam mag niet met een cijfer beginnen.
# Float moet met klein letter beginnen, niet met hoofdletter.
# In de input, moet er geen " eindigen of ' beginnen. Men mag wel '' gebruiken of "" gebruiken, niet '" of "'.
# Het is geen /n, maar \n om een newline te maken.
# zelfde in de print statement.
# bij maal = 1egetal * 2egetal, zelfde (geen cijfer beginnen in een variabelnaam).
# maal kan een beter variabelnaam hebben, bv: product, of vermenigvuldiging (liefst product, want dat is wat kort en duidelijker).
# in de print statement moet de maal in str() erin gezet!

# verbeterde versie ⬇️:

eerste_getal = float(input('Vul getal 1 in\n'))
tweede_getal = float(input('Vul getal 2 in\n'))

maal = eerste_getal * tweede_getal

print('De vermenigvuldiging is: ' + str(maal))

'''
# Uitwerking:

#een variabelnaam mag niet met een cijfer beginnen
#Float moet float zijn
#' wordt afgesloten met " ipv '
#/n moet \n zijn
1egetal = Float(input('Vul getal 1 in/n")) 
2egetal = Float(input('Vul getal 2 in/n"))
                
#variable naam kan beter                      
maal = 1egetal * 2egetal
                      
#' wordt afgesloten met "
# + (concatenate) werkt alleen tussen strings. "maal" is nu nog een float en 
#moet dus worden omgezet
print('De vermenigvuldiging is: " + maal)



#verbeterde versie
getal1 = float(input('Vul getal 1 in\n')) 
getal2 = float(input('Vul getal 2 in\n'))
                      
product = getal1 * getal2

print('De vermenigvuldiging is: ' + str(product))
'''