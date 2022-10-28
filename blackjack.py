import random


def play_game():
  
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

  user_cards = []
  computer_cards = []
  is_game_over = False
  for card in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
  
  

  def calculate_score(list_of_cards):
    score = sum(list_of_cards)

    if score == 21 and len(list_of_cards) == 2:
        return 0

    elif 11 in list_of_cards and score > 21:
      list_of_cards.remove(11)
      list_of_cards.append(1)
    return score


  def compare(user_score, computer_score):
    if user_score == computer_score:
      print("Draw.")
    elif user_score == 0:
      print("Blackjack. User wins.")
    elif computer_score == 0:
      print("Blackjack. Computer wins")
    elif user_score > 21:
      print("User Bust. Computer wins.")
    elif computer_score > 21:
      print("Computer Bust. User wins.")
    elif user_score > computer_score:
      print("User has a higher score. User wins.")
    else:
      print("Computer has a higher score. Computer wins.")
    
    
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computers first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      draw_another = input("Do you want to draw another card? Answer yes or no. ").lower()
      if draw_another == "yes":
        user_cards.append(deal_card())
      else:
        is_game_over = True
    

    
  while computer_score < 17 and computer_score != 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print("*******************************")
  print(f"User cards: {user_cards}, user score: {user_score}")
  print(f"Computer cards: {computer_cards}, computer score: {computer_score}")
  compare(user_score, computer_score)

  keep_playing = input("Do you want to play again? Answer yes or no. ").lower()

  if keep_playing == "yes":
    play_game()
  
play_game()