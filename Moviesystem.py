#from dbm import _Database
from email.mime import message
from msilib import Table
from msilib.schema import ListBox
from multiprocessing.sharedctypes import Value
#from ssl import _PasswordType
from tkinter import  *
import tkinter as ttk
from tkinter import ttk
from tkinter.ttk import Combobox
from webbrowser import get
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter



class MovieBookingSystem():
    def __init__(self,root):
        self.root=root
        self.root.title("Movie Booking System")
        self.root.geometry("1440x700+0+0")
        def label(self):
                self.backGroundImage=PhotoImage(file="BG2")
                self.backGroundImagelabel=label(self,iamge=self.backGroundImage)
                self.backGroundImagelabel.place(X=0,Y=0)

        #==============================================variable=====================================
        self.Name=StringVar()
        self.Contact_no=StringVar()
        self.No_of_seats=StringVar()
        self.Print=StringVar()
        self.Date=StringVar()
        self.Time=StringVar()
        self.Location=StringVar()
        self.Movie_name=StringVar()
        self.Duration=StringVar()
        self.Price=StringVar()
        self.Total_Amount=StringVar()

        

        lbltitle=Label(self.root,text="Movie Booking System",bg ='beige',fg="maroon",bd=20,relief=RIDGE,font=("",30,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=8,relief=RIDGE,padx=5,bg="beige")
        frame.place(x=0,y=110,width=1530,height=400)
        
        #==================================Data Frame Left===================================
        
        DataFrameLeft=LabelFrame(frame,text="Movie Information",bg ='beige',fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=0,width=700,height=350)

        lblName=Label(DataFrameLeft,bg="beige",text="Name:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblName.grid(row=0,column=0,sticky=W)

        txtName=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.Name,width=25)
        txtName.grid(row=0,column=1)

        lblContact=Label(DataFrameLeft,bg="beige",text="Contact No:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblContact.grid(row=1,column=0,sticky=W)
         
        txtContact=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.Contact_no,width=25)
        txtContact.grid(row=1,column=1)

        lblseats=Label(DataFrameLeft,bg="beige",text="No of Seats:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblseats.grid(row=2,column=0,sticky=W)

        txtseats=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.No_of_seats,width=25)
        txtseats.grid(row=2,column=1)

        lblPrint=Label(DataFrameLeft,bg="beige",text="Print:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblPrint.grid(row=3,column=0,sticky=W)

        coPrint= Combobox(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.Print,width=22,state="readonly")
        coPrint["value"]=("2D","3D","IMAX")
        coPrint.current(0)
        coPrint.grid(row=3,column=1)

        lblDate=Label(DataFrameLeft,bg="beige",text="Date:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblDate.grid(row=4,column=0,sticky=W)

        txtDate=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.Date,width=25)
        txtDate.grid(row=4,column=1)

        lblTime=Label(DataFrameLeft,bg="beige",text="Time:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblTime.grid(row=5,column=0,sticky=W)
        
        coTime= Combobox(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.Time,width=22,state="readonly")
        coTime["value"]=("10:00 am","12:00 pm","3:00pm","6:00 pm","8:00pm")
        coTime.current(0)
        coTime.grid(row=5,column=1)

        lblLocation=Label(DataFrameLeft,bg="beige",text="Location:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblLocation.grid(row=6,column=0,sticky=W)
        
        coLocation= Combobox(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.Location,width=22,state="readonly")
        coLocation["value"]=("PVR Pavillion Mall","INOX Amanora","PVR SGS","INOX Westen","PVR Phoneix")
        coLocation.current(0)
        coLocation.grid(row=6,column=1)

        lblMovie=Label(DataFrameLeft,bg="beige",text="Movie Name:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblMovie.grid(row=7,column=0,sticky=W)

        txtMovie=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.Movie_name,width=25)
        txtMovie.grid(row=7,column=1)

        lblDuration=Label(DataFrameLeft,bg="beige",text="Duration:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblDuration.grid(row=8,column=0,sticky=W)

        txtDuration=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.Duration,width=25)
        txtDuration.grid(row=8,column=1)

        lblPrice=Label(DataFrameLeft,bg="beige",text="Price:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblPrice.grid(row=0,column=2,sticky=W)

        txtPrice=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.Price,width=25)
        txtPrice.grid(row=0,column=3)

        lblTotalAmt=Label(DataFrameLeft,bg="beige",text="Total Amount:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblTotalAmt.grid(row=1,column=2,sticky=W)

        txtTotalAmt=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.Total_Amount,width=25)
        txtTotalAmt.grid(row=1,column=3)

        #==================================Data Frame Right===================================
        
        DataFrameRight=LabelFrame(frame,text="Movie Details",bg ='powder blue',fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=710,y=0,width=600,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listMovie=['RRR','Spiderman far from home','The Nun','Student of the year 2',
        'Sairat','Tumbbad','James Bond','Drishyam 2','Inception','Interstellar']
        
        def selectmovie(event=""):
            value=str(listBox.get(listBox.curselection))
            x=value
            if (x=="RRR"):
                self.Movie_name.set("RRR")
                self.Duration.set("165 min")
                self.Price.set("Rs.350")

            elif (x=="Spiderman far from home"):
                self.Movie_name.set("Spiderman far from home")
                self.Duration.set("200 min")
                self.Price.set("Rs.150")

            elif (x=="The Nun"):
                self.Movie_name.set("The Nun")
                self.Duration.set("119 min")
                self.Price.set("Rs.150")

            elif (x=="Student of the year 2"):
                self.Movie_name.set("Student of the year 2")
                self.Duration.set("180 min")
                self.Price.set("Rs.300")

            elif (x=="Sairat"):
                self.Movie_name.set("Sairat")
                self.Duration.set("150 min")
                self.Price("Rs.100")

            elif (x=="Tumbbad"):
                self.Movie_name.set("Tumbbad")
                self.Duration.set("145 min")
                self.Price.set("Rs.210")
            
            elif (x=="James Bond"):
                self.Movie_name.set("James Bond")
                self.Duration.set("125 min")
                self.Price.set("Rs.250")

            elif (x=="Drishyam 2"):
                self.Movie_name.set("Drishyam 2")
                self.Duration.set("200 min")
                self.Price.set("Rs.300")
            
            elif (x=="Inception"):
                self.Movie_name.set("Inception")
                self.Duration.set("145 min")
                self.Price.set("Rs.100")

            elif (x=="Interstellar"):
                self.Movie_name.set("Interstellar")
                self.Duration.set("125 min")
                self.Price.set("Rs.135")
            


        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=25,height=16)
        listBox.bind("<<ListboxSelect>>",selectmovie)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=Listbox.yview)

        for item in listMovie:
            listBox.insert(END,item)

        #==================================Buttons Frame ===================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=500,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=22,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.show_data,text="Show Data",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

       # btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),#width=21,bg="blue",fg="white")
       # btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=22,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)
        #==================================Information Frame ===================================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=570,width=1530,height=195)
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1320,height=175)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.movie_table=ttk.Treeview(Table_frame,column=("Name","Contact_no","No_of_seats","Print","Date","Time","Location","Movie_name","Duration","Price","Total_Amount"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.movie_table.xview)
        yscroll.config(command=self.movie_table.yview)


        self.movie_table.heading("Name",text="Name")
        self.movie_table.heading("Contact_no",text="Contact_no")
        self.movie_table.heading("No_of_seats",text="No_of_seats")
        self.movie_table.heading("Print",text="Print")
        self.movie_table.heading("Date",text="Date")
        self.movie_table.heading("Time",text="Time")
        self.movie_table.heading("Location",text="Location")
        self.movie_table.heading("Movie_name",text="Movie_name")
        self.movie_table.heading("Duration",text="Duration")
        self.movie_table.heading("Price",text="Price")
        self.movie_table.heading("Total_Amount",text="Total_Amount")
        
        self.movie_table["show"]="headings"
        self.movie_table.pack(fill=BOTH,expand=1)

        self.movie_table.column("Name",width=100)
        self.movie_table.column("Contact_no",width=100)
        self.movie_table.column("No_of_seats",width=100)
        self.movie_table.column("Print",width=100)
        self.movie_table.column("Date",width=100)
        self.movie_table.column("Time",width=100)
        self.movie_table.column("Location",width=100)
        self.movie_table.column("Movie_name",width=100)
        self.movie_table.column("Duration",width=100)
        self.movie_table.column("Price",width=100)
        self.movie_table.column("Total_Amount",width=100)
       


        self.fatch_data()
        self.movie_table.bind("<ButtonRelease-1>",self.get_cursor)

    
    def add_data(self):
        myconn=mysql.connector.connect(host= "localhost",username= "root",password= "root",database= "movie")
        my_cursor=myconn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.Name_var.get(),
                                                                                    self.Contact_no_var.get(),
                                                                                    self.No_of_seats_var.get(),
                                                                                    self.Print_var.get(),
                                                                                    self.Date_var.get(),
                                                                                    self.Time_var.get(),
                                                                                    self.Location_var.get(),
                                                                                    self.Movie_name_var.get(),
                                                                                    self.Duration_var.get(),
                                                                                    self.Price_var.get(),
                                                                                    self.Total_Amount_var.get()
                                                                                    
        ))
        
        myconn.commit()
        self.fatch_data()
        myconn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")

    def update(self):
        myconn=mysql.connector.connect(host= "localhost",username= "root",password= "root",database= "movie")
        my_cursor=myconn.cursor()
        my_cursor.execute("update Movie set Name=%s,Contact_no=%s,No_of_seats=%s,Print=%s,Date=%s,Time=%s,Location=%s,Movie_name=%s,Duration=%s,Price=%s,Total_Amount=%s",(
                                                                                  
                                                                                    self.Name_var.get(),
                                                                                    self.Contact_no_var.get(),
                                                                                    self.No_of_seats_var.get(),
                                                                                    self.Print_var.get(),
                                                                                    self.Date_var.get(),
                                                                                    self.Time_var.get(),
                                                                                    self.Location_var.get(),
                                                                                    self.Movie_name_var.get(),
                                                                                    self.Duration_var.get(),
                                                                                    self.Price_var.get(),
                                                                                    self.Total_Amount_var.get()
        ))

        myconn.commit()
        self.fatch_data()
        self.reset()
        myconn.close()

        messagebox.showinfo("Success","Member has been updated successfully")

        
    def fatch_data(self):
        myconn=mysql.connector.Connect(host= "localhost",username= "root", password="root", database="movie")
        my_cursor=myconn.cursor()
        my_cursor.execute("select * from movie")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.movie_table.delete(*self.movie_table.get_children())
            for i in rows:
                self.movie_table.insert("",END,values=i)
            myconn.commit()
        myconn.close()

    def get_cursor(self,event=""):
        cursor_row=self.movie_table.focus()
        content=self.movie_table.item(cursor_row)
        row=content['values']

        self.Name.set(row[0]),
        self.Contact_no.set(row[1]),
        self.No_of_seats.set(row[2]),
        self.Print.set(row[3]),
        self.Date.set(row[4]),
        self.Time.set(row[5]),
        self.Location.set(row[6]),
        self.Movie_name.set(row[7]),
        self.Duration.set(row[8]),
        self.Price.set(row[9]),
        self.Total_Amount.set(row[10])

    def show_data(self):
        self.txtBox.insert(END,"Name\t\t"+self.Name_var.get() + "\n")
        self.txtBox.insert(END,"Contact_No\t\t"+self.Contact_No_var.get() + "\n")
        self.txtBox.insert(END,"No_Of_Seats\t\t"+self.No_Of_Seats_var.get() + "\n")
        self.txtBox.insert(END,"Print\t\t"+self.Print_var.get() + "\n")
        self.txtBox.insert(END,"Date\t\t"+self.Date_var.get() + "\n")
        self.txtBox.insert(END,"Time\t\t"+self.Time_var.get() + "\n")
        self.txtBox.insert(END,"Location\t\t"+self.Location_var.get() + "\n")
        self.txtBox.insert(END,"Movie_name\t\t"+self.Movie_name_var.get() + "\n")
        self.txtBox.insert(END,"Duration\t\t"+self.Duration_var.get() + "\n")
        self.txtBox.insert(END,"Price\t\t"+self.Price.get() + "\n")
        self.txtBox.insert(END,"Total_Amonut\t\t"+self.Total_Amonut_var.get() + "\n")

    def reset(self):
        self.Name.set(""),
        self.Contact_no.set(""),
        self.No_of_seats.set(""),
        self.Print.set(""),
        self.Date.set(""),
        self.Time.set(""),
        self.Location.set(""),
        self.Movie_name.set(""),
        self.Duration.set(""),
        self.Price.set(""),
        self.Total_Amount.set(""),
    def iExit(self):
        iExit= tkinter.messagebox.askyesno("Movie Booking system","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return 


    
   # def delete(self):
       # if self.prn_var.get()==" " or self.id_var.get()==" ":
      #      messagebox.showerror("Error","First select the member")
    #    else:
     #       myconn=mysql.connector.connect(host="localhost",username="root",password="root",database="movie")
      #      my_cursor=myconn.cursor()
       #     query="delete from library where PRN_NO=%s"
        #    value=(self.prn_var.get(),)
         #   my_cursor.execute(query,value)
          #  myconn.commit()
           # self.fatch_data()
            #self.reset()
            #myconn.close()

            #messagebox.showinfo("Success","Member has been deleted successfully")







                                                                                    

 
if __name__ == "__main__":
    root=Tk()
    obj=MovieBookingSystem(root)
    root.mainloop()
