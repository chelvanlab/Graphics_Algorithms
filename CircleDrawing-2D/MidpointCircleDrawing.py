from tkinter import *
from math import *

root = Tk()

c = Canvas(root,height=500,width=500)
c.pack()


def drawCircle(ox,oy,r):

    x = 0
    y = r

    xtemp = x
    ytemp = y

    pk = 1-r

    print(pk)

    if pk<0:
        x = x+1
        y = y
        print(x,y)
        c.create_oval(ox+x, oy-y, ox+x, oy-y, width=0, fill='black')

        while x<y:

            pk = round(pk + 2*(xtemp+1) + (pow(y,2)-pow(ytemp,2)) - (y-ytemp) +1)

            xtemp = x
            ytemp = y

            if pk<0:
                x = x+1
                y = y
                print(x,y)
                c.create_oval(ox + x, oy - y, ox + x, oy - y, width=0, fill='black')

            else:
                x = x+1
                y = y-1
                print(x,y)
                c.create_oval(ox + x, oy - y, ox + x, oy - y, width=0, fill='black')


drawCircle(200,200,80)
root.mainloop()