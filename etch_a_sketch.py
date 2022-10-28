from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.back(10)


def clockwise():
    turtle.right(10)


def counter_clockwise():
    turtle.left(10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(clockwise, 'd')
screen.onkey(counter_clockwise, 'a')
screen.onkey(clear, 'c')
screen.exitonclick()
