import random
from art import logo, vs
from game_data import data
import replit

def get_random_account():
  return random.choice(data)

def format_data(account):
  name = account['name']
  description = account['description']
  country = account['country']
  return f"{name}, a {description}, from {country}"
  
def check_answer(guess, a_followers, b_followers):
  if guess == 'a' and a_followers > b_followers:
    return True
  elif guess == 'b' and b_followers > a_followers:
    return True
  else:
    return False


def play_game():

  print(logo)

  choice_a = get_random_account()
  choice_b = get_random_account()
  game_should_continue = True
  
  if choice_a == choice_b:
    choice_b = get_random_account()
  score = 0


  while game_should_continue:
    choice_a = choice_b
    choice_b = get_random_account()
    
    print(f"Compare A: {format_data(choice_a)}")
    print(vs)
    print(f"Against B: {format_data(choice_b)}")
    guess = input("Who has more followers? A or B: ").lower()
    a_follower_count = choice_a['follower_count']
    b_follower_count = choice_b['follower_count']
  
    keep_playing = check_answer(guess, a_follower_count, b_follower_count)

    replit.clear()
    print(logo)
    if keep_playing:
      score += 1
      print(f"You got it right. Your score is {score}.")
    else:
      game_should_continue = False
      print(f"You got it wrong. Your score was {score}.")
    
  


  
play_game()