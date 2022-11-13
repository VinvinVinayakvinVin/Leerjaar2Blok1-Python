# -*-coding:utf-8 -*-
'''
@File    :   Opgave 10.7
@Time    :   2022/11/13 18:15:29
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
* 7. Paragraaf 10.7 aanvulling: sum()¶
a. Lees deze paragraaf en sommeer de volgende lijst (de beoordelingscijferts op IMDB voor de acht seizoenen van GofT):

waarderingen = [9.31, 9.1, 9.1, 9.06, 9.05, 8.96, 8.83, 6.33]

b. Bepaal het gemiddelde van bovenstaande lijst.

c. Bepaal het minimum van deze lijst. Is daar een functie voor zoals sum(). Raadpleeg eventueel internet.
'''

# a:

waarderingen = [9.31, 9.1, 9.1, 9.06, 9.05, 8.96, 8.83, 6.33]
som = 0
for i in waarderingen:
    som += i

print(som)
som = sum(waarderingen)
print(som)

# b:
gem = som / len(waarderingen)
print(gem)

# c:
print(min(waarderingen))



# Uitwerkingen:
'''
waarderingen = [9.31, 9.1, 9.1, 9.06, 9.05, 8.96, 8.83, 6.33]

# a.
print(sum(waarderingen))

# b. 
print(sum(waarderingen)/len(waarderingen))

# c. 
print(min(waarderingen))


# # Output:


# 69.74000000000001
# 8.717500000000001
# 6.33
'''