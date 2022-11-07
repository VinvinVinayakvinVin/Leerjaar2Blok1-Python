# -*-coding:utf-8 -*-
'''
@File    :   test.py
@Time    :   2022/11/07 13:04:21
@Author  :   Vinayak Shukla Kalapnat 
@Version :   1.0
@Desc    :   None
'''

import os
from tkinter import *
import time

os.chdir(os.getcwd() + "\\Extra oefenopdracht 1\\")

root = Tk()
root.attributes("-topmost", True)
frame = Frame(root)

def clearFrame():    
    for widget in frame.winfo_children():
       widget.destroy()  

canvas = Canvas(root, width=1000, height=500, bg="white")

# n_rijen = len(open('Snoopy.txt').readlines())
# n_rijen = len(open('Snoopy2.txt').readlines())
n_rijen = len(open('CatDog.txt').readlines())
# n_rijen = len(open('CatDog2.txt').readlines())
teller = 0
while teller < 10:
    file = open('CatDog.txt')
    text = Text(root)
    for i in range(1, n_rijen + 1):
        line = file.readline()
        x = 100
        n = 0
        for letter in line:
            canvas.create_text(x + n*5, i*10, text=letter)
            n = n + 1
    canvas.pack()
    canvas.update()

    time.sleep(0.6)
    canvas.delete("all")

    file = open('CatDog2.txt')

    text = Text(root)
    for i in range(1, n_rijen + 1):
        line = file.readline()
        x = 100
        n = 0
        for letter in line:
            canvas.create_text(x + n*5, i*10, text=letter)
            n = n + 1
    canvas.pack()
    canvas.update()

    time.sleep(0.6)

    if teller != 9:
        canvas.delete("all")    
    
    teller = teller + 1 

root.mainloop()