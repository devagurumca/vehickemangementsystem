#--------------------import package-------------------------
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector
from tkcalendar import DateEntry
import time
import datetime
from tkinter import ttk


global dash

top=Tk()
top.geometry("1366x768")
#top.resizable(False,False)
#class vechile_entry():
     #------------------design-----------------------
'''def veh_design():
     c1=Canvas(c,width=1366,height=768,bg="red")
     c1.pack()'''
def vehicle_entry():
     top.destroy()
     import customerdetails

#-------------------------design----------------------------------------

def exit():
     top.destroy()
def open():
     dash=Frame(c,width=300,height=450,bg="#2f58e0")
     dash.place(x=0,y=40)
     dash1=Frame(dash,width=300,height=380,bg="#343536")
     dash1.place(x=0,y=120)
     l4=Label(dash,text="   DASH BOARD",fg="white", font="consolas 20 bold",bg="#2f58e0")
     l4.place(x=35,y=70)
     b3=Button(dash1,text="VECHILE ENTRY  ",width=25,relief=FLAT,font="consolas 18 bold",bg="#343536",activebackground="#343536",fg="yellow",command=vehicle_entry)
     b3.place(x=0,y=5)
     b4=Button(dash1,text="VIEW CUSTOMER \nSERVICE DETAILS  ",width=25,relief=FLAT,font="consolas 18 bold",bg="#343536",activebackground="#343536",fg="yellow")
     b4.place(x=0,y=65)
     b5=Button(dash1,text="BILLING",width=22,relief=FLAT,font="consolas 18 bold",bg="#343536",activebackground="#343536",fg="yellow")
     b5.place(x=0,y=150)
     b6=Button(dash1,text="VIEW DAILY \n VECHILE ENTRY",width=22,relief=FLAT,font="consolas 18 bold",bg="#343536",activebackground="#343536",fg="yellow")
     b6.place(x=0,y=200)
     b7=Button(dash1,text="EXIT",width=22,relief=FLAT,font="consolas 18 bold",bg="#343536",activebackground="#343536",fg="yellow",command=exit)
     b7.place(x=0,y=280)

     def close():
          dash.destroy()
     b2=Button(dash,image=image3,bg="#2f58e0",activebackground="#2f58e0",relief=FLAT,command=close,width=50,height=30)
     b2.place(x=0,y=2)




'''#-------------------------------Footer Area design-----------------------
footer=Frame(top,width=1366,height=90,bg="#6b6b64")
footer.place(x=0,y=658)
l=Label(footer,text="VECHILE SERVICE AND REPAIR SHOP",font="consolas 22 bold",bg="#6b6b64",fg="yellow")
l.place(x=420,y=2)
l1=Label(footer,text= "58,Bharatiya Road,jahindpuram,",bg="#6b6b64",font="consolas 12 bold",fg="yellow")
l1.place(x=500,y=35)
l2=Label(footer,text= "Madurai-11",bg="#6b6b64",font="consolas 12 bold",fg="yellow")
l2.place(x=560,y=58)'''

#-----------------------image--------------------------------------
image1=ImageTk.PhotoImage(Image.open(r'C:\Users\DEVA\AppData\Local\Programs\Python\Python37\PYTHON PROGRAM IN CENTER\shorepoint project\list.png'))
image2=ImageTk.PhotoImage(Image.open(r'C:\Users\DEVA\Downloads\wallpaperflare.com_wallpaper.jpg'))
image3=ImageTk.PhotoImage(Image.open(r'C:\Users\DEVA\AppData\Local\Programs\Python\Python37\PYTHON PROGRAM IN CENTER\shorepoint project\close (1).png'))


#------------------------------canvas for background--------------------------
c=Canvas(top,width=1366,height=768)
c.place(x=0,y=0)
c.create_image(0,0,image=image2,anchor=NW)

#------------------------header Area design------------------------
header=Frame(c,width=1366,height=40,bg="white")
header.place(x=0,y=0)
time_string = time.strftime('%H:%M %p')
date = datetime.datetime.now()
l=Label(header,text=time_string,bg="white",padx=3,pady=5,fg="blue",font="consolas 15 bold")
l.place(x=1250,y=0)
l1=Label(header,text=f"{date:%A, %B %d, %Y}",bg="white",padx=3,pady=5,fg="#1b36cf",font="consolas 15 bold")
l1.place(x=950,y=0)

# menubar icon open button
b=Button(header,image=image1,bg="white",activebackground="white",relief=FLAT,command=open)
b.place(x=0,y=2)
#ve=vechile_entry()
top.mainloop()
