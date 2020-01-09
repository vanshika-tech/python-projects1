
from tkinter import *
import random
#import tkMesaageBox

answers=["python", 
"java", 
"swift", 
"canada", 
"india", 
"america", 
"london", 
]

words=["nptoyh", 
"avja", 
"wfsit", 
"cdanaa", 
"aidin", 
"aiearcm", 
"odnlon", 
]
num=random.randrange(0,7,1)

def reset():
    global words,answers,num
    num=random.randrange(0,7,1)
    lbl.config(text=words[num])
    txt.delete(0,END)

def default():
    global words,answers,num
    lbl.config(text=words[num])

def checkans():
    global words,answers,num
    var=txt.get()
    if(var==answers[num]):
        print("success")
        #tkMessageBox.showinfo("Success","This is the correct answer")
        reset()
    else:
        print("error")
        #tkMessageBox.showinfo("Error","This is the wrong answer")
        txt.delete(0,END)


root=Tk()
root.geometry("350x400+400+300")
root.title("JumblledGame")
root.configure(background="#000000")
lbl=Label(root,text="Start the Game",font=("verdana",18),bg="#000000",fg="#ffffff")
lbl.pack(pady=30,ipady=10,ipadx=10)
txt=Entry(root,font=('verdana,16'))
txt.pack(ipady=5,ipadx=5)
cbtn=Button(root,text="Check",font=("Comic sans ms",16),width=16,bg="#4C4B4B",fg="#6ab04c",relief=GROOVE, command=checkans)
cbtn.pack(pady=40)
sbtn=Button(root,text="Reset",font=("Comic sans ms",16),width=16,bg="#4C4B4B",fg="#EA425C",relief=GROOVE, command=reset)
sbtn.pack(pady=5)

default()

root.mainloop()
