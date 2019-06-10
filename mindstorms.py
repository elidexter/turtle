import turtle
def make_box(brad):
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
def draw_square():
    window=turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)      
    angle=0#init 0 angle
    while angle<=360:
        brad.right(angle)
        make_box(brad) 
        angle+=15# add 15 degress to angle and reinit grapich box
    #angie=turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
    window.exitonclick()

draw_square()