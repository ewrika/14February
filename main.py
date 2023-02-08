import time
import math
from turtle import *
import wave
import sys


pen = Turtle()
pen.color('red')
bgpic("C:/Users/hohao/PycharmProjects/pythonProject4/f89-pXQzhP8.gif")
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)


def draw_heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()


def draw_txt():
    pen.up()
    pen.setpos(-50, 90)
    pen.down()
    pen.color('white')
    time.sleep(1)
    pen.write("Лучшей Девочке", font=("Aesthetic", 13, "bold"))
    pen.up()
    pen.setpos(-70, 70)
    pen.down()
    time.sleep(1)
    pen.write("    inst: ugoad", font=("Montserrat", 11, "bold"))
    pen.down()
    pen.setpos(-50, 50)
    pen.up()
    time.sleep(1)
    pen.write("От Егора", font=("Montserrat", 11, "bold"))

draw_heart()
draw_txt()
pen.ht()
time.sleep(2)
pen.clear()
bgpic(picname='nopic')

import turtle
import math

def xt(t):
    return 16 * math.sin(t) ** 3
def yt(t):
    return 13 * math.cos(t) - 5 \
           * math.cos(2 * t) - 2 * \
           math.cos(3 * t) - math.cos(4 * t)

t = turtle.Turtle()
t.speed(500)
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)
for i in range(2550):
    t.goto((xt(i) * 20, yt(i) * 20))
    t.pencolor((255 - i) % 255, i % 255, (255 + i) // 2 % 255)
    t.goto(0, 0)
t.hideturtle()
turtle.update()
turtle.mainloop()

done()
