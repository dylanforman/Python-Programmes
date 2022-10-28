print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You come to a crossroads. Do you go left or right?")

direction.lower()

if direction == "left":
  
  swim_or_wait = input("You arrive at a river. Do you swim across or wait?")
  swim_or_wait.lower()

  if swim_or_wait == "wait":
    which_door = input("You arrive at 3 doors. Do you go through the red door, yellow door, or blue door?")
    which_door.lower()

    if which_door == "yellow":
      print("You have found the treasure and survived!")
    elif which_door == "red":
      print("You fell into fire and burned to death. Game Over!")
    elif which_door == "blue":
      print("You walked into a room of lions and were eaten alive. Game Over!")
    else:
      print("Wrong Choice. Game Over!")
    
  else:
    print("You were attacked and killed by trout. Game Over!")
    
  
else:
  print("You went right at the crossroads and got killed by a tiger. Game Over!")
  