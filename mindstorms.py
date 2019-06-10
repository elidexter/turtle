import turtle
def make_box(turtle):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
def make_circle(turtle):
    turtle.circle(100)
def draw_circlebysquare():
    window=turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)      
    angle=0#init 0 angle
    while angle<=360:
        print "render on "+str(angle)+" degrees"
        brad.right(angle)
        make_box(brad) 
        angle+=15# add 15 degress to angle and reinit grapich box    
    window.exitonclick()
def draw_circlebycircle():
    window=turtle.Screen()
    window.bgcolor("red")
    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(2)      
    angle=0#init 0 angle
    while angle<=360:
        print "render on "+str(angle)+" degrees"
        angie.right(angle)
        make_circle(angie) 
        angle+=15# add 15 degress to angle and reinit grapich box    
    window.exitonclick()

draw_circlebysquare()
draw_circlebycircle()