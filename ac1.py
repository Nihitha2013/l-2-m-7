from tkinter import *
root=Tk()
root.title("Login to your account")
root.geometry("400x400")
f=Frame(master=root, height=200,width=340,bg="blue")
l1=Label(f, text="Email Id:",width=12)
l2=Label(f, text="Password:",width=12)
einp=Entry(f)
pid=Entry(f, show="*")

def display():
    ms="You have created new account.. Congratulations!!!"
    tb.insert(END,ms)

tb=Text(fg="black",bg="yellow")
b=Button(text="create Account", command=display)

f.place(x=20,y=0)
l1.place(x=20,y=80)
einp.place(x=150,y=80)
l2.place(x=20,y=140)
pid.place(x=150,y=140)
b.place(x=130,y=210)
tb.place(y=250)
root.mainloop()