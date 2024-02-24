import turtle

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catching the Turtle")
FONT = ("Verdana", 30, "bold")

#Score Turtle
score_turtle = turtle.Turtle()
score_turtle.color("dark blue")
score_turtle.write(arg="SCORE: 0", move=False, align="center", font=FONT)



turtle.mainloop()