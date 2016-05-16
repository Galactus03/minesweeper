""" Mine version of minesweeper against somya's"""

from Tkinter import *
import tkMessageBox
import random

#creating the first frame
main=Tk()
main.title("Minesweeper")
grid_size=0
grid_size_label=Label(main,text="Select the grid size : ",font=("Times", 15,"bold"))

#This is the main function that will do all the mines thingy
def create_grid(x,mine_grid):
# x here is the grid size
    grid_dict={}
    cells_position={}
    for i in range(0,x):
        for j in range(0,x):
            grid_dict[i,j]=Button(mine_grid,text=str(i)+","+str(j))
            grid_dict[i,j].grid(row=i,column=j)
            cells_position[i,j]=0

#genrating the mines,the position with mines will be marked "*"
    for i in range(1,x/2+1):
        mine_x=random.randint(0,8)
        mine_y=random.randint(0,8)
        cells_position[mine_x,mine_y]="*"

#now we will find number of mines around each cell and mark them so
    possible_movements=[(x,y)for x in range(-1,2) for y in range(-1,2) if (y!=0 or x!=0)]
    for key in cells_position:
        if cells_position[key] != "*":
            mine_value=0
            for movement in possible_movements:
                if (key[0]+movement[0],key[1]+movement[1]) in cells_position:
                    if cells_position[key[0]+movement[0],key[1]+movement[1]] == "*":
                        mine_value+=1
            cells_position[key]=mine_value
            print cells_position,"cells_position"
            grid_dict[key]["text"]=mine_value


def small_grid():
    grid_size=8
    print grid_size,"Grid size selected "
    main.destroy()
    mine_frame=Tk()
    create_grid(grid_size,mine_frame)
    mine_frame.mainloop()


def medium_grid():
    grid_size=16
    print grid_size,"Grid size selected"
    main.destroy()
    mine_frame=Tk()
    create_grid(grid_size,mine_frame)
    mine_frame.mainloop()

def large_grid():
    grid_size=32
    print grid_size,"Grid size selected"
    mine_frame=Tk()
    main.destroy()
    create_grid(grid_size,mine_frame)
    mine_frame.mainloop()

small_button=Button(main,text="SMALL",command=small_grid)
medium_button=Button(main,text="MEDIUM",command=medium_grid)
large_button=Button(main,text="lARGE",command=large_grid)
grid_size_label.pack(fill=BOTH)
small_button.pack(fill=BOTH)
medium_button.pack(fill=BOTH)
large_button.pack(fill=BOTH)




main.mainloop()
