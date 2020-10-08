from turtle import *


def tree(branchLen, t):
    if branchLen > 20:
        t.forward(branchLen)
        t.right(30)
        tree(branchLen-25,t)
        t.left(60)
        tree(branchLen-20,t)
        t.right(30)
        t.backward(branchLen)

t = Turtle()
mywin = t.getscreen()
tree(100,t)
