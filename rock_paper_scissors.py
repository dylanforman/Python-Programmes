import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choice = random.randint(0,2)

if user_choice == 0:
  print(rock)

  if computer_choice == 0:
    print("Computer chose:\n")
    print(rock)
    print("\n It was a draw.")

  elif computer_choice == 1:
    print("Computer chose:\n")
    print(paper)
    print("\n You lose. Paper beats rock.")

  elif computer_choice == 2:
    print("Computer chose:\n")
    print(scissors)
    print("\n You won. Rock beats scissors.")

elif user_choice == 1:
  print(paper)

  if computer_choice == 0:
    print("Computer chose:\n")
    print(rock)
    print("\n You won. Paper beats rock.")

  elif computer_choice == 1:
    print("Computer chose:\n")
    print(paper)
    print("\n It was a draw.")

  elif computer_choice == 2:
    print("Computer chose:\n")
    print(scissors)
    print("\n You lose. Scissors beats paper.")

elif user_choice == 2:
  print(scissors)

  if computer_choice == 0:
    print("Computer chose:\n")
    print(rock)
    print("\n You lose. Rock beats scissors.")

  elif computer_choice == 1:
    print("Computer chose:\n")
    print(paper)
    print("\n You won. Scissors beats paper.")

  elif computer_choice == 2:
    print("Computer chose:\n")
    print(scissors)
    print("\n It was a draw.")