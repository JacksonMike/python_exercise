import turtle


# 圆心坐标(x,y),半径r
x, y, r = eval(input("please input:"))
# 圆面积
area = 3.14 * r * r
turtle.penup()
turtle.goto(float(x), float(y-r))
turtle.pendown()
turtle.circle(float(r))
turtle.penup()
turtle.goto(float(x), float(y))
turtle.pendown()
turtle.write(area)
turtle.hideturtle()
turtle.done()

