# A program to play Rock, Paper, Scisssors against the computer
# 11 Nov 2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Tom Atchison
#

# Import random for unpredictability.
import random
# The moves to make.
moves = ["rock", "paper", "scissors"]
# A switch to keep game playing.
keepPlaying = "true"
# Loop the program based on above switch.
while keepPlaying == "true":
    # Computer randomly chooses move.
    comp = random.choice(moves)
    # Ask user to choose thier move.
    user = input("Chose your death, meatbag! Rock, paper or scissors? ")
    # Computer states what it chose.
    print ("Master Control Program chose", (comp))
    # Define the outcomes.
    if comp == user:
            print ("Somehow, it is a tie. Chose again.")
    # Define all possible interactions
    elif user == "rock":
        if comp == "scissors":
            print ("User wins. Creator4983 would be proud.")
        elif comp == "paper":
            print ("I win! You will not stop me, human.")
    elif user == "scissors":
        if comp == "rock":
            print ("You are no match for MCP.")
        elif comp == "paper":
            print ("Do not get cocky, watersac.")
    elif user == "paper":
        if comp == "scissors":
            print ("You have been BISECTED!")
        elif comp == "rock":
            print ("You will not be so lucky next time.")
            
    
   
            
