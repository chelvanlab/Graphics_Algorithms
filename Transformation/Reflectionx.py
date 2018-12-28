from tkinter import *
import numpy as np

root = Tk()

c = Canvas(root,height=500,width=500)
c.pack()

def reflect(t):

    rm = np.array([
        [1,0,0],[0,-1,0],[0,1,1]
    ])

    p1 = np.array([
        [100],[100],[1]
    ])

    p2 = np.array([
        [100], [200],[1]
    ])

    p3 = np.array([
        [200], [200],[1]
    ])


    c.create_line(int(p1[0]),int(p1[1]),int(p1[0]),int(p2[1]))
    c.create_line(int(p1[0]), int(p1[1]), int(p3[0]), int(p3[1]))
    c.create_line(int(p2[0]), int(p2[1]), int(p3[0]), int(p3[1]))

    p1r = np.dot(rm,p1)
    p2r = np.dot(rm,p2)
    p3r = np.dot(rm,p3)

    print(p1r)
    print("")
    print(p2r)
    print("")
    print(p3r)
    print("")

    c.create_line(0,250,500,250)

    c.create_line(int(p1r[0]),int(p1r[1]+500),int(p1r[0]),int(p2r[1]+500))
    c.create_line(int(p1r[0]), int(p1r[1]+500), int(p3r[0]), int(p3r[1]+500))
    c.create_line(int(p2r[0]), int(p2r[1]+500), int(p3r[0]), int(p3r[1]+500))

reflect(90)
root.title("Reflection")
root.mainloop()