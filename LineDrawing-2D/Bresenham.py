from tkinter import *

root = Tk()

c = Canvas(root,height=500,width=500)
c.pack()

def drawLine(x1,y1,x2,y2):

    x = x1
    y = y1

    xtemp = x
    ytemp = y

    dy = y2-y1
    dx = x2-x1
    tdy = 2*dy
    tdx = 2*dx

    m = dy/dx
    print(m)

    # m < 1
    if m<1:

        pk = tdy-dx

        if pk>0:
           x = x+1
           y = y+1
           print(x,y)
           c.create_oval(x, y, x, y, width=0, fill='black')

           while x!=x2:

               pk = pk + tdy - tdx * (y-ytemp)

               ytemp = y

               if pk>=0:
                   x = x+1
                   y = y+1
                   print(x,y)
                   c.create_oval(x, y, x, y, width=0, fill='black')

               else:
                   x = x+1
                   y = y
                   print(x,y)
                   c.create_oval(x, y, x, y, width=0, fill='black')

    #m>1
    elif m>1:

        pk = tdx - dy

        if pk>0:
            x = x+1
            y = y+1

            while y!=y2:

                pk = pk + tdx - tdy * (x - xtemp)

                xtemp = x

                if pk>=0:
                    x = x+1
                    y = y+1
                    print(x,y)
                    c.create_oval(x, y, x, y, width=0, fill='black')

                else:
                    x = x
                    y = y+1
                    print(x, y)
                    c.create_oval(x, y, x, y, width=0, fill='black')

    #m=1
    else:
        while x!=x2:
            x = x+1
            y = y+1
            print(x,y)
            c.create_oval(x, y, x, y, width=0, fill='black')


drawLine(50,100,250,300)
root.title("Bresenham Line Drawing Algorithm ")
root.mainloop()


