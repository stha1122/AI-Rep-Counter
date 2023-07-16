from tkinter import *
from bicepCurlCounter import *
from pushUpCounter import *
from squat import *
from PIL import ImageTk,Image
def bicepCurl(root):
    root.title("AI rep Counter")
    root.geometry("1800x1000+0+0")
    button1=Button(root,text="Start",width=20,command=lambda:change1(root))
    button1.place(x=250,y=750)
    button2 = Button(root, text="Start", width=20, command=lambda: change2(root))
    button2.place(x=700, y=750)
    button3 = Button(root, text="Start", width=20, command=lambda: change3(root))
    button3.place(x=1150, y=750)


def change1(root):
    root.destroy()
    bicepCurlCounter()

def change2(root):
    root.destroy()
    puspUpConuter()

def change3(root):
    root.destroy()
    sitUpCounter()
def call():
    root=Tk()
    canvas=Canvas(root,width=2000,height=900)
    photo=ImageTk.PhotoImage(Image.open("C:\\Users\\Swetha\\Desktop\\DIP\\front design3.png"))
    canvas.create_image(0,0,anchor=NW,image=photo)
    canvas.pack()
    bicepCurl(root)
    root.mainloop()
call()