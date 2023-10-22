from random import randint
from art import logo

#We are creating global contants

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
MEDIUM_LEVEL_TURNS = 7


#Function to check user's actual answer

def check_answer(guess , answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too High!!")
        return turns - 1
    elif guess < answer:
        print("Too Low :(") 
        return turns - 1
    else:
        print(f"Correct :) you got it!! the correct answer is {answer} ")       

#Make function to set difficulty

def set_difficulty():
   level = input("Choose a difficulty Type :'Easy','Medium' or 'Hard': ")
   if level == "easy":
    return EASY_LEVEL_TURNS
   elif level == "medium":
    return MEDIUM_LEVEL_TURNS
   else:
    return HARD_LEVEL_TURNS   
def game() :
    print(logo)
    #Choosing the number between 1 to 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Hint {answer}")

    turns = set_difficulty()
   

    #Repeat the cycle when they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts according to your choosen level!!")
        #Let the user guess the number .
        guess = int(input("Make a guess:"))
        turns = check_answer(guess , answer , turns)
        if turns == 0:
           print("You've run out of guesses, you lose.")
           return
        elif guess != answer :
           print("Guess Again")

#Track the numbe rof the turns and also reduce by 1

#art module from the art.py file 

game()

