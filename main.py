import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catching the Turtle")
FONT = ("Verdana", 15, "bold")
grid_size = 10
score = 0
game_over = False

turtle_list =[]

#Score Turtle
score_turtle = turtle.Turtle()

#Count Down Turtle
countdown_turtle = turtle.Turtle()

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

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    new_turtle_in_new_structure.onclick(handle_click)
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
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_hide_turtles_randomly,1000)

def countdown(time):
    global  game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("brown")
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.85
    countdown_turtle.setpos(0, 220)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda : countdown(time-1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over !!!", move=False, align="center", font=FONT)


def startgame():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_hide_turtles_randomly()
    countdown(10)
    turtle.tracer(1)

startgame()
turtle.mainloop()