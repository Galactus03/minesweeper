#MineSweeper

from Tkinter import *
import tkMessageBox

frame = Tk()


Label(frame, text="Enter the grid size n:").grid(row=0)
e1=Entry(frame)
e1.grid(row=0,column=1)

def fetch_grid_size():
    grid_size = e1.get()
    type(grid_size)


    x={}
    for i in range (1,grid_size+1):
        for j in range(1,grid_size+1):

            x[i,j]=Button(frame,text=str(i)+str(j),height=2,width=2).grid(row=i,column=j)

Button(frame,text='ok',command=fetch_grid_size).grid(row=1,column=0,sticky=W,pady=4)





#button1['state']='disabled' -------for disabling a button


#main.minsize(height=600,width=400)


frame.mainloop()
