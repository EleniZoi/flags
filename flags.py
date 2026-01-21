import  turtle
import random

bob = turtle.Turtle()
points = 0
lives = 3

def Germany():
    bob.fillcolor("black")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(33.33)  # 100/3 for equal stripes
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0, -33.33)
    bob.pd()
    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(33.33)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0, -66.66)
    bob.pd()
    bob.fillcolor("yellow")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(33.33)
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()

def Spain():  # Spanish flag: three horizontal stripes (red, yellow, red)
    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(25)  # 100/4 for top red stripe
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0, -25)
    bob.pd()
    bob.fillcolor("yellow")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(50)  # 100/2 for yellow stripe (twice as thick)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0, -75)
    bob.pd()
    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(25)  # 100/4 for bottom red stripe
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()

def Sweden():  # Swedish flag: yellow Nordic cross on blue background
    bob.fillcolor("blue")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(100)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(60, 0)  # Vertical cross arm at 2/5 width
    bob.pd()
    bob.fillcolor("yellow")
    bob.begin_fill()
    for i in range(2):
        bob.fd(30)  # Cross arm width
        bob.rt(90)
        bob.fd(100)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0, -40)  # Horizontal cross arm at 2/5 height
    bob.pd()
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()


countries = [Germany, Spain, Sweden]

while lives > 0 and len(countries) > 0:
    bob.reset()
    flag = random.choice(countries)
    flag()
    answer = input("Guess the flag! ")
    if answer == flag.__name__:
        print("Correct!")
        points = points + 1
        countries.remove(flag)
    else:
        print("Wrong!")
        lives = lives - 1

    print("Points: ", points)
    print("Lives: ", lives)

print("Game over")






turtle.done()
