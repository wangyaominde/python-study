# -*- coding: utf-8 -*-
#-code by wangyaomin-#

import turtle
import time


def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(2)
    brad.circle(radius=100)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()


draw_square()
