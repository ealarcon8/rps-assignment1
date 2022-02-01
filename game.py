


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

#INTRODUCTION

player_name = input("Welcome to the game! What is your preferred name?")

#I'm printing blank lines so the output is easier to read.
print()

print ("Hi,", player_name, "Good luck!")

print()

# ASK FOR USER INPUT

user_input = input("Please choose one of the following: 'Rock', 'Paper', or 'Scissors': ")

print()

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

print ()

# DETERMINE THE WINNER

if user_input == computer_choice:
    print ("Both players chose", user_input, "You both win!")
    quit()

elif user_input == "rock":
    if computer_choice == "scissors":
        print ("Rock crushes scissors. You win!")
    elif computer_choice == "paper":
        print ("Paper covers rock. You lose.")
elif user_input == "paper":
    if computer_choice == "rock":
        print ("Paper covers rock. You win!")
    elif computer_choice == "scissors":
        print ("Scissors cut paper. You lose!")
elif user_input == "scissors":
    if computer_choice == "paper":
        print ("Scissors cut paper. You win!") 
    elif computer_choice == "rock":
        print ("Rock crushes scissors. You lose.")

print ()

# CLOSING STATEMENT

print ("Thank you for playing! Please play again!")

print ()
quit()
