from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector
from tkcalendar import DateEntry
import time
import datetime
from tkinter import ttk

#----------- declaration------------
global v
top=Tk()
top.geometry("1366x768")
def back():
     top.destroy()
     import main
     
def clear():
     e.delete(0,END)
     e1.delete(0,END)
     e2.delete(0,END)
     e3.delete(0,END)
     e4.delete(0,END)
     e5.delete(0,END)
     e6.delete(0,END)
     e7.delete(0,END)
     
def requested():
     db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="shorepoint")
     cursordb = db.cursor()

     vtype=e.get()
     vnumber=e1.get()
     cname=e2.get()
     vmodel=e3.get()
     sertype=e4.get()
     phno=e5.get
     cdate=e6.get()
     add=e7.get()
     
     if vtype == "":
          messagebox.showerror("REQURIED","no value in vehicle type field")
     elif vnumber=="":
          messagebox.showerror("REQURIED","no value in vehicle number field")
     elif cname =="":
          messagebox.showerror("REQURIED","no value in customer name field")
     elif vmodel =="":
          messagebox.showerror("REQURIED","no value in vehicle model field")
     elif  sertype =="":
          messagebox.showerror("REQURIED","no value in serving type field")
     elif phno=="":
          messagebox.showerror("REQURIED","no value inphone numberfield")
     elif cdate =="":
          messagebox.showerror("REQURIED","no value in current date field")
     elif add =="":
          messagebox.showerror("REQURIED","no value in address field")       
     else:
          print(vtype)
          print(vnumber)
          print(cname)
          print(vmodel)
          print(sertype)
          
          #print(sql)
          sql="INSERT INTO vehicleentry (id, vehicletype,vehiclenumber,ownerfullname,vehiclemodel,servicetype,phonenumber,date,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
          val=("",vtype,vnumber,cname,vmodel,sertype,phno,cdate,add)
          cursordb.execute(sql,val)
          '''chk=messagebox.showinfo("successfully","your record added successfully")
          if chk == 1:
               e.delete(0,END)
               e1.delete(0,END)
               e2.delete(0,END)
               e4.delete(0,END)
               e5.delete(0,END)
               e6.delete(0,END)
               e7.delete(0,END)'''
          db.commit()
          cursordb.close()
def caps(event):
    v.set(v.get().upper())

#-----------------------image--------------------------------------
image1=ImageTk.PhotoImage(Image.open(r'C:\Users\DEVA\Downloads\download (1) (1).png'))
image2=ImageTk.PhotoImage(Image.open(r'C:\Users\DEVA\AppData\Local\Programs\Python\Python37\PYTHON PROGRAM IN CENTER\shorepoint project\close (1).png'))
#---------------design for products-------------

#------------------------header Area design------------------------
header=Frame(top,width=1366,height=40,bg="#343536")
header.place(x=0,y=0)
time_string = time.strftime('%H:%M %p')
date = datetime.datetime.now()
l=Label(header,text=time_string,bg="#343536",padx=3,pady=5,fg="yellow",font="consolas 15 bold")
l.place(x=1250,y=0)
l1=Label(header,text=f"{date:%A, %B %d, %Y}",bg="#343536",padx=3,pady=5,fg="yellow",font="consolas 15 bold")
l1.place(x=950,y=0)
def exit():
     top.destroy()
def open():
     dash=Frame(top,width=250,height=100,bg="white")
     dash.place(x=0,y=45)
     b3=Button(dash,text="BACK ",width=18,relief=FLAT,font="consolas 18 bold",bg="white",activebackground="yellow",fg="blue",command=back)
     b3.place(x=0,y=50)
     

     def close():
          dash.destroy()
     b2=Button(dash,image=image2,bg="white",activebackground="white",relief=FLAT,command=close,width=50,height=30)
     b2.place(x=0,y=2)

b=Button(header,image=image1,bg="#343536",activebackground="#343536",relief=FLAT,command=open)
b.place(x=0,y=2)
#-----------frame for add products--------------------------
f=Frame(top,width=1100,height=450,bg="white")
f.place(x=130,y=160)

l=Label(f,text="FILL SERVICE REQUESTED FORM", font="consolas 26 bold",bg="white",fg="black")
l.place(x=30,y=10)
#categories
l1=Label(f,text="Vehicle Type  :", font="consolas 22 bold",bg="white",fg="black")
l1.place(x=50,y=100)
cag=StringVar()
combo1=['2 Wheeler','3 Wheeler','4 Wheeler']
e=ttk.Combobox(f,font="consolas 15 bold",textvariable=cag,values=combo1)

e.current()

e.place(x=300,y=110)
#e.config(combo1=plus)
#product l
l3=Label(f,text="Vehicle Number:", font="consolas 22 bold",bg="white",fg="black")
l3.place(x=580,y=100)
v=StringVar()
e1=Entry(f,highlightthickness=2,highlightbackground="black",textvariable=v,font="consolas 15 bold")
e1.place(x=820,y=110)
e1.bind("<KeyRelease>", caps)

#pname
l4=Label(f,text="Owner Fullname:", font="consolas 22 bold",bg="white",fg="black")
l4.place(x=50,y=150)
pname=StringVar()
e2=Entry(f,font="consolas 15 bold",highlightthickness=2,highlightbackground="black",width=21)
e2.place(x=300,y=160)

#mrp
l5=Label(f,text="Vehicle Model:", font="consolas 22 bold",bg="white",fg="black")
l5.place(x=580,y=150)
e3=Entry(f,highlightthickness=2,highlightbackground="black",font="consolas 15 bold")
e3.place(x=820,y=160)
#quantiy type
l6=Label(f,text="Service Type  :", font="consolas 22 bold",bg="white",fg="black")
l6.place(x=50,y=200)
combo2=['wash','Dent removal ','Tyre change']
qty=StringVar()

e4=ttk.Combobox(f,font="consolas 15 bold",textvariable=qty,values=combo2)
e4.place(x=300,y=210)
e4.current()


#vali=f.register(validate)
#e4.configure(validate="key",validatecommand =(vali,"%P"))

#sp
l7=Label(f,text="Phone number :", font="consolas 22 bold",bg="white")
l7.place(x=580,y=200)
e5=Entry(f,font="consolas 15 bold",highlightthickness=2,highlightbackground="black")
e5.place(x=820,y=210)
#date
l7=Label(f,text="Date\t      :", font="consolas 22 bold",bg="white",fg="black")
l7.place(x=50,y=250)
e6=DateEntry(f,border=0,font="consolas 15 bold")
e6.place(x=300,y=260)
#address
l8=Label(f,text="Address      :", font="consolas 22 bold",bg="white",fg="black")
l8.place(x=580,y=250)
e7=Entry(f,border=0,font="consolas 15 bold",highlightthickness=2,highlightbackground="black")
e7.place(x=820,y=260)


#add button
b5= Button(f,text="REQUESTED",bg="blue",activebackground="white",font="consolas 20 bold",fg="white",command=requested)
b5.place(x=270,y=370)
#update button
b6= Button(f,text="CLEAR",bg="red",activebackground="red",font="consolas 20 bold",width=7,fg="white",command=clear)
b6.place(x=600,y=370)

top.mainloop()

     
