#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import art
import random
print(art.logo)
print ("I'm thinking of a number between 1 and 100.")
NUMBER_CHOICE=random.randint(0,100)
HARD_ATTEMPT=5
EASY_ATTEMPT=10
def easy_attempt():
  failure_flag=True
  print("You have 10 attempts remaining to guess the number.")
  while(failure_flag):
    guess=input("Make a guess: ")
    if(guess<NUMBER_CHOICE):
      print("Too low.")
      print("Guess again.")
    elif(guess>NUMBER_CHOICE):
      print("Too high.")
      print("Guess again.")
    elif(guess==NUMBER_CHOICE):
      print(f"You got it! The answer was {NUMBER_CHOICE}.")
      
      
    

