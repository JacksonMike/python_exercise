import turtle

turtle.setheading(60)
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.circle(30, steps=3)

turtle.setheading(45)
turtle.penup()
turtle.goto(-20, 50)
turtle.pendown()
turtle.circle(30, steps=4)

turtle.setheading(36)
turtle.penup()
turtle.goto(60, 50)
turtle.pendown()
turtle.circle(30, steps=5)

turtle.setheading(330)
turtle.penup()
turtle.goto(120, 50)
turtle.pendown()
turtle.circle(30, steps=6)

turtle.hideturtle()
turtle.done()
