#Simple calculator
'''
Author: Ahum Maitra
Date: 25-March-2025
'''
import tkinter
from tkinter import W



# Initialize the main application window
App = tkinter.Tk()
App.title("Simple Calculator")

# Labels
Title = tkinter.Label(App, text="Welcome to Calculator!")
Title.grid(row=0, column=0, columnspan=2)  # Display label
Label_Input = tkinter.Label(App, text="Enter first number: ")
Label_Input.grid(row=1, column=0)
Label_Input_second = tkinter.Label(App, text="Enter second number: ")
Label_Input_second.grid(row=2, column=0)

# Input fields
Entry1 = tkinter.Entry(App)
Entry1.grid(row=1, column=1)
Entry2 = tkinter.Entry(App)
Entry2.grid(row=2, column=1)

# Radio Buttons for operations
operation = tkinter.IntVar()  # One variable for all radio buttons

tkinter.Radiobutton(App, text='Addition', variable=operation, value=1).grid(row=3, column=0, sticky=W)
tkinter.Radiobutton(App, text='Subtraction', variable=operation, value=2).grid(row=4, column=0, sticky=W)
tkinter.Radiobutton(App, text='Multiplication', variable=operation, value=3).grid(row=5, column=0, sticky=W)
tkinter.Radiobutton(App, text='Division', variable=operation, value=4).grid(row=6, column=0, sticky=W)

# Function to perform calculations
def calculate():
    try:
        num1 = float(Entry1.get())
        num2 = float(Entry2.get())
        op = operation.get()

        if op == 1:
            result = num1 + num2
        elif op == 2:
            result = num1 - num2
        elif op == 3:
            result = num1 * num2
        elif op == 4:
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero"
        else:
            result = "Please select an operation"

        Result_Label.config(text=f"Result: {result}")

    except ValueError:
        Result_Label.config(text="Invalid input! Enter numbers only.")

# Submit button
Submit = tkinter.Button(App, text="Calculate", command=calculate)
Submit.grid(row=7, column=0, columnspan=2)

# Label to display the result
Result_Label = tkinter.Label(App, text="Result: ")
Result_Label.grid(row=8, column=0, columnspan=2)

# Run the app
App.mainloop()

