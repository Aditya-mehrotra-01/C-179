from tkinter import *
import random

root=Tk()
root.geometry("400x300")
root.title("Encapsulation")
label_score=Label(root,bg="white")
label_score['text']="Score:0"
label_score.place(relx=0.1,rely=0.2,anchor=CENTER)
label_co=Label(root, bg="white")
label_co.place(relx="0.5", rely="0.4" ,anchor=CENTER)
label_name=Label(root,bg="white")
label_name.place(relx=0.4,rely=0.4,anchor=CENTER)
input_value = Entry(root)
input_value.place(relx=0.2,rely=0.5, anchor= CENTER)


class score():
    
    def __init__(self):
        self.__score=0
        
    def updatescore(self,input_value):
        self.text=["BLUE","GREEN","RED","YELLOW"]
        self.random_no_text = random.randint(0,3)
        
        self.color=["blue","green","red","yellow"]
        self.random_no_color=random.randint(0, 3)
        
        label_co["text"] = self.text[self.random_no_text]
        label_co["fg"] = self.color[self.random_no_color]
        
obj=score()

btn=Button(root,text="start",command=score)
btn.place(relx=0.6,rely=0.8,anchor=CENTER)
input_value.delete(0,END)
root.mainloop()