#draw_square
import turtle

def move_turtle(some_turtle):
# draw a square
    i = 0
    while i < 4 :
        some_turtle.forward(100)
        some_turtle.right(90)
        i += 1


def draw_square() :
# creating an instance called 'brad'
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("pink")
    brad.speed(5)
    #accessing the class 'turtle' to do all the actions
    move_turtle(brad)

def draw_circle():
# drawing a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_art( ):
    window = turtle.Screen()
    window.bgcolor("white")

    draw_square()
    draw_circle()

    window.exitonclick()


draw_art()
