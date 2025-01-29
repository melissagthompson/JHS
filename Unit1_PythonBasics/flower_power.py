#  Name:
#  Flower Power
#  Create a turtle program that draws flowers

import turtle
#    creates background variable for colorchange
#    and the digital pen
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(5)    # the larger the number, the faster the speed

#    changes color of background
screen.bgcolor('lightblue')

# a function that can draw a petal
def draw_petal():
    for _ in range(2):
        t.circle(50, 60)  # Adjust petal size
        t.left(120)
