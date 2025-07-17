import pgzrun
import turtle

WIDTH = 1400
HEIGHT = 700
def l():
    g.left(90)
    bg.update()
def r():
    g.right(90)
    bg.update()
def f():
    g.forward(10)
    bg.update()
bg = turtle.Screen()
bg.tracer(0)
bg.bgcolor("dark blue")
bg.listen()
g = turtle.Turtle()
g.shape("circle")
g.color("white")
bg.update()

pgzrun.go()