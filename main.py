import turtle
import random

drawing_board=turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Turle Drawing")
turtle_instance=turtle.Turtle()



#Turle moves

def turtle_color():
    r=random.random()
    g=random.random()
    b=random.random()
    turtle_instance.pencolor(r,g,b)

def move_and_change_color():
    turtle_instance.forward(100)
    turtle_color()

def rotate_turtle_left():
    turtle_instance.left(50)

def rotate_turtle_right():
    turtle_instance.right(50)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()
def turtle_penup():#turtle giderken çizmez
    turtle_instance.penup()

def turtle_pendown():
    turtle_instance.pendown()

def turtle_backward():
    turtle_instance.backward(100)

drawing_board.listen()
drawing_board.onkey(fun=move_and_change_color,key="w")
drawing_board.onkey(fun=turtle_backward,key="s")
drawing_board.onkey(fun=rotate_turtle_left,key="a")
drawing_board.onkey(fun=rotate_turtle_right,key="d")
drawing_board.onkey(fun=clear_screen,key="z")
drawing_board.onkey(fun=turtle_return_home,key="h")
drawing_board.onkey(fun=turtle_penup,key="q")
drawing_board.onkey(fun=turtle_pendown,key="e")


turtle.mainloop()#kapanmasın oyun