#Simple calculator
'''
Author: Ahum Maitra  # Note: Names are case-sensitive and may trigger spell-check warnings.
Date: 25/03/2025
'''
import tkinter
from tkinter.constants import W
App= tkinter.Tk()
Title= tkinter.Label(App,"Welcome to Calculator!")
Label_Input= tkinter.Label(App,"Enter first number: ")
Label_Input_second= tkinter.Label(App,"Enter second number: ")
Add = tkinter.IntVar()
tkinter.Radiobutton(App, text='Addition', variable=Add).grid(row=0, sticky=W)
Sub = tkinter.IntVar()
tkinter.Radiobutton(App, text='Subtraction', variable=Sub).grid(row=0, sticky=W)
Mul = tkinter.IntVar()
tkinter.Radiobutton(App, text='Multiplication', variable=Mul).grid(row=0, sticky=W)
Div = tkinter.IntVar()
tkinter.Radiobutton(App, text='Division', variable=Div).grid(row=0, sticky=W)