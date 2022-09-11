# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 10:28:48 2022

@author: vinay
"""

"""
1.4.1 opdracht:
    Dit berekend de aantal seconden.
"""
x = 42
seconden = x * 60 + 42
print(seconden, "seconden")

"""
1.4.2 opdracht:
    Dit berekend de aantal miles
    Note: 1.61 km = 1 mile
"""
z = 1.61
miles = 10/z
print(miles, "miles")

"""
1.4.3 opdracht:
    Dit berekend de gemiddelde snelheid in miles per hour.
"""
print("Het gemiddelde snelheid is: ", round(miles/(seconden/3600), 2), "miles per hour")
