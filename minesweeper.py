"""An hackable minesweeper game"""
#MineSweeper

from Tkinter import *
import tkMessageBox
from random import *
import math
frame = Tk()


Label(frame, text="Enter the grid size n:").grid(row=0,column=0)
e1=Entry(frame)
e1.grid(row=1,column=0)

def mine_positions(n,m):
    no_of_mines=math.floor((n**2)/4.0)
    print 'no_of_mines',no_of_mines
    pos=[]
    for i in range(0,int(no_of_mines)):
        while True:
            k=randint(0,len(m))
            print len(m)
            z=(m)[k]
            if z not in pos:
                pos.append(z)
                break
    return pos


def fetch_grid_size():
    grid_size = e1.get()
    size_of_grid=int(grid_size)
    x={}
    for i in range (1,size_of_grid+1):
        for j in range(1,size_of_grid+1):
            x[i,j]=Button(frame,text=str(i)+','+str(j),height=1,width=1)
            x[i,j].grid(row=i,column=j)

        (x.keys()).sort()

    mine_pos=mine_positions(size_of_grid,x.keys())
    print mine_pos




Button(frame,text='ok',command=fetch_grid_size).grid(row=2,column=0,sticky=W,pady=4)









#button1['state']='disabled' -------for disabling a button


#main.minsize(height=600,width=400)


frame.mainloop()
