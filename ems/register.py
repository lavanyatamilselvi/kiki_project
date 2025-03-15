from tkinter import *
from tkinter import ttk, messagebox
import tkinter
from PIL import Image, ImageTk
import mysql.connector
    
class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("550x800+0+0")

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # =============variables ===================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ======== bg image ================
        self.bg = ImageTk.PhotoImage(file=r"images\back.webp")  # Replace with the actual path
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # =========== left image ============
        self.bg1 = ImageTk.PhotoImage(file=r"images\register.jpeg")  # Replace with the actual path
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # ======= Main frame =========================
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(
            frame,
            text="REGISTER HERE",
            font=("times new roman", 20, "bold"),
            fg="green",
            bg="white",
        )
        register_lbl.place(x=20, y=20)

    # ====================== Label entry ==============

    # ----------------------------------row1
        fname = Label(
            frame,
            text="First Name",
            font=("times new roman", 15, "bold"),
            bg="white",
        )
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(
            frame,
            text="Last Name",
            font=("times new roman", 15, "bold"),
            bg="white",
        )
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15,"bold"))
        self.txt_lname.place(x=370, y=130, width=250)

    # ------------------------------row2
        contact = Label(
            frame,
            text="Contact No",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(
            frame,
            text="Email",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

    # ---------------------------------row3
        security_Q = Label(
            frame,
            text="Select Security Questions",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(
            frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly"
        )
        self.combo_security_Q["value"] = (
            "Select",
            "Your Birth Place",
            "Your Favourite Teacher Name",
            "Your Pet Name",
        )
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(
            frame,
            text="Security Answer",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

    # -------------------------------------row4
        pswd = Label(
            frame,
            text="Password",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        pswd.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(
            frame,
            text="Confirm Password",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        confirm_pswd.place(x=370, y=310)
        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

    # ======================= check button ======================
        self.var_check = IntVar()
        checkbtn = Checkbutton(
            frame,
            variable=self.var_check,
            text="I Agree The Terms & Condition",
            font=("times new roman", 12, "bold"),
        )
        checkbtn.place(x=50, y=380)

    # ===========================buttons=========================

        register_btn=Button(frame,text="Register",command=self.register_data,font=("times new roman", 15, "bold"),bg="green",fg="black")
        register_btn.place(x=10, y=420, width=200)

        login_btn=Button(frame,text="Login",command=self.exit,font=("times new roman", 15, "bold"),bg="red",fg="black")
        login_btn.place(x=250, y=420, width=200)
    # ========================== Function Declaration ========================
    def register_data(self):
        if self.var_fname.get() == "":
            messagebox.showerror("Error", "Enter first name",parent=self.root)
        elif self.var_lname.get() == "":
            messagebox.showerror("Error", "Enter the last name",parent=self.root)
       
        elif self.var_contact.get() == "":
            messagebox.showerror("Error", "Enter the contact number",parent=self.root)
        elif self.var_email.get() == "":
            messagebox.showerror("Error", "Enter the email",parent=self.root)
        elif self.var_securityQ.get() == "":
            messagebox.showerror("Error", "Select security question",parent=self.root)
        elif self.var_securityA.get() == "":
            messagebox.showerror("Error", "Enter security answer",parent=self.root)
        elif self.var_pass.get() == "":
            messagebox.showerror("Error", "Enter password",parent=self.root)
        elif self.var_confpass.get() == "":
            messagebox.showerror("Error", "Enter confirm password",parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm password must be the same!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="Oracle_Mysql", database="mydata"
                )
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email",parent=self.root)
                else:
                    my_cursor.execute(
                        "INSERT INTO register VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_securityQ.get(),
                            self.var_securityA.get(),
                            self.var_pass.get(),
                        ),
                    )
                    conn.commit()
                    messagebox.showinfo("Success", "Register Successfully")
                conn.close()

            except mysql.connector.errors.IntegrityError as h:
                messagebox.showerror("Error", "Mobile number already exist",parent=self.root)


            except  mysql.connector.errors.DatabaseError as e:
                 conn = mysql.connector.connect(host="localhost", user="root", password="Oracle_Mysql", database="mydata")
                 my_cursor = conn.cursor()
                 query = "select * from register where email=%s"
                 value = (self.var_email.get(),)
                 my_cursor.execute(query, value)
                 row = my_cursor.fetchone()
            # print(row)

                 if row is None:
                   messagebox.showerror("Error", "Email already exist")
                 else:
                    conn.close()
                    messagebox.showerror("Error", "Enter valid mobile number",parent=self.root)
          
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}",parent=self.root)
    def exit(self):
        self.root.destroy()
                
if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
