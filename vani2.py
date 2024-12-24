from tkinter import*
a=Tk()
f=Label(a,text="Enter the name:",font="Lucida 10")
f.grid(row=0,column=1)
eb=Entry(a,font="Lucida 10")
eb.grid(row=0,column=4)
f2=Label(a,text="Enter the roll number:",font="Lucida 10")
f2.grid(row=1,column=1)
eb2=Entry(a,font="Lucida 10")
eb2.grid(row=1,column=4)
b=Button(a,text="save")
b.grid(row=5,column=2)
b2=Button(a,text="Delete")
b2.grid(row=5,column=5)
a.geometry("500x500")
n=["ven","car","bike","bus"]

a.mainloop()
