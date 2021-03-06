import turtle 
import time

delay = 1

window = turtle.Screen()
window.title("Conway's Game of Life, But turtles You know")
window.bgcolor("black")
window.setup(600, 600)
window.tracer(0)
edge =  280

cells = []

cell = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.sety(edge)
head.setx(-edge)
head.direction = "stop"


while True: 
    window.update()



    time.sleep(delay)

window.mainloop()