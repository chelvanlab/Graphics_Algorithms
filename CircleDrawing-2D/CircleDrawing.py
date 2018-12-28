from tkinter import *
import math

root = Tk()

c = Canvas(root,height=500,width=500)
c.pack()

def drawCircle(ox,oy,r):

    for i in range(0,361):
        x = r*round(math.cos(math.radians(i)),2)
        y = r*round(math.sin(math.radians(i)),2)

        x = ox+x
        y = oy-y
        print(x,y)
        c.create_oval(x, y, x, y, width=0, fill="black")

drawCircle(150,150,100)
root.mainloop()