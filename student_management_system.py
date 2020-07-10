from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class student:
    def __init__(self,root):
        self.root=root 
        self.root.title("Student Management System")
        self.root.geometry("1530x775+0+0")

        title=Label(self.root,text="Student Management System",bd=5,relief=SOLID,font=("times new roman",40,"bold"),bg="yellow",fg="black")
        title.pack(side=TOP,fill=X)

        #####variables#####
        self.Roll_No_var=StringVar()
        self.Name_var=StringVar()
        self.Email_var=StringVar()
        self.Gender_var=StringVar()
        self.Contact_var=StringVar()
        self.DOB_var=StringVar()
        self.Address_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

 #####frame-1####    
    
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=20,y=100,width=450,height=650)

        m_title=Label(Manage_Frame,text="Manage Students",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20,padx=68)
        
#####

        lbl_roll=Label(Manage_Frame,text="Roll NO.",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

#####

        lbl_name=Label(Manage_Frame,text="Name",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

##### 
    
        lbl_Email=Label(Manage_Frame,text="Email",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_Email=Entry(Manage_Frame,textvariable=self.Email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")
#####
        lbl_Gender=Label(Manage_Frame,text="Gender",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman",14,"bold"),state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        #txt_Gender=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        #txt_Gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

#####

        lbl_Contact=Label(Manage_Frame,text="Contact",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_Contact=Entry(Manage_Frame,textvariable=self.Contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

####

        lbl_DOB=Label(Manage_Frame,text="D.O.B",font=("times new roman",20,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_DOB=Entry(Manage_Frame,textvariable=self.DOB_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")


#####

        lbl_Address=Label(Manage_Frame,text="Address",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        txt_Address=Entry(Manage_Frame,textvariable=self.Address_var,width=35,bd=5,relief=GROOVE)
        txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")


#####frame-2####    
    
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="black")
        btn_Frame.place(x=5,y=500,width=430)

        Addbtn=Button(btn_Frame,text="Add",width=10,bd=4,relief=SOLID,bg="white",command=self.add_students).grid(row=2,pady=40,column=0,padx=10)
        updtebtn=Button(btn_Frame,text="Update",width=10,bd=4,relief=SOLID,bg="white",command=self.update_data).grid(row=2,pady=40,column=1,padx=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,bd=4,relief=SOLID,bg="white",command=self.delete_data).grid(row=2,pady=40,column=2,padx=10)
        clearbtn=Button(btn_Frame,text="Clear",width=10,bd=4,relief=SOLID,bg="white",command=self.Clear).grid(row=2,pady=40,column=3,padx=10)

###### frame-3 #####
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Detail_Frame.place(x=500,y=100,width=1000,height=650)

        lbl_search=Label(Detail_Frame,text="Search By",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,font=("times new roman",14,"bold"),state='readonly')
        combo_search['values']=("Rollno","Name","Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=17,bd=4,relief=SOLID,bg="white",command=self.search_data).grid(row=0,pady=40,column=3,padx=10)
        showallbtn=Button(Detail_Frame,text="Show all",width=17,bd=4,relief=SOLID,bg="white",command=self.fetch_data).grid(row=0,pady=40,column=4,padx=10)


######frame-4########
            

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="black")
        Table_Frame.place(x=10,y=100,width=970,height=520)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll",text="Roll NO.")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("DOB",text="DOB")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("Roll",width=100)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("DOB",width=100)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_students(self):
        if self.Roll_No_var.get()=="" or self.Name_var.get()=="":
            messagebox.showerror("Error","All fields are required")


        elif self.Email_var.get()=="" or self.Contact_var.get()=="":
            messagebox.showerror("Error","All fields are required")

        elif self.DOB_var.get()=="" or self.Address_var.get()=="" or self.Gender_var.get()=="":
            messagebox.showerror("Error","All fields are required")

        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                            self.Name_var.get(),
                                                                            self.Email_var.get(),
                                                                            self.Gender_var.get(),
                                                                            self.Contact_var.get(),
                                                                            self.DOB_var.get(),
                                                                            self.Address_var.get()
                                                                            ))

            con.commit()
            self.fetch_data()
            self.Clear()
            con.close()
            messagebox.showinfo("Success","Data is successfully added")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def Clear(self):
        self.Roll_No_var.set(""),
        self.Name_var.set(""),
        self.Email_var.set(""),
        self.Gender_var.set(""),
        self.Contact_var.set(""),
        self.DOB_var.set(""),
        self.Address_var.set("")

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0]),
        self.Name_var.set(row[1]),
        self.Email_var.set(row[2]),
        self.Gender_var.set(row[3]),
        self.Contact_var.set(row[4]),
        self.DOB_var.set(row[5]),
        self.Address_var.set(row[6])  


    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set Name=%s,Email=%s,Gender=%s,Contact=%s,DOB=%s,Address=%s where Rollno=%s",(
                                                                        self.Name_var.get(),
                                                                        self.Email_var.get(),
                                                                        self.Gender_var.get(),
                                                                        self.Contact_var.get(),
                                                                        self.DOB_var.get(),
                                                                        self.Address_var.get(),
                                                                        self.Roll_No_var.get()
                                                                        ))

        con.commit()
        self.fetch_data()
        self.Clear()
        con.close()                                             


    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where Rollno=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.Clear()


    def search_data(self):
        if self.search_txt.get()=="" or self.search_by.get()=="":
            messagebox.showerror("Error","Enter data you want to Search")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()

            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
            con.close()


root=Tk()
object=student(root)
root.mainloop()