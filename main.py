from random import randint
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#     i += 1
# for i in range(5):
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)
#     timmy.down()


# for i in range(3,8):
#     for j in range (i):
#         timmy.forward(100)
#         timmy.right(360/i)
#     timmy.pencolor(randint(0, 100) / 100,randint(0, 100) / 100,randint(0, 100) / 100)

timmy.speed(10)
timmy.pensize(5)
print(randint(1,4))
for i in range(200):
    timmy.forward(20)
    angles=[-90,0,90]
    timmy.right(random.choice(angles))
    timmy.pencolor(randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100)


screen = Screen()
screen.exitonclick()

