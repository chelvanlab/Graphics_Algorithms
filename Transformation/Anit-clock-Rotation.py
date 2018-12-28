from tkinter import *
import numpy as np
import math

root = Tk()

c = Canvas(root,height=500,width=500)
c.pack()

def rotate(t):

    tm = np.array([
        [round(math.cos(math.radians(t)),2),round(math.sin(math.radians(t)),2)],
        [round(math.sin(-math.radians(t)),2),round(math.cos(math.radians(t)),2)]
    ])

    p1 = np.array([
        [100],[100]
    ])

    p2 = np.array([
        [100], [200]
    ])

    p3 = np.array([
        [200], [200]
    ])

    c.create_line(int(p1[0]),int(p1[1]),int(p1[0]),int(p2[1]))
    c.create_line(int(p1[0]), int(p1[1]), int(p3[0]), int(p3[1]))
    c.create_line(int(p2[0]), int(p2[1]), int(p3[0]), int(p3[1]))

    p1t = np.dot(tm,p1)
    p2t = np.dot(tm,p2)
    p3t = np.dot(tm,p3)

    print(p1t)
    print(p2t)
    print(p3t)

    c.create_line(int(p1t[0]),int(p1t[1]),int(p2t[0]),int(p2t[1]),fill="green")
    c.create_line(int(p2t[0]),int(p2t[1]),int(p3t[0]),int(p3t[1]),fill="green")
    c.create_line(int(p3t[0]),int(p3t[1]),int(p1t[0]),int(p1t[1]),fill="green")

rotate(5)
root.title("Anti-clock Rotation")
root.mainloop()