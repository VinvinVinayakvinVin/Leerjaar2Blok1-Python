# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 10:28:48 2022

@author: vinay
"""

"""
1.4.1 opdracht:
    Dit berekend de aantal seconden.
"""
x = 42  # Variabel x staat voor het aantal minuten.
seconden = x * 60 + 42 # Dit berekent het aantal seconden.
print(seconden, "seconden")

"""
1.4.2 opdracht:
    Dit berekend de aantal miles
    Note: 1.61 km = 1 mile
"""
miles = 10/1.61 # Dit berekent het aantal miles in 10 kilometer.
print(miles, "miles")

"""
1.4.3 opdracht:
    Dit berekend de gemiddelde snelheid in miles per hour.
"""
print("Het gemiddelde snelheid is: ", round(miles/(seconden/3600), 2), "miles per hour")
