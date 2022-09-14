# -*-coding:utf-8 -*-
'''
@File    :   Opgave 2.19.py
@Time    :   2022/09/14 16:52:49
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

'''
Dit is een opgave uit het boek:

Exercise 2.2:

Practice using the Python interpreter as a calculator:

1. The volume of a sphere with radius r is  (4/3)𝜋r3 . 
What is the volume of a sphere with radius 5?
'''

from math import pi


r = 5                       # r = radius in centimetres.
v = (4/3)*pi*pow(r, 3)      # v = calculates the volume of a sphere with a radius of r.
print(f"The volume of a sphere with a radius of {r} is:", v)

# v = (4/3)*pi*r**3         # Zo kon je ook v berekenen.

'''
2. Suppose the cover price of a book is  $24.95 , 
but bookstores get a  40%  discount. Shipping costs  $3  for the first copy and 75 cents for each additional copy. 
What is the total wholesale cost for 60 copies?
'''

cover_price = 24.95             # price is in $'s
discount = 0.4                  # 40% discount.
shipping_cost = 3               # $3 shipping cost for the first copy.
additional_copy_cost = 0.75     # each additional copy costs 75 cents.
total_copies = 60
cost = 60*cover_price*(1-discount) + shipping_cost + additional_copy_cost*(total_copies-1)

print(f"Total wholesale cost for 60 copies is ${round(cost, 2)}")

'''
Uitwerking:

    # In de interpreter vul je:
    # 60*24.95*(1 - 0.4) + 3 + (60 - 1)*0.75

    # In Jupyter:
    cover = 24.95
    discount = 0.4
    n = 60
    ship1 = 3        # Shipping cost first copy
    ship_rest = 0.75 # Shipping cost for each additional copy

    cost = n*cover*(1 - discount) + ship1 + (n-1)*ship_rest

    # Print cost with two digits precision after the decimal point.
    print(f"Wholesale cost: {cost:.2f}")  # Wat nieuws geleerd weer: die .2f zorgt voor afronden op twee decimalen!
'''

# # test:
# t = 11.113
# s = 11.115
# print(f"{t:.2f}, {s:.2f}")