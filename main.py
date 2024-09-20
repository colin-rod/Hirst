from random import randint
from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
timmy.shape("circle")

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

# timmy.speed(0)
# timmy.pensize(5)
# print(randint(1,4))
# for i in range(200):
#     timmy.forward(20)
#     angles=[-90,0,90]
#     timmy.right(random.choice(angles))
#     timmy.pencolor(randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100)

# steps = 50
# angle_step = 360/steps
# angle = 0
# for i in range(steps):
#     timmy.setheading(angle)
#     timmy.pencolor(randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100)
#     timmy.circle(100)
#     angle += angle_step
#     print(i)

number = 30
colors = colorgram.extract('image.jpg', number)
print(colors)
color_list= []

for i in range(2,number):
    first_color = colors[i]
    r = first_color.rgb.r/255
    g = first_color.rgb.g/255
    b = first_color.rgb.b/255
    rgb = (r,g,b)
    color_list.append(rgb)

print(color_list)
dots = 10
space = 50
size = 20

timmy.pensize(size)
x= -1*((space*(dots-1))/2)
y = x
timmy.teleport(x,y)
for i in range(dots):
    for j in range(dots):
        timmy.pencolor(random.choice(color_list))
        timmy.dot(10)
        timmy.penup()
        timmy.forward(space)
    y += space
    timmy.teleport(x,y)




screen = Screen()
screen.exitonclick()

