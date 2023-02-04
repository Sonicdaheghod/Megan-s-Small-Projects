#Video used as reference: https://www.youtube.com/watch?v=mmpVsw8aXi4&list=PLXCw5VdOQb7gCT0gC5jg66carWh48JcOy&index=4 
#making a Friend making app
#Significance of this program: I have read some articles about college students and even adults having trouble making new friends.  
    #As a result, I was inspired to create this program to help these people learn and understand how to make friends using the resources this app can provide to them. 
    #This user interface allows the user to control what resources they want to use that aids them in their friend-making journey.

#tkinter helps make the user interface for the app
from tkinter import *
from tkinter import ttk

#------make a user interface window--------
#making a class
class theToDoList:
    def __init__(self, root):
        self.root = root
    #creating title to show up on application
        ##you HAVE to use title and geometry respectively, cannot create another name
        self.root.title("List of Resources for Making Friends")
    #creating shape of program
        self.root.geometry("700x500+400+200")

    #sets the title of the program for users to see on interface and decorates it based on font/color
        self.label = Label(self.root, text= "The App That Helps You Make Friends!",
            font= "Times, 30 bold", width=20,bd=10, bg = "lightseagreen", fg = "black")
        self.label.pack(side="top", fill=BOTH)

    #adding the button: "add task"
        self.secondLabel = Label(self.root, text= "Additional Friendly Resources",
            font= "Times, 22 bold", width=25,bd=13, bg = "lightseagreen", fg = "black")
        self.label.pack(side="top", fill=BOTH)
        #position for the button
        self.secondLabel.place(x=20, y=90)

    #adding label that shows the collective list of resources
        self.thirdLabel = Label(self.root, text= "Resources",
            font= "Times, 22 bold", width=15,bd=13, bg = "lightseagreen", fg = "black")
        self.label.pack(side="top", fill=BOTH)
        #position for the button
        self.thirdLabel.place(x=750, y=90)

    #text box that shows all the resources
        self.boxResources = Listbox(self.root,
            height = 14, bd = 4, width = 45, font = "Times, 20 italic bold") 
        #position of text box
        self.boxResources.place(x = 550, y = 170)

    #adding text box under where user can add resources by typing what they want in it
        self.textBox = Text(self.root,font= "Times, 20 bold", height = 2.25, width=30,bd=10)
        self.textBox.place(x=20, y = 170)

    #-------Making the function so that user can add and delete a resource on list-------------
        def addResource():
            resourceInput = self.textBox.get(1.0,END)
            #the get(1.0,END) means it will focus on everything typed in the box
            self.boxResources.insert(END,resourceInput) #this gets the text in the text box and puts it into the lsit of resources box
            with open("appData.txt","a") as file: #w means to write, a means append
                file.write(resourceInput)
                file.seek(0)
                file.close()
            self.textBox.delete(1.0,END) #this removes what we typed in the add resource box after user presses "add resource"

        def deleteResource():
            removeResource = self.boxResources.curselection()
            getResourceToDelete = self.boxResources.get(removeResource)
            with open("appData.txt","r+") as f: #r+ determines number of bytes in a file
                newF = f.readlines()
                f.seek(0) #seek changes the position of file to a given position
                for line in newF:
                    item = str(getResourceToDelete)
                    if item not in line:
                        f.write(line)
                    f.truncate() #resizes file to given number of bytes
                self.boxResources.delete(removeResource) #must keep "delete" since that is the corresponding function for delete button to work.

        with open("appData.txt", "r") as file:
            readFile = file.readlines()
            for i in readFile:
                isReady = i.split() #split makes things in a string into a list format
                self.boxResources.insert(END, isReady)
            file.close()

        #creating button for adding and deleting a resource

        ##1- "add resource" button
        self.button = Button(self.root, text="Add", font= "Times, 22 bold", fg="lightcoral",command = addResource)
        self.button.place(x=20, y = 200)
        ##2-"delete resource" button
        self.button = Button(self.root, text="Delete", font= "Times, 22 bold", fg="lightcoral",command = deleteResource)
        self.button.place(x=40, y = 200)
#starting execution of program point
def main():
    root = Tk() #tk helps bring many tools for the application I am making
#root is a window where different tools go to 
    userInterface = theToDoList(root)
    root.mainloop()
    #mainloop allows the todo list to identify for actions from user such as clicking until the user exits it


    
if __name__ == "__main__":
    main()
