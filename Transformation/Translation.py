from tkinter import *
import numpy as np

root = Tk()

c = Canvas(root,height=500,width=500)
c.pack()

def translate(tx,ty):

    tm = np.array([
        [tx],[ty]
    ])
    p1 = np.array([
        [100],[100]
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


    c.create_line(int(p1[0]),int(p1[1]),int(p2[0]),int(p2[1]))
    c.create_line(int(p2[0]), int(p2[1]), int(p3[0]), int(p3[1]))
    c.create_line(int(p3[0]), int(p3[1]), int(p4[0]), int(p4[1]))
    c.create_line(int(p4[0]), int(p4[1]), int(p1[0]), int(p1[1]))

    p1t = np.add(tm,p1)
    p2t = np.add(tm, p2)
    p3t = np.add(tm, p3)
    p4t = np.add(tm, p4)

    c.create_line(int(p1t[0]), int(p1t[1]), int(p2t[0]), int(p2t[1]),fill="green")
    c.create_line(int(p2t[0]), int(p2t[1]), int(p3t[0]), int(p3t[1]),fill="green")
    c.create_line(int(p3t[0]), int(p3t[1]), int(p4t[0]), int(p4t[1]),fill="green")
    c.create_line(int(p4t[0]), int(p4t[1]), int(p1t[0]), int(p1t[1]),fill="green")



translate(150,150)
root.title("Translation")
root.mainloop()