import abc
from tkinter import *
import time
import datetime
import pygame

pygame.init()
root =Tk()
root.title("Music Box")
root.geometry('1352x700+0+0')
root.configure(background='white')
ABC = Frame(root,bg="powder Blue",bd=20,relief=RIDGE)
ABC.grid()
ABC1 = Frame(ABC,bg="powder Blue",bd=20,relief=RIDGE)
ABC1.grid()
ABC2 = Frame(ABC,bg="powder Blue",relief=RIDGE)
ABC2.grid()
ABC3 = Frame(ABC,bg="powder Blue",relief=RIDGE)
ABC3.grid()

str1=StringVar()
str1.set("Just Like Music")
Date1=StringVar()
Time1=StringVar()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))

#===============================================================================
def value_Cs():
    str1.set("C#")
    sound=pygame.mixer.Sound("E:\\Aditya_Verma\\python_Programming\\games\\Piano_20Tiles\\Sounds\\g4.ogg")
#============================Label With Title===================================
Label(ABC1,text="Piano Musical Keys",font=('arial',25,'bold'),padx=8,pady=8,bd=4,bg="powder Blue",fg="white",justify=CENTER).grid(row=0,column=0,columnspan=11)

#===============================================================================
txtDisplay=Entry(ABC1,textvariable=Date1,font=('arial',18,'bold'),bd=34,bg="powder blue",fg="black",width=28,justify=CENTER).grid(row=1,column=0,pady=1)

txtDisplay=Entry(ABC1,textvariable=str1,font=('arial',18,'bold'),bd=34,bg="powder blue",fg="black",width=28,justify=CENTER).grid(row=1,column=1,pady=1)

txtDisplay=Entry(ABC1,textvariable=Time1,font=('arial',18,'bold'),bd=34,bg="powder blue",fg="black",width=28,justify=CENTER).grid(row=1,column=2,pady=1)

#===============================================================================
btnCs=Button(ABC2,height=6,width=6,bd=4,text="C#",font=('arial',18,'bold'),bg="black",fg="white",command=value_Cs)
btnCs.grid(row=0,column=0,padx=5,pady=5)

btnDs=Button(ABC2,height=6,width=6,bd=4,text="D#",font=('arial',18,'bold'),bg="black",fg="white")
btnDs.grid(row=0,column=1,padx=5,pady=5)

btnSpace2=Button(ABC2,state=DISABLED,height=6,width=2,bg="powder blue",relief=FLAT)
btnSpace2.grid(row=0,column=3,padx=0,pady=0)

btnFs=Button(ABC2,height=6,width=6,bd=4,text="F#",font=('arial',18,'bold'),bg="black",fg="white")
btnFs.grid(row=0,column=4,padx=5,pady=5)

btnGs=Button(ABC2,height=6,width=6,bd=4,text="G#",font=('arial',18,'bold'),bg="black",fg="white")
btnGs.grid(row=0,column=6,padx=5,pady=5)

btnBb=Button(ABC2,height=6,width=6,bd=4,text="Bb",font=('arial',18,'bold'),bg="black",fg="white")
btnBb.grid(row=0,column=8,padx=5,pady=5)

btnSpace5=Button(ABC2,state=DISABLED,height=6,width=2,bg="powder blue",relief=FLAT)
btnSpace5.grid(row=0,column=9,padx=0,pady=0)

btnCs1=Button(ABC2,height=6,width=6,bd=4,text="C#1",font=('arial',18,'bold'),bg="black",fg="white")
btnCs1.grid(row=0,column=10,padx=5,pady=5)

btnDs1=Button(ABC2,height=6,width=6,bd=4,text="D#1",font=('arial',18,'bold'),bg="black",fg="white")
btnDs1.grid(row=0,column=12,padx=5,pady=5)

#===============================================================================

btnC=Button(ABC3,height=8,width=6,bd=4,text="C",font=('arial',18,'bold'),fg="black",bg="white")
btnC.grid(row=0,column=0,padx=5,pady=5)

btnD=Button(ABC3,height=8,width=6,bd=4,text="D",font=('arial',18,'bold'),fg="black",bg="white")
btnD.grid(row=0,column=1,padx=5,pady=5)

btnE=Button(ABC3,height=8,width=6,bd=4,text="E",font=('arial',18,'bold'),fg="black",bg="white")
btnE.grid(row=0,column=2,padx=5,pady=5)

btnF=Button(ABC3,height=8,width=6,bd=4,text="F",font=('arial',18,'bold'),fg="black",bg="white")
btnF.grid(row=0,column=3,padx=5,pady=5)

btnG=Button(ABC3,height=8,width=6,bd=4,text="G",font=('arial',18,'bold'),fg="black",bg="white")
btnG.grid(row=0,column=4,padx=5,pady=5)

btnA=Button(ABC3,height=8,width=6,bd=4,text="A",font=('arial',18,'bold'),fg="black",bg="white")
btnA.grid(row=0,column=5,padx=5,pady=5)

btnB=Button(ABC3,height=8,width=6,bd=4,text="B",font=('arial',18,'bold'),fg="black",bg="white")
btnB.grid(row=0,column=6,padx=5,pady=5)

btnC1=Button(ABC3,height=8,width=6,bd=4,text="C1",font=('arial',18,'bold'),fg="black",bg="white")
btnC1.grid(row=0,column=7,padx=5,pady=5)

btnD1=Button(ABC3,height=8,width=6,bd=4,text="D1",font=('arial',18,'bold'),fg="black",bg="white")
btnD1.grid(row=0,column=8,padx=5,pady=5)

btnE1=Button(ABC3,height=8,width=6,bd=4,text="E1",font=('arial',18,'bold'),fg="black",bg="white")
btnE1.grid(row=0,column=9,padx=5,pady=5)

btnF1=Button(ABC3,height=8,width=6,bd=4,text="F1",font=('arial',18,'bold'),fg="black",bg="white")
btnF1.grid(row=0,column=10,padx=5,pady=5)

#===============================================================================
root.mainloop()