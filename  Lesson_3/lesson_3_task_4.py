import turtle

screen = turtle.Screen()
screen.title("Рисунок рыбки")
screen.setup(width=600, height=600)
t = turtle.Turtle()
t.speed(3)


def draw_horizontal_oval(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.setheading(-45)
    for _ in range(2):
        t.circle(width, 90)
        t.circle(height, 90)
    t.end_fill()


t.penup()
t.goto(20, -10)
t.pendown()
t.color("orange")
draw_horizontal_oval(t, 60, 30, "orange")


t.penup()
t.goto(10, 10) 
t.setheading(150)
t.pendown()
t.color("red")
t.begin_fill()
for _ in range(3):
    t.forward(45)
    t.left(120)
t.end_fill()

t.penup()
t.goto(100, 30)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(5)
t.end_fill()

t.hideturtle()

t.screen.exitonclick()
t.screen.mainloop()

turtle.done()
