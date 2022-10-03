from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def left():
    tim.left(10)


def right():
    tim.right(10)


def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
