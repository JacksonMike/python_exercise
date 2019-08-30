import turtle
y = 100
while y > -110:
    turtle.penup()
    turtle.goto(-200, y)
    turtle.pendown()
    turtle.fd(400)
    y -= 30

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.rt(90)
turtle.fd(180)

turtle.penup()
turtle.goto(-100, 80)
turtle.pendown()
turtle.write("公斤", font=("Arial", 12, "normal"))

turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.write("1", font=("Arial", 12, "normal"))

turtle.penup()
turtle.goto(-100, 20)
turtle.pendown()
turtle.write("2", font=("Arial", 12, "normal"))

turtle.penup()
turtle.goto(-100, -10)
turtle.pendown()
turtle.write("...", font=("Arial", 12, "normal"))

turtle.penup()
turtle.goto(-100, -40)
turtle.pendown()
turtle.write("197", font=("Arial", 12, "normal"))

turtle.penup()
turtle.goto(-100, -70)
turtle.pendown()
turtle.write("199", font=("Arial", 12, "normal"))

turtle.penup()
turtle.goto(100, 80)
turtle.pendown()
turtle.write("磅", font=("Arial", 12, "normal"))

turtle.penup()
turtle.goto(100, 50)
turtle.pendown()
turtle.write("2.2", font=("Arial", 12, "normal"))

turtle.penup()
turtle.goto(100, 20)
turtle.pendown()
turtle.write("6.6", font=("Arial", 12, "normal"))

turtle.penup()
turtle.goto(100, -40)
turtle.pendown()
turtle.write("433.4", font=("Arial", 12, "normal"))

turtle.penup()
turtle.goto(100, -70)
turtle.pendown()
turtle.write("437.8", font=("Arial", 12, "normal"))

turtle.hideturtle()
turtle.done()
