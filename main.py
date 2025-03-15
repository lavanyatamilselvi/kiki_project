from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random
import time
import datetime
from system import Employee_Management_System
from register import Register

def main():
    win =Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background image
        img4 = Image.open(r"images\back.webp")
        img4 = img4.resize((1550, 738), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_lbl = Label(self.root, image=self.photoimg4)
        bg_lbl.place(x=0, y=0, width=1550, height=738)

        # Frame for login form
        frame = Frame(self.root, bg="black")
        frame.place(x=520, y=170, width=340, height=450)

        # Profile image in the frame
        img1 = Image.open(r"images\LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)  # Updated Resampling method
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_img1 = Label(frame, image=self.photoimg1, bg="black")
        lbl_img1.place(x=120, y=20, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Label
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        # Icon Images
        img2 = Image.open(r"images\LoginIconAppl.png")
        img2 = img2.resize((50, 50), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img2 = Label(frame, image=self.photoimg2, bg="black")
        lbl_img2.place(x=10, y=180, width=25, height=25)

        img3 = Image.open(r"images\lock-512.png")
        img3 = img3.resize((50, 50), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_img3 = Label(frame, image=self.photoimg3, bg="black")
        lbl_img3.place(x=10, y=250, width=25, height=25)

        # Login Button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"),
                          bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Registration button
        registerbtn = Button(frame, text="New User Register",command=self.register_window,font=("times new roman", 10, "bold"),
                             borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # Forget password button
        forgetbtn = Button(frame, text="Forget Password",command=self.forget_password_window, font=("times new roman", 10, "bold"),
                           borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetbtn.place(x=10, y=370, width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app= Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "Rohith" and self.txtpass.get() == "Vignesh":
            messagebox.showinfo("Success", "Welcome to Employee Management System")
            
            
            self.new_window = (self.root)
            self.app =Employee_Management_System(self.new_window)
            self.root=self.app

                    
            
            conn.commit()
            conn.close()
            
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Oracle_Mysql", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()))
            
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                
                
                self.new_window = (self.root)
                self.app =Employee_Management_System(self.new_window)
                self.root=self.app

                    
                
            conn.commit()
            conn.close()


#=============================Reset password====================================
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select the security question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Oracle_Mysql", database="mydata")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s and securityQ=%s and securityA=%s"
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())  # Added .get() to self.txt_security
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter correct answer", parent=self.root2)
            else:
                query = "update register set password=%s where email=%s"
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your password has been reset, please login with the new password", parent=self.root2)  # Changed messagebox.showerror to messagebox.showinfo for success message
                self.root2.destroy()

#=============================forget_password_window============================
        
    def forget_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Oracle_Mysql", database="mydata")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row is None:
                messagebox.showerror("Error", "Please enter a valid email address")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x500+610+170")
                self.root2.resizable(False, False)
                self.root2.config(bg="lightblue")

                # Title Label
                title_label = Label(
                self.root2,
                text="Forget Password",
                font=("times new roman", 20, "bold"),
                fg="white",
                bg="darkblue",
            )
                title_label.place(x=0, y=10, relwidth=1)

            # Security Question
                security_Q = Label(
                self.root2,
                text="Select Security Question",
                font=("times new roman", 15, "bold"),
                bg="lightblue",
                fg="black",
            )
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(
                self.root2, font=("times new roman", 15), state="readonly"
            )
                self.combo_security_Q["value"] = (
                "Select",
                "Your Birth Place",
                "Your Favourite Teacher Name",
                "Your Pet Name",
            )
                self.combo_security_Q.place(x=50, y=110, width=300)
                self.combo_security_Q.current(0)

                # Security Answer
                security_A = Label(
                    self.root2,
                    text="Security Answer",
                    font=("times new roman", 15, "bold"),
                    bg="lightblue",
                    fg="black",
            )
                security_A.place(x=50, y=160)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=190, width=300)

                # New Password
                new_password = Label(
                self.root2,
                text="New Password",
                font=("times new roman", 15, "bold"),
                bg="lightblue",
                fg="black",
            )
                new_password.place(x=50, y=240)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=270, width=300)

            # Reset Button
                btn = Button(
                self.root2,
                text="Reset",
                command=self.reset_pass,
                font=("times new roman", 15, "bold"),
                fg="white",
                bg="green",
                cursor="hand2",
            )
                btn.place(x=150, y=330, width=100)

if __name__ == "__main__":
    main()
