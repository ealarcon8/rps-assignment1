


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


# ASK FOR USER INPUT

user_input = input("Please choose one of the following: 'Rock', 'Paper', or 'Scissors': ")

# move after validation
# print ("User chose:", u)


# VALIDATIONS

if (user_input == "Rock"):
     print ("User chose:", user_input)
elif (user_input == "rock"):
    print ("User chose:", user_input)
elif (user_input == "ROCK"):
    print ("User chose:", user_input)
elif (user_input == "Paper"):
    print ("User chose:", user_input)
elif (user_input == "paper"):
    print ("User chose:", user_input)
elif (user_input == "PAPER"):
    print ("User chose:", user_input)
elif (user_input == "Scissors"):
    print ("User chose:", user_input)
elif (user_input == "scissors"):
    print ("User chose:", user_input)
elif (user_input == "SCISSORS"):
    print ("User chose:", user_input)
#else syntax from: https://www.w3schools.com/python/python_conditions.asp
else: 
    print("Sorry, I didn't understand that choice. Please try again.")
# quit syntax from: https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
    print (quit)
    quit()


# COMPUTER CHOICE

# import random from class
import random
#is the same as: from random import choice

options = ["rock", "paper", "scissors"]

computer_choice=random.choice(options)

print("COMPUTER CHOSE:", computer_choice)


# DETERMINE THE WINNER



## Use Eugenie's code from Slack or Brandon's code from Slack (For BRandon's start with "result=none")

# FINAL RESULTS
