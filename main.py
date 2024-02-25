import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catching the Turtle")
FONT = ("Verdana", 15, "bold")
grid_size = 10
turtle_list =[]

#Score Turtle
score_turtle = turtle.Turtle()
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.85
    score_turtle.setpos(0,y)
    score_turtle.write(arg="SCORE: 0", move=False, align="center", font=FONT)

def make_turtle(x,y):
    new_turtle_in_new_structure = turtle.Turtle()
    new_turtle_in_new_structure.penup()
    new_turtle_in_new_structure.shape("turtle")
    new_turtle_in_new_structure.shapesize(2,2)
    new_turtle_in_new_structure.color("green")
    new_turtle_in_new_structure.goto(x * grid_size, y * grid_size)
    turtle_list.append(new_turtle_in_new_structure)


x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10,-20]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for new_turtle_in_new_structure in turtle_list:
        new_turtle_in_new_structure.hideturtle()

def show_hide_turtles_randomly():
    random.choice(turtle_list).showturtle()


turtle.tracer(0)

setup_score_turtle()
setup_turtles()
hide_turtles()
show_hide_turtles_randomly()

turtle.tracer(1)


turtle.mainloop()