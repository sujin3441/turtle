#turtle : class
import turtle

def draw_square(some_turtle):
# draw a square
    for i in range(1,5) :
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art() :
    window = turtle.Screen()
    window.bgcolor("white")
# creating an instance called 'brad'
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(3)

    i = 0
    while i < 35 :
        draw_square(brad)
        brad.right(10)
        i += 1

# creating an instance called 'angie'
    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.circle(100)
    # angie.circle(50)

    window.exitonclick()

draw_art()
