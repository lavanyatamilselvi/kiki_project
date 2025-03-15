from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter 
import os
from time import strftime
from datetime import datetime
from employee import Employee
from payroll import PayrollSystem
from help import Help

class Employee_Management_System:  
    def __init__(self, root):
       
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("EMPLOYEE MANAGEMENT SYSTEM")
        # First Image
        img1 = Image.open(r"images\f1.png")
        img1 = img1.resize((455, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=455, height=130)

        # Second Image
        img2 = Image.open(r"images\f2.png")
        img2 = img2.resize((455, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=455, y=0, width=455, height=130)

        # Third Image
        img3 = Image.open(r"images\f3.png")
        img3 = img3.resize((456, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=910, y=0, width=456, height=130)

        # Background Image
        img4 = Image.open(r"images\bg1.jpg")
        img4 = img4.resize((1366, 638), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_lbl = Label(self.root, image=self.photoimg4)
        bg_lbl.place(x=0, y=130, width=1366, height=638)

        title_lbl = Label(bg_lbl, text="EMPLOYEE  MANAGEMENT  SYSTEM", 
                          font=("times new roman", 30, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1366, height=40)

        def time():
            string=strftime('%I:%M:%S %p')
            lbl.config(text= string)
            lbl.after(1000, time)
        lbl=Label(title_lbl,font=("times new roman", 14, "bold"),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()  

        # Function for creating buttons
        def create_button(img_path, x, y, text,com):
            img = Image.open(img_path)
            img = img.resize((350, 180), Image.Resampling.LANCZOS)
            photoimg = ImageTk.PhotoImage(img)
            btn_img = Button(bg_lbl, image=photoimg, cursor="hand2",command=com)
            btn_img.place(x=x, y=y, width=350, height=180)
            btn_img.image = photoimg  # Prevent garbage collection
            btn_text = Button(bg_lbl, text=text, cursor="hand2",command=com, 
                              font=("times new roman", 14, "bold"), bg="darkblue", fg="white")
            btn_text.place(x=x, y=y+180, width=350, height=40)

        # Buttons
        create_button(r"images\emp_4.webp",190, 50, "Employee Details",self.employee_details)
        create_button(r"images\help.desk.jpg", 750, 50, "Help Desk",self.help)
        create_button(r"images\payroll.jpg", 190, 300, "PayRoll System",self.PayrollSystem_page)
        create_button(r"images\exit.jpg", 750, 300, "Exit",self.exit)


    def open_img(self):
        os.startfile("data")

# =============Function Buttons ==============
    def employee_details(self):
        self.new_window= Toplevel(self.root)
        self.app = Employee(self.new_window)

    def PayrollSystem_page(self):
        self.new_window= Toplevel(self.root)
        self.app = PayrollSystem(self.new_window)

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Employee Management","Are you sure to exit")
        if self.exit>0:
            self.root.destroy()
            
        else:
            return


    def help(self):
        self.new_window= Toplevel(self.root)
        self.app = Help(self.new_window)
    
if __name__ == "__main__":
    root = Tk()
    obj = Employee_Management_System(root)
    root.mainloop()
    
