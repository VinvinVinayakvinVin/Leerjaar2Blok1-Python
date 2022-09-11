# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 10:48:53 2022

@author: vinay
"""

"""
Opdracht 1.5
    Dit berekend de contante waarde op t = 0.
    De kans op overlijden wordt buiten beschouwd.
"""
t = 10.0
i = 0.025
c = 1000.0
print(round(c/pow((1+i), t), 2), "= Hoeveel je op de bank moet investeren om 10 jaar later €1000 te verdienen.")
