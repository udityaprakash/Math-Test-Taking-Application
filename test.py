import time
import random
from tkinter import messagebox
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageTk
def bolb(y,z):
    mes=[y,z]
    con=['Attempted wrongly','Attempted correctly']
    plt.pie(mes,labels=con,autopct="%1.1f%%")
    plt.show()
def result(x,y,z):
    if len(uz)>3:
        x=3
    else:
        None
    huk=Toplevel()
    huk.geometry("1200x688")
    de=ImageTk.PhotoImage(image[0])
    des=Label(huk,image=de)
    des.pack(fill="y")
    huk.resizable(0,0)
    Button(huk,text="Anaysis",bg="yellow",fg="red",font="calibri 12 bold",command=lambda:bolb(y,z)).place(x=0,y=0)
    mnd=Frame(huk,bg="snow",width=500,height=700)
    mnd.place(x=100,y=180)
    Label(mnd,text="Congratulations",font="ariston 40 underline",bg="snow").grid(row=0,column=0,pady=10,padx=50,columnspan=2)
    Label(mnd,text="You Scored: ",font="ariston 25 bold",bg="snow").grid(row=2,pady=10,column=0)
    aqw=[]
    aqw.append(z*5)
    aqw.append("/")
    aqw.append((y+z)*5)
    Label(mnd,text=aqw,font="ariston 25 bold",bg="snow").grid(row=2,pady=10,column=1,padx=10)
    Label(mnd,text="percentage:",font="ariston 25 bold",bg="snow").grid(row=3,column=0,pady=10,padx=10)
    dzx=[]
    dzx.append((aqw[0]/aqw[2])*100)
    dzx.append("%")
    Label(mnd,text=dzx,font="ariston 25 bold",bg="snow").grid(row=3,column=1,pady=10,padx=10)
    lalp=Frame(mnd,bg="snow")
    lalp.grid(row=1,column=0,pady=20,columnspan=2)
    if dzx[0]<20.001:
            Label(mnd,text="Better Luck Next Time",font="ariston 32 bold",bg="snow").grid(row=0,column=0,padx=50,columnspan=2)
            mel=ImageTk.PhotoImage(image[2])
            me=Label(lalp,image=mel,borderwidth=0)
            me.pack(side=LEFT)
            mu=ImageTk.PhotoImage(image[2])
            Label(lalp,image=mu,borderwidth=0).pack(side=LEFT)
    elif 20.001<dzx[0]<33.003:
            ml=ImageTk.PhotoImage(image[2])
            Label(lalp,image=ml,borderwidth=0).pack(side=LEFT)
    elif 33.003<dzx[0]<51.001:
            mai=ImageTk.PhotoImage(image[3])
            Label(lalp,image=mai,borderwidth=0).pack(side=LEFT)        
    elif 51.001<dzx[0]<70.001:
            mle=ImageTk.PhotoImage(image[3])
            Label(lalp,image=mle,borderwidth=0).pack(side=LEFT)
            may=ImageTk.PhotoImage(image[3])
            Label(lalp,image=may,borderwidth=0).pack(side=LEFT) 
    elif 70.001<dzx[0]<85.001:
            mfg=ImageTk.PhotoImage(image[3])
            Label(lalp,image=mfg,borderwidth=0).pack(side=LEFT)
            my=ImageTk.PhotoImage(image[3])
            Label(lalp,image=my,borderwidth=0).pack(side=LEFT)
            kaim=ImageTk.PhotoImage(image[3])
            Label(lalp,image=kaim,borderwidth=0).pack(side=LEFT) 
    else:
            jkl=ImageTk.PhotoImage(image[3])
            Label(lalp,image=jkl,borderwidth=0).pack(side=LEFT)
            mno=ImageTk.PhotoImage(image[3])
            Label(lalp,image=mno,borderwidth=0).pack(side=LEFT)
            kim=ImageTk.PhotoImage(image[3])
            Label(lalp,image=kim,borderwidth=0).pack(side=LEFT)
            kimop=ImageTk.PhotoImage(image[3])
            Label(lalp,image=kimop,borderwidth=0).pack(side=LEFT)
            kuiim=ImageTk.PhotoImage(image[3])
            Label(lalp,image=kuiim,borderwidth=0).pack(side=LEFT)
    huk.mainloop()
    #mes=[x,y,z]
    #con=['Cheated answers','Attempted wrongly','Attempted correctly']
    #plt.pie(mes,labels=con,autopct="%1.1f%%")
    #plt.show()
def cool(hg,jk):
    if hg==jk:
        j.append("1")
        resl=Frame(root,bg="snow")
        resl.place(x=700,y=100)
        Label(resl,text="Total questions attemted:",bg="snow").grid(row=0,column=0)
        lol=len(pj)+len(j)
        Label(resl,text=lol,bg="snow").grid(row=0,column=1)
        Label(resl,text="Attempted Correctly: ",bg="snow").grid(row=1,column=0)
        Label(resl,text=len(j),bg="snow").grid(row=1,column=1)
        Label(resl,text="Attempted Wrongly: ",bg="snow").grid(row=2,column=0)
        Label(resl,text=len(pj),bg="snow").grid(row=2,column=1)
        if len(uz)<3:
            Label(resl,text="Answers Seen: ",bg="snow").grid(row=3,column=0)
            Label(resl,text=len(uz),bg="snow").grid(row=3,column=1)
        else:
            Label(resl,text="Answers Seen: ",bg="snow").grid(row=3,column=0)
            Label(resl,text="3",bg="snow").grid(row=3,column=1)
        if lol>=1:
           Button(root,text="RESULT", bg="yellow",fg="red",width=16,height=1,command=lambda:result(len(uz),len(pj),len(j))).place(x=635,y=400)
        else:
            None
        tod(et,ax)
    else:
        pj.append("0")
        resl=Frame(root,bg="snow",width=20,height=3)
        resl.place(x=700,y=100)
        Label(resl,text="Total questions attemted:",bg="snow").grid(row=0,column=0)
        lol=len(pj)+len(j)
        Label(resl,text=lol,bg="snow").grid(row=0,column=1)
        Label(resl,text="Attempted Wrongly: ",bg="snow").grid(row=2,column=0)
        Label(resl,text=len(pj),bg="snow").grid(row=2,column=1)
        Label(resl,text="Attempted Correctly: ",bg="snow").grid(row=1,column=0)
        Label(resl,text=len(j),bg="snow").grid(row=1,column=1)
        if len(uz)<3:
            Label(resl,text="Answers Seen: ",bg="snow").grid(row=3,column=0)
            Label(resl,text=len(uz),bg="snow").grid(row=3,column=1)
        else:
            Label(resl,text="Answers Seen: ",bg="snow").grid(row=3,column=0)
            Label(resl,text="3",bg="snow").grid(row=3,column=1)    
        if lol>=1:
           Button(root,text="RESULT", bg="yellow",fg="red",width=16,height=1,command=lambda:result(len(uz),len(pj),len(j))).place(x=635,y=400)
        else:
            None
        tod(et,ax)
def callback():
    hj=messagebox.askokcancel("Quit","Do you really want to exit the Exam")
    if (hj):  
        root.quit()
    else:
        None
def ma(pi):
    opq=Label(uuq,text="ANSWER",font="ariston 22 bold",)
    opq.grid(row=0,column=0)
    yy=Label(uuq,text=pi,font="calibri 20 bold",fg="blue",width=16,height=1)
    yy.grid(row=1,column=0)
    uz.append("q")
def tod(et,ax):    
         to=random.randint(1533,9999)
         mu=random.randint(et,ax)
         Label(toot,text=to,bg="snow",font="calibri 30 bold").grid(row=0,column=0)
         Label(toot,text=mu,bg="snow" ,font="calibri 30 underline",width=10,height=1).grid(row=1,column=0)
         tow=to*mu
         Entry(toot,textvariable=go,font="calibri 15 bold").grid(row=2,column=0)
         Button(root,text="NEXT", bg="yellow",fg="red",width=16,height=1,command=lambda:cool(tow,go.get())).place(x=635,y=300)
         global bac
         if len(uz)<3:
             bac=Button(root,text="ANSWER", bg="yellow",fg="red",width=16,height=1,command=lambda:ma(tow))
             bac.place(x=635,y=350)
         else:
             bac.place_forget()
             uuq.place_forget()
def kal():
    hj.place(x=9999,y=0)
    azx.place(x=8880,y=0)
    bal.place(x=16000,y=0)
    messagebox.showinfo("Wishes","All the Best For your Exam")
    global et
    et=1
    global ax
    ax=9
    tod(et,ax)
def lds():
    hj.place(x=9999,y=0)
    azx.place(x=8888,y=0)
    bal.place(x=16000,y=0)
    messagebox.showinfo("Best Wishes","All the Best For your Exam")
    global et
    et=11
    global ax
    ax=100
    tod(et,ax)
def pls():
    hj.place(x=9999,y=0)
    azx.place(x=8888,y=0)
    bal.place(x=16000,y=0)
    messagebox.showinfo("Best Wishes","All the Best For your Exam")
    global et
    et=200
    global ax
    ax=999
    tod(et,ax)
root=Tk()
j=[]
pj=[]
go=IntVar()
uz=[]
to=[]
mu=[]
mn=[]
global image
image=[]
image.append(Image.open("destro.jpg"))
image.append(Image.open("tyr.jpg"))
image.append(Image.open("download.jpg"))
image.append(Image.open("hgf.jpg"))
plu=ImageTk.PhotoImage(image[1])
dos=Label(root,image=plu)
dos.pack()
root.title("Maths Test")
root.geometry("1000x500")
root.protocol("WM_DELETE_WINDOW",callback)
messagebox.showinfo("Exam Level","First Choose Examnation Level i.e Easy, Medium or Hard at top left corner")
mm=Label(root,text="Multiply the following:",font="calibri 30 underline")
mm.place(x=400,y=0)
bec=Frame(root)
bec.place(x=935,y=100)
Label(bec,text="NOTE: ",fg="red").pack()
Label(bec,text="Each correct Question").pack()
Label(bec,text="contains 5 marks").pack()
uuq=Frame(root,width=0,height=0)
uuq.place(x=100,y=200)
hj=Button(root,text="Easy",width=10,height=1,command=kal)
hj.place(x=0,y=0)
azx=Button(root,text="Medium",width=10,height=1,command=lds)
azx.place(x=80,y=0)
bal=Button(root,text="Hard",width=10,height=1,command=pls)
bal.place(x=160,y=0)
toot=Frame(root,bg="snow",width=0,height=0)
toot.place(x=435,y=100)
Label(root,text=".......You can only see answers of max 3 Questions.......",font="calibri 20").place(x=400,y=450)
root.mainloop()
