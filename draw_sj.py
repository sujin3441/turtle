import turtle

window = turtle.Screen()
window.bgcolor("white")


# initialize instance
sj = turtle.Turtle()
sj.shape("turtle")
sj.color("green")
sj.speed(2)

#s
sj.backward(100)
sj.left(90)
sj.backward(100)
sj.right(90)
sj.forward(100)
sj.right(90)
sj.forward(100)
sj.right(90)
sj.forward(100)
sj.left(90)

#j
sj.penup()
sj.goto(200,0)

sj.pendown()
sj.forward(200)
sj.right(90)
sj.forward(100)
sj.left(90)





window.exitonclick()
