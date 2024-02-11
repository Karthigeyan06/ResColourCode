import turtle    


def pen(a,b,c,d):
    

    t = turtle.Turtle()


    t.speed(10)
    

    t.color('black')
    t.pensize(3)
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.forward(180)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(50)


    t.penup()
    t.goto(-70, 0)
    t.pendown()
    t.color(a)
    t.begin_fill()

    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.end_fill()


    t.penup()
    t.goto(-40,0)
    t.pendown()
    t.color(b)
    t.begin_fill()
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.end_fill()

    t.penup()
    t.goto(-10,0)
    t.pendown()
    t.color(c)
    t.begin_fill()
    t.right(180)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.end_fill()


    t.penup()
    t.goto(20,0)
    t.pendown()
    t.color(d)
    t.begin_fill()
    t.right(180)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.end_fill()

    t.penup()
    t.color('black')
    t.goto(-100, 0)
    t.pendown()
    t.right(180)
    t.forward(180)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(50)

    t.penup()
    t.goto(-100,-25)
    t.pendown()
    t.left(90)
    t.forward(50)
    t.penup()

    t.goto(80,-25)
    t.right(180)
    t.pendown()
    t.forward(50)
    







        
    t.end_fill()
    t.hideturtle()



    turtle.done()

    return()