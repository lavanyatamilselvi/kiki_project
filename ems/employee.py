from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Employee Management System")
        # Variables
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_designition = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idproofcomb =StringVar()
        self.var_idproof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()
        self.var_employee_Id = StringVar()
        self.var_city = StringVar()


        lbl_title = Label(self.root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman', 37, 'bold'), fg='darkblue', bg='white')
        lbl_title.place(x=0, y=0, width=1366, height=50)
        img_logo = Image.open(r"images\emp_1.webp")  
        img_logo = img_logo.resize((50, 50), Image.LANCZOS)  # Use LANCZOS for resizing
        self.photo_logo = ImageTk.PhotoImage(img_logo)
        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=180, y=0, width=50, height=50)
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')# Image Frame
        img_frame.place(x=0, y=50, width=1366, height=160)
        # 1st Image
        img_1 = Image.open(r"images\emp_4.webp")  
        img_1 = img_1.resize((455, 160), Image.LANCZOS)  # Use LANCZOS for resizing
        self.photo1 = ImageTk.PhotoImage(img_1)
        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=455, height=160)
        # 2nd Image
        img_2 = Image.open(r"images\emp1.jpg") 
        img_2 = img_2.resize((455, 160), Image.LANCZOS)  # Use LANCZOS for resizing
        self.photo2 = ImageTk.PhotoImage(img_2)
        self.logo = Label(img_frame, image=self.photo2)
        self.logo.place(x=455, y=0, width=455, height=160)
        # 3rd Image
        img_3 = Image.open(r"images\emp_2.jpg") 
        img_3 = img_3.resize((455, 160), Image.LANCZOS)  # Use LANCZOS for resizing
        self.photo3 = ImageTk.PhotoImage(img_3)
        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=910, y=0, width=455, height=160)
        # Main Frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=220, width=1500, height=560)
        # Upper frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information', font=('times new roman', 11, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1480, height=270)
        # Label and Entry fields
        lbl_dep = Label(upper_frame,text='Deparment:', font=('arial', 11, "bold"), bg='white')
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)
        combo_dep = ttk.Combobox(upper_frame,textvariable=self.var_dep, font=('arial', 12, 'bold'), width=17, state='readonly')
        combo_dep['value'] = ('select Department', 'Human Resources (HR)', 'Software Engineering', 'Manager','Finance',"Sales and Marketing","Data Analytics","Customer Support","Security")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        # Name
        lbl_Name = Label(upper_frame, font=("arial", 12, "bold"), text="Name:                  ", bg="white")
        lbl_Name.grid(row=0, column=2, padx=0, pady=7)
        ttk_name = ttk.Entry(upper_frame,textvariable=self.var_name,width=22, font=("arial", 11, "bold"))
        ttk_name.grid(row=0, column=3, padx=2, pady=7)
        # Designation
        lbl_designition = Label(upper_frame, font=("arial", 12, "bold"), text="Designation:", bg="white")
        lbl_designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        ttk_designation = ttk.Entry(upper_frame,textvariable=self.var_designition, width=22, font=("arial", 11, "bold"))
        ttk_designation.grid(row=1, column=1, padx=2, pady=7)
        # Email
        lbl_email = Label(upper_frame, font=("arial", 12, "bold"), text="Email:", bg="white")
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        ttk_email = ttk.Entry(upper_frame,textvariable=self.var_email ,width=22, font=("arial", 11, "bold"))
        ttk_email.grid(row=1, column=3, padx=2, pady=7)
        # Address
        lbl_employee_Id = Label(upper_frame, font=("arial", 12, "bold"), text="Employee Id:", bg="white")
        lbl_employee_Id.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        ttk_employee_Id = ttk.Entry(upper_frame,textvariable=self.var_employee_Id, width=22, font=("arial", 11, "bold"))
        ttk_employee_Id.grid(row=2, column=1, padx=2, pady=7)
        # Married
        lbl_married_status = Label(upper_frame, font=("arial", 12, "bold"), text="Marital status:", bg="white")
        lbl_married_status.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        com_txt_married = ttk.Combobox(upper_frame,textvariable=self.var_married,state="readonly",
                                       font=("arial",12,"bold"),width=18)
        com_txt_married['value'] = ("Married","Single")
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,sticky=W,padx=19,pady=7) 
        #dob
        lbl_dob = Label(upper_frame, font=("arial", 12, "bold"), text="DOB:", bg="white")
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        ttk_dob= ttk.Entry(upper_frame,textvariable=self.var_dob, width=22, font=("arial", 11, "bold"))
        ttk_dob.grid(row=3, column=1, padx=2, pady=7)
        #doj
        lbl_doj = Label(upper_frame, font=("arial", 12, "bold"), text="DOJ:", bg="white")
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7) 
        ttk_doj = ttk.Entry(upper_frame,textvariable=self.var_doj, width=22, font=("arial", 11, "bold"))
        ttk_doj.grid(row=3, column=3, padx=2, pady=7)
        #idproof
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,state="readonly",font=("arial",12,"bold"),width=22)
        com_txt_proof["value"]=("Select ID Proof","PAN CARD","ADHAR CARD","DRIVING LICENSE")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("arial", 11, "bold"))
        txt_proof.grid(row=4, column=1, padx=2, pady=7)
        #gender
        lbl_gender = Label(upper_frame, font=("arial", 12, "bold"), text="Gender:", bg="white")
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_gender["value"]=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=20,pady=7)
        #phone
        lbl_phone = Label(upper_frame, font=("arial", 12, "bold"), text="Phone:", bg="white")
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)
        ttk_phone = ttk.Entry(upper_frame,textvariable=self.var_phone, width=22, font=("arial", 11, "bold"))
        ttk_phone.grid(row=0, column=5, padx=2, pady=7)
        #country
        lbl_country = Label(upper_frame, font=("arial", 12, "bold"), text="Country:", bg="white")
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)
        ttk_country = ttk.Entry(upper_frame,textvariable=self.var_country, width=22, font=("arial", 11, "bold"))
        ttk_country.grid(row=1, column=5, padx=2, pady=7)
        #CTC
        lbl_ctc = Label(upper_frame, font=("arial", 12, "bold"), text="Salary(CTC):", bg="white")
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)
        ttk_ctc = ttk.Entry(upper_frame,textvariable=self.var_salary, width=22, font=("arial", 11, "bold"))
        ttk_ctc.grid(row=2, column=5, padx=2, pady=7)
        #Address
        lbl_address = Label(upper_frame, font=("arial", 12, "bold"), text="Address:", bg="white")
        lbl_address.grid(row=3,column=4,sticky=W,padx=2,pady=7)
        ttk_address = ttk.Entry(upper_frame,textvariable=self.var_address, width=22, font=("arial", 11, "bold"))
        ttk_address.grid(row=3, column=5, padx=2, pady=7)
        #city
        lbl_city = Label(upper_frame, font=("arial", 12, "bold"), text="City:", bg="white")
        lbl_city.grid(row=4,column=4,sticky=W,padx=2,pady=7)
        ttk_city = ttk.Entry(upper_frame,textvariable=self.var_city, width=22, font=("arial", 11, "bold"))
        ttk_city.grid(row=4, column=5, padx=2, pady=7)
        # Button Frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1050, y=10, width=280, height=210)
        btn_add = Button(button_frame,text="Save",command=self.add_data,font=("arial", 15, "bold"),width=22,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)
        btn_update = Button(button_frame,text="Update",command=self.update_data,font=("arial", 15, "bold"),width=22,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)
        btn_delete = Button(button_frame,text="Delete",command=self.delete_data,font=("arial", 15, "bold"),width=22,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)
        btn_clear = Button(button_frame,text="Clear",command=self.reset_data,font=("arial", 15, "bold"),width=22,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)
        # Down frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information Table', font=('times new roman', 11, 'bold'), fg='red')
        down_frame.place(x=10, y=280, width=1480, height=270)
        #search frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white', text='Search Employee Information', font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1470, height=60)
        search_by = Label(search_frame,font=("arial",11,"bold"),text="Search by:",fg='white',bg='red')
        search_by.grid(row=0,column=0,sticky=W,padx=5)
        #search
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",
        
                                        font=('arial',12,"bold"),width=18)

        com_txt_search['value'] = ('Select Option','Employee_Id','id_proof','Phone')
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)
        com_txt_search = ttk.Entry(search_frame,width=22,font=("arial",11,"bold"))
        com_txt_search.grid(row=0,column=2,padx=5)

        self.var_search = StringVar()
        txt_search = ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5)
        btn_search = Button(search_frame,text="Search",command=self.search_data,font=("arial",11,"bold"),width=14,bg="blue")
        btn_search.grid(row=0,column=3,padx=5)
        btn_Showall = Button(search_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),width=14,)
        btn_Showall.grid(row=0,column=4,padx=5)
        welcome =  Label(search_frame,text="WELCOME",font=("times new roman",30,"bold"))
        welcome.place(x=780,y=0,width=600,height=30)
        img_logo_mask = Image.open(r"images\emp_1.webp")
        img_logo_mask = img_logo_mask.resize((50,50),Image.Resampling.LANCZOS)
        self.phoimg_logo_mask = ImageTk.PhotoImage(img_logo_mask)
        self.logo = Label(search_frame,image=self.phoimg_logo_mask)
        self.logo.place(x=900,y=0,width=50,height=30)

       # ====================  Employee Table =================

       # Table Frame
        table_frame = Frame(down_frame, bd=2, relief=RIDGE, bg='white')
        table_frame.place(x=0, y=60, width=1330, height=100)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame,column=("dep","name","degi","email","employee_id","married","dob","doj","idproofcomb","idproof","gender","phone","country","salary","address","city"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)   
        scroll_y.pack(side=RIGHT,fill=Y)   

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Designition')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('employee_id',text='Employee Id')
        self.employee_table.heading('married',text='Married Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcomb',text='ID Type')
        self.employee_table.heading('idproof',text="ID Proof")
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('city',text='City')

        self.employee_table['show'] = 'headings'
        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("degi",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("employee_id",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproofcomb",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("city",width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
# **********************Function Declaration *********************
    def add_data(self):
    # Check for empty or invalid inputs
        if self.var_dep.get() == "select Department":
            messagebox.showerror('Error', 'Please select a valid Department.', parent=self.root)
        elif not self.var_name.get():
            messagebox.showerror("Error", "Name field cannot be empty.", parent=self.root)
        elif not self.var_phone.get().isdigit() or len(self.var_phone.get()) != 10:
            messagebox.showerror("Error", "Enter a valid 10-digit Phone number.", parent=self.root)
        elif not self.var_email.get() or "@" not in self.var_email.get() or "." not in self.var_email.get():
            messagebox.showerror("Error", "Enter a valid Email address.", parent=self.root)
        elif not self.var_employee_Id.get():
            messagebox.showerror("Error", "Employee ID field cannot be empty.", parent=self.root)
        elif not self.var_salary.get().isdigit():
            messagebox.showerror("Error", "Salary must be a valid number.", parent=self.root)
        elif not self.var_dob.get():
            messagebox.showerror("Error", "Date of Birth (YYYY-MM-DD) is required.", parent=self.root)
        elif not self.var_doj.get():
            messagebox.showerror("Error", "Date of Joining (YYYY-MM-DD) is required.", parent=self.root)
        elif not self.var_address.get():
            messagebox.showerror("Error", "Address field cannot be empty.", parent=self.root)
        elif self.var_idproofcomb.get() == "Select ID Proof":
            messagebox.showerror("Error", "Please select a valid ID Proof type.", parent=self.root)
        elif not self.var_idproof.get():
            messagebox.showerror("Error", "ID Proof field cannot be empty.", parent=self.root)
        elif not self.var_city.get():
            messagebox.showerror("Error", "City field cannot be empty.", parent=self.root)
        elif not self.var_country.get():
            messagebox.showerror("Error", "Enter the Name of Country", parent=self.root)
        elif not self.var_designition.get():
            messagebox.showerror("Error", "Designation field cannot be empty.", parent=self.root)

        else:
            try:
            # Database connection
                conn = mysql.connector.connect(host='localhost', username='root', password='Oracle_Mysql', database='mydata')
                my_cursor = conn.cursor()
            
            # Check for duplicate entries
                my_cursor.execute("SELECT * FROM employee1 WHERE email = %s OR Employee_Id = %s", 
                              (self.var_email.get(), self.var_employee_Id.get()))
                result = my_cursor.fetchone()
                if result:
                    messagebox.showerror("Error", "Employee with this Email or Employee ID already exists.", parent=self.root)
                else:
                # Insert data into the database
                    my_cursor.execute(
                    'INSERT INTO employee1 (department, name, designition, email, Employee_Id, married_status, dob, doj, id_proof_type, id_proof, gender, phone, country, salary, address, city) '
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
                        self.var_dep.get(),
                        self.var_name.get(),
                        self.var_designition.get(),
                        self.var_email.get(),
                        self.var_employee_Id.get(),
                        self.var_married.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_idproofcomb.get(),
                        self.var_idproof.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_country.get(),
                        self.var_salary.get(),
                        self.var_address.get(),
                        self.var_city.get()
                    ))
                
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo('Success', 'Employee has been added successfully!', parent=self.root)
        
            except mysql.connector.Error as db_error:
                messagebox.showerror("Database Error", f"Database error occurred: {str(db_error)}", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"An unexpected error occurred: {str(es)}", parent=self.root)
        # Fetch data
    def fetch_data(self):
        conn= mysql.connector.connect(host='localhost',username='root',password='Oracle_Mysql',database='mydata')
        my_cursor= conn.cursor()
        my_cursor.execute('select * from employee1')
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designition.set(data[2])
        self.var_email.set(data[3])
        self.var_employee_Id.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])
        self.var_address.set(data[14])
        self.var_city.set(data[15])   
   
    def update_data(self):
    # Validate mandatory fields
        if not self.var_dep.get() or self.var_dep.get() == "select Department":
            messagebox.showerror("Error", "Please select a valid Department.", parent=self.root)
        elif not self.var_name.get():
            messagebox.showerror("Error", "Name field cannot be empty.", parent=self.root)
        elif not self.var_phone.get().isdigit() or len(self.var_phone.get()) != 10:
            messagebox.showerror("Error", "Enter a valid 10-digit Phone number.", parent=self.root)
        elif not self.var_email.get() or "@" not in self.var_email.get() or "." not in self.var_email.get():
            messagebox.showerror("Error", "Enter a valid Email address.", parent=self.root)
        elif not self.var_employee_Id.get():
            messagebox.showerror("Error", "Employee ID field cannot be empty.", parent=self.root)
        elif not self.var_salary.get().isdigit():
            messagebox.showerror("Error", "Salary must be a valid number.", parent=self.root)
        elif not self.var_dob.get():
            messagebox.showerror("Error", "Date of Birth (YYYY-MM-DD) is required.", parent=self.root)
        elif not self.var_doj.get():
            messagebox.showerror("Error", "Date of Joining (YYYY-MM-DD) is required.", parent=self.root)
        elif not self.var_address.get():
            messagebox.showerror("Error", "Address field cannot be empty.", parent=self.root)
        elif self.var_idproofcomb.get() == "Select ID Proof":
            messagebox.showerror("Error", "Please select a valid ID Proof type.", parent=self.root)
        elif not self.var_idproof.get():
            messagebox.showerror("Error", "ID Proof field cannot be empty.", parent=self.root)
        elif not self.var_city.get():
            messagebox.showerror("Error", "City field cannot be empty.", parent=self.root)
        else:
            try:
            # Confirm update
                update = messagebox.askyesno("Update", "Are you sure you want to update this employee's data?", parent=self.root)
                if update:
                # Establish database connection
                    conn = mysql.connector.connect(host='localhost', username='root', password='Oracle_Mysql', database='mydata')
                    my_cursor = conn.cursor()
                
                # Check if the Employee ID exists
                    my_cursor.execute("SELECT * FROM employee1 WHERE Employee_Id = %s", (self.var_employee_Id.get(),))
                    result = my_cursor.fetchone()
                    if not result:
                        messagebox.showerror("Error", "Employee ID does not exist in the database.", parent=self.root)
                    else:
                    # Update data in the database
                        my_cursor.execute(
                        'UPDATE employee1 SET Department=%s, Name=%s, Designition=%s, Email=%s, Married_status=%s, DOB=%s, DOJ=%s, id_proof_type=%s, id_proof=%s, Gender=%s, Phone=%s, Country=%s, Salary=%s, Address=%s, City=%s '
                        'WHERE Employee_Id=%s', (
                            self.var_dep.get(),
                            self.var_name.get(),
                            self.var_designition.get(),
                            self.var_email.get(),
                            self.var_married.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_idproofcomb.get(),
                            self.var_idproof.get(),
                            self.var_gender.get(),
                            self.var_phone.get(),
                            self.var_country.get(),
                            self.var_salary.get(),
                            self.var_address.get(),
                            self.var_city.get(),
                            self.var_employee_Id.get()
                        ))
                    
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Employee data updated successfully!", parent=self.root)
                else:
                    return  # User canceled the update action

            except mysql.connector.Error as db_error:
                messagebox.showerror("Database Error", f"Database error occurred: {str(db_error)}", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"An unexpected error occurred: {str(es)}", parent=self.root)        
# Delete

    def delete_data(self):
        if self.var_idproof.get() == "":
            messagebox.showerror('Error', 'ID Proof is required to delete the record', parent=self.root)
        else:
            try:
            # Confirmation dialog
                delete = messagebox.askyesno('Delete', 'Are you sure you want to delete this employee?', parent=self.root)
                if delete:
                # Database connection and deletion
                    conn = mysql.connector.connect(host='localhost', username='root', password='Oracle_Mysql', database='mydata')
                    my_cursor = conn.cursor()
                    sql = 'DELETE FROM employee1 WHERE id_proof = %s'
                    value = (self.var_idproof.get(),)
                    my_cursor.execute(sql, value)
                    conn.commit() 
                    conn.close()
                
                # Refresh data on screen 
                    self.fetch_data()
                
                # Success message
                    messagebox.showinfo('Delete', 'Employee Successfully Deleted', parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)

    # Reset
    def reset_data(self):
        self.var_dep.set( "Select Department")
        self.var_name.set("")
        self.var_designition.set("")
        self.var_email.set("")
        self.var_employee_Id.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")
        self.var_address.set("")
        self.var_city.set("")
    # Search
    def search_data(self):
        if self.var_com_search.get() == 'Select Option' :
            messagebox.showerror('Error', 'Please select option', parent=self.root)
        elif self.var_search.get() == '':
            messagebox.showerror('Error', 'please enter the valid search data', parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Oracle_Mysql', database='mydata')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM employee1 WHERE " + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("", END, values=i)
                else:
                    messagebox.showerror('Error',"Employee not found", parent=self.root)
                conn.commit()
                conn.close()
                
            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)

    
if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()