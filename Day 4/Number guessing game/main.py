#Number guessing game in Python
import random
def game():
    Number_computer= random.randint(1,100)
    Number_input=int(input("Enter a number:"))

    while True:
     try:
        print("Hello, Welcome to the number guessing game, Created by Ahum Maitra\n")
        print("Let's start!\n")

        if (Number_input==Number_computer):
            print(f"Your number is {Number_input} and computer's number is {Number_computer}. Congrats! Number matched")
            break
        else:
            print(f"Sorry! Your number is {Number_input} and computer's number is {Number_computer}, not matched!\n")
            print("END")
            break
     except ValueError:
            print("Invalid input! Please enter a valid number.")
game()



