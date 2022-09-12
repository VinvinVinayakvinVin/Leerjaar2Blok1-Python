# -*-coding:utf-8 -*-
'''
@File    :   Opgave 2.2.py
@Time    :   2022/09/11 20:49:56
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None

# Opgave:
Schrijf een programma dat als invoer je 
voornaam heeft en dan de onderstaande zin uitprint.

"Hoe gaat het met [voornaam]?"
Nu dus met een ? (vraagteken) achter je naam.
'''

voornaam = input("Type een voornaam: ")
print("Hoe gaat het met " + voornaam + "?")      # Let op, ik heb net zoals in opg 2.1, String optelling gebruikt door + te gebruiken.
# print("Hoe gaat het met", voornaam + "?")      # methode 2 uitgeprobeerd van het uitwerking. <- van opg 2.1
# print(f"Hoe gaat het met {voornaam}?")         # methode 3 uitgeprobeerd van het uitwerking. <- van opg 2.1