from tkinter import *
import numpy as np

root = Tk()

c = Canvas(root,height=500,width=500)
c.pack()


def shearing(sx):

    x1 = 100
    y1 = 100

    x2 = 150
    y2 = 100

    x3 = 150
    y3 = 150

    x4 = 100
    y4 = 150

    c.create_line(x1,y1,x2,y1)
    c.create_line(x2,y2,x3,y3)
    c.create_line(x3,y3,x4,y4)
    c.create_line(x4,y4,x1,y1)

    xs1 = x1+sx*y1
    xs2 = x2+sx*y2
    xs3 = x3+sx*y3
    xs4 = x4+sx*y4

    print(xs1, y1, xs2, y1)
    c.create_line(xs1, y1, xs2, y1)
    c.create_line(xs2, y2, xs3, y3)
    c.create_line(xs3, y3, xs4, y4)
    c.create_line(xs4, y4, xs1, y1)


shearing(1)
root.mainloop()