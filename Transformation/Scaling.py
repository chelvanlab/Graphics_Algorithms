from tkinter import *
import numpy as np

root = Tk()

c = Canvas(root,height=500,width=500)
c.pack()


def scale(sx,sy):

    sm = np.array([
        [sx,0],[0,sy]
    ])


    p1 = np.array([
        [100], [100]
    ])

    p2 = np.array([
        [200], [100]
    ])

    p3 = np.array([
        [200], [200]
    ])

    p4 = np.array([
        [100], [200]
    ])

    c.create_line(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
    c.create_line(int(p2[0]), int(p2[1]), int(p3[0]), int(p3[1]))
    c.create_line(int(p3[0]), int(p3[1]), int(p4[0]), int(p4[1]))
    c.create_line(int(p4[0]), int(p4[1]), int(p1[0]), int(p1[1]))

    p1s = np.dot(sm, p1)
    p2s = np.dot(sm, p2)
    p3s = np.dot(sm, p3)
    p4s = np.dot(sm, p4)

    c.create_line(int(p1s[0]), int(p1s[1]), int(p2s[0]), int(p2s[1]), fill="green")
    c.create_line(int(p2s[0]), int(p2s[1]), int(p3s[0]), int(p3s[1]), fill="green")
    c.create_line(int(p3s[0]), int(p3s[1]), int(p4s[0]), int(p4s[1]), fill="green")
    c.create_line(int(p4s[0]), int(p4s[1]), int(p1s[0]), int(p1s[1]), fill="green")


scale(2,2)
root.title("Scaling")
root.mainloop()