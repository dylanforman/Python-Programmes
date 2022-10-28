from turtle import Screen, Turtle
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a colour: ")
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The winning colour was {winning_color}")
            else:
                print(f"You have lost! {winning_color} is the winner!")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
