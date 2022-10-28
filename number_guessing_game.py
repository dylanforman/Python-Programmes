
from art import logo
import random

hard_mode = 5
easy_mode = 10

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too High.")
    return turns - 1
  elif guess < answer:
    print("Too Low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose a difficulty. Type easy or hard: ").lower()
  if level == 'easy':
    return easy_mode
  elif level == 'hard':
    return hard_mode
  

guessed_correctly = False


def game():
  
  print(logo)
  answer = random.randint(1, 100)

  print("Welcome to the Number Guessing Game")
  print("I'm thinking of a number between 1 and 100")
  print(f"Psst. The answer is {answer}")

  turns = set_difficulty()

  guess = 0

  while guess != answer:
    print(f"You have {turns} guesses remaining.")

    guess = int(input("Guess a number: "))
    

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You ran out of lives. Game Over")
      print(f"The answer was {answer}.")
    elif guess != answer:
      print("Guess Again.")

game()
    