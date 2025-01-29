#  Name:
#  Flower Power
#  Create a turtle program that draws flowers

import turtle
t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor('lightblue')

# a function that can draw a petal
def draw_petal():
    for _ in range(2):
        t.circle(50, 60)  # Adjust petal size
        t.left(120)
