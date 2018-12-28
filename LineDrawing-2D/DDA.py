from tkinter import *

root = Tk()

c = Canvas(root,height=500,width=500)
c.pack()

def drawLine(x1,y1,x2,y2):

    x = x1
    y = y1

    m = (y2-y1)/(x2-x1)

    print(m)

    if m<1:
        while x1!=x2:
            x = x+1
            y = round(y+m,2)
            print(x,y)
            c.create_oval(x, y, x, y, width=0, fill='black')

    elif m>1:
        while y!=y2:
            y = y+1
            x = round(x+1/m,2)
            print(x,y)
            c.create_oval(x, y, x, y, width=0, fill='black')

    else:
        while x!=x2:
            x = x+1
            y = y+1
            print(x,y)
            c.create_oval(x, y, x, y, width=0, fill='black')

drawLine(50,100,250,300)
root.title("DDA Line Drawing Algorithm ")
root.mainloop()

