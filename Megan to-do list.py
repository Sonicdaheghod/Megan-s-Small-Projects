#making a to-do list

#tkinter helps make the user interface for the to-do list
from tkinter import *
from tkinter import ttk

#------First - make a user interface window--------
#making a class
class theToDoList:
    def __init__(self, root):
        pass

#starting execution of program point
def main():
    root = Tk() #tk helps bring many tools for the application I am making
#root is a window where different tools go to 
    userInterface = theToDoList(root)
    root.mainloop()
    #mainloop allows the todo list to identify for actions from user such as clicking until the user exits it

if __name__ == "__main__":
    main()

#Video used: https://www.youtube.com/watch?v=mmpVsw8aXi4&list=PLXCw5VdOQb7gCT0gC5jg66carWh48JcOy&index=4 
# 4:03