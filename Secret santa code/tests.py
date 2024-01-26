import turtle

letters = turtle.Turtle()
m = turtle.Turtle()
k = turtle.Turtle()
j = turtle.Turtle()
l = turtle.Turtle()
c = turtle.Turtle()
q = turtle.Turtle()
back = turtle.Turtle()
letters.penup()
letters.goto(-100, -450)
letters.pendown()
letters.hideturtle()
k.penup()
k.goto(-220, 150)
k.pendown()
k.hideturtle()



def cube():
    c.speed(10)
    c.penup()
    c.goto(-100, -300)
    c.pendown()
    c.pensize(3)
    c.begin_fill()
    c.color('Black')
    c.fillcolor('green')
    for i in range(4):
        c.forward(300)
        c.left(90)
    c.end_fill()
    c.begin_fill()
    c.color('black')
    c.fillcolor('green')
    c.goto(-100, 0)
    c.end_fill()
    c.begin_fill()
    c.color('black')
    c.fillcolor('black')
    c.left(45)
    c.forward(200)
    c.right(45)
    c.forward(250)
    c.goto(200, 0)
    c.end_fill()
    c.begin_fill()
    c.color('black')
    c.fillcolor('green')
    c.goto(293,143)
    c.right(90)
    c.forward(300)
    c.goto(200,-300)
    c.right(90)
    c.forward(100)
    c.right(90)
    c.end_fill()
    c.begin_fill()
    c.color('black')
    c.fillcolor('red')
    for i in range(4):
        c.forward(100)
        c.right(90)
        c.forward(100)
        c.left(90)
        c.forward(100)
        c.left(90)
    c.end_fill()    
    c.right(90)
    c.forward(100)
    c.left(57)
    #lines inside right side cube
    c.forward(80) #no touch
    c.begin_fill()
    c.fillcolor('red')
    c.left(35) #first turn into side
    c.forward(80)
    c.left(136)
    c.forward(63) #no touch 
    c.right(138)
    c.forward(98)
    c.right(43)
    c.forward(58)
    c.left(43)
    c.forward(119)
    #second ribbon 
    c.right(35)
    c.forward(57)#49
    c.right(144)
    c.forward(133)
    c.left(137)
    c.forward(30)
    #third/right side
    c.right(138)
    c.forward(99)
    c.right(46)
    c.forward(25)
    c.left(50)
    c.forward(58)
    c.end_fill()
    c.hideturtle()
def redraw():
    j.speed(10)
    j.pensize(3)
    j.penup()
    j.goto(-100, -300)
    j.pendown()
    j.pensize(3)
    for i in range(4):
        j.forward(300)
        j.left(90)
    j.goto(-100, 0)
    j.left(45)
    j.forward(200)
    j.right(45)
    j.forward(250)
    j.goto(200, 0)
    j.goto(293,143)
    j.right(90)
    j.forward(300)
    j.goto(200,-300)
    j.right(90)
    j.forward(100)
    j.right(90)
    for i in range(4):
        j.forward(100)
        j.right(90)
        j.forward(100)
        j.left(90)
        j.forward(100)
        j.left(90)    
    j.right(90)
    j.forward(100)
    j.left(57)
    #lines inside right side cube
    j.forward(80) #no touch
    j.left(35) #first turn into side
    j.forward(80)
    j.left(136)
    j.forward(63) #no touch 
    j.right(138)
    j.forward(98)
    j.right(43)
    j.forward(58)
    j.left(43)
    j.forward(119)
    #second ribbon 
    j.right(35)
    j.forward(57)#49
    j.right(144)
    j.forward(133)
    j.left(137)
    j.forward(30)
    #third/right side
    j.right(138)
    j.forward(99)
    j.right(46)
    j.forward(25)
    j.left(50)
    j.forward(58)
    j.hideturtle()   

def backround():
    turtle.bgcolor('lightgrey')
    back.speed(100)
    back.penup()
    back.goto(-640,-150)
    back.begin_fill()
    back.fillcolor('white')
    back.pendown()
    back.right(180)
    back.left(180)
    back.forward(3)
    for i in range(50):
        back.right(1)
        back.forward(4)
    for i in range(80):
        back.left(1)
        back.forward(5)
    for i in range(4):
        back.forward(40)
    for i in range(70):
        back.right(1)
        back.forward(5)
    for i in range(50):
        back.left(1)
        back.forward(7)
    back.goto(650,-650)
    back.goto(-650, -650)
    back.goto(-640,-150)
    back.end_fill()
    back.hideturtle()
def lid():
    l.speed(10)
    l.pensize(3)
    l.penup()
    l.goto(293,-70)#143
    l.pendown()
    l.left(5) 
    l.forward(125)
    #right side lid
    l.left(85)
    l.forward(300)
    l.left(93)
    l.forward(350)
    l.left(87)
    l.forward(87)
    #inner ribbon 
    l.left(90)
    l.forward(120)
    l.left(90)
    #going to top lid
    l.begin_fill()
    l.color('black')
    l.fillcolor('red')
    l.forward(93)
    l.right(87)
    l.forward(110)
    l.right(90)
    #right side ribbon 
    l.forward(109)
    l.left(90)
    l.forward(114)
    l.right(93)
    l.forward(88)
    l.right(86)
    l.forward(109)
    #bottom ribbon 
    l.left(87)
    l.forward(105)
    l.right(90)
    l.forward(18)
    l.right(91)
    l.forward(210)
    l.left(90)
    l.forward(108)
    l.end_fill()
    l.hideturtle()
def relid():
    m.speed(10)
    m.pensize(3)
    m.penup()
    m.goto(293,-70)#143
    m.pendown()
    m.begin_fill()
    m.color('black')
    m.fillcolor('green')
    m.left(5) 
    m.forward(125)
    #right side lid
    m.left(85)
    m.forward(300)
    m.left(93)
    m.forward(350)
    m.left(87)
    m.forward(82)
    #inner ribbon 
    m.left(90)
    m.forward(225)
    m.right(90)
    m.forward(216)
    m.end_fill()
    m.hideturtle()
   
    

