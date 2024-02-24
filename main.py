import turtle

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catching the Turtle")
FONT = ("Verdana", 30, "bold")

#Score Turtle
score_turtle = turtle.Turtle()
def setup_score_turtle():

    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.80


    score_turtle.setpos(0,y)
    score_turtle.write(arg="SCORE: 0", move=False, align="center", font=FONT)

setup_score_turtle()


turtle.mainloop()