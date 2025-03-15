import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from fpdf import FPDF
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime
from tkinter import messagebox

class PayrollSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1550x800+0+0")

        # Connect to the database
        self.connect_database()
        # Employee Details Section
        lbl_title =tk.Label(self.root, text='EMPLOYEE  PAYROLL ', font=('times new roman', 37, 'bold'), fg='darkblue', bg='white')
        lbl_title.place(x=0, y=0, width=1366, height=50)

        self.frame_employee = tk.LabelFrame(root, text="Employee Details", padx=10, pady=10,fg="red", font=("arial", 12, "bold"))
        self.frame_employee.place(x=10, y=60, width=700, height=260)

        self.labels = ["Employee ID", "Department", "Designation", "Name", "Email", "D.O.B", "D.O.J",
                       "Address", "Gender", "Phone", "City", "Basic Salary"]
        self.entries = {}
        row = 0
        c=0
        for label in self.labels:
            tk.Label(self.frame_employee, text=label, font=("arial", 12, "bold")).grid(row=row, column=c+1, sticky="w", pady=5,padx=10)
            entry = tk.Entry(self.frame_employee, width=20, font=("arial", 12, "bold"))
            
            entry.grid(row=row, column=c+2)
            self.entries[label] = entry
            if row==5:
                row=0
                c+=2
            else:
                row += 1
        
        # Employee Salary Section
        self.frame_salary = tk.LabelFrame(root, text="Employee Salary Details", padx=10, pady=10,fg="red", font=("arial", 12, "bold"))
        self.frame_salary.place(x=10, y=330, width=700, height=200)

        self.salary_labels = ["Month                ", "Year", "Total Days", "Absents", "  ESI                  ", "  DA", "  PF", "  Net Salary"]
        self.salary_entries = {}
        self.frame_btn2 = tk.LabelFrame(root, padx=10, pady=10,fg="red", font=("arial", 12, "bold"))
        self.frame_btn2.place(x=10, y=540, width=700, height=150)
        row2 = 0
        for label in self.salary_labels:
            tk.Label(self.frame_salary, text=label, font=("arial", 12, "bold")).grid(row=row2, column=c+1, sticky="w", pady=5)
            entry = tk.Entry(self.frame_salary, width=20, font=("arial", 12, "bold"))
            entry.grid(row=row2, column=c+2,padx=5)
            self.salary_entries[label] = entry
            if row2==3:
                row2=0
                c+=2
            else:
                row2 += 1

        # Buttons
        tk.Button(self.frame_btn2, text="Calculate",command=self.calculate_salary,width=21,height=2,bg="blue",fg="white", font=("arial", 12, "bold")).grid(row=1,column=2)
        tk.Button(self.frame_btn2, text="Save", command=self.save_data,width=22,height=2,bg="blue",fg="white", font=("arial", 12, "bold")).grid(row=1, column=1)
        tk.Button(self.frame_btn2, text="Clear", command=self.clear_fields,width=21,height=2,bg="blue",fg="white",font=("arial", 12, "bold")).grid(row=2, column=0)
        tk.Button(self.frame_btn2, text="View", command=self.view_data,width=21,height=2,bg="blue",fg="white", font=("arial", 12, "bold")).grid(row=1, column=0)
        tk.Button(self.frame_btn2, text="Update", command=self.update_data,width=22,height=2,background="blue",fg="white", font=("arial", 12, "bold")).grid(row=2, column=1)
        tk.Button(self.frame_btn2, text="Delete", command=self.delete_data,width=21,height=2,bg="blue",fg="white", font=("arial", 12, "bold")).grid(row=2, column=2)

        # Salary Receipt Section
        self.frame_receipt = tk.LabelFrame(root, text="Salary Receipt", padx=10, pady=10,fg="red", font=("arial", 12, "bold"))
        self.frame_receipt.place(x=720, y=60, width=620, height=620)

        self.receipt_text = tk.Text(self.frame_receipt, width=110, height=100, font=("arial", 15, "bold"))
        self.receipt_text.pack()

       
       

        tk.Button(self.root, text="Generate Receipt", command=self.generate_salary_receipt,width=20,height=2,bg="blue",fg="white", font=("arial", 12, "bold")).place(x=1100,y=600)
    def on_click(self,event):
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = eval(self.screen.get())
                self.screen.delete(0, tk.END)
                self.screen.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input!",parent=self.root)
        elif text == "C":
            self.screen.delete(0, tk.END)
        else:
            self.screen.insert(tk.END, text)

    def connect_database(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Oracle_Mysql",  # Replace with your MySQL password
                database="mydata"
            )
            self.cursor = self.db.cursor()
        except Exception as e:
            messagebox.showerror("Database Connection Error", f"Error connecting to database: {e}",parent=self.root)

    def calculate_salary(self):
        try:
            self.receipt_text.config(state="normal")

            salary = float(self.entries["Basic Salary"].get())
            absents = int(self.salary_entries["Absents"].get())
            total_days = int(self.salary_entries["Total Days"].get())
            present_days = total_days - absents

        # If absent for all days, net salary is zero
            if absents == total_days:
                da = 0
                pf = 0
                esi = 0
                net_salary = 0
            else:
            # Automated calculations
                da = 0.50 * salary   # 50% of Basic Salary
                pf = 0.12 * salary   # 12% of Basic Salary
                esi = 0.0075 * salary  # 0.75% of Basic Salary

            # Calculate Net Salary
                net_salary = (((((salary / total_days) * present_days) + da) - esi) - pf)
        
        # Update the UI with calculated values
            self.salary_entries["  DA"].delete(0, tk.END)
            self.salary_entries["  DA"].insert(0, f"{da:.2f}")
            self.salary_entries["  PF"].delete(0, tk.END)
            self.salary_entries["  PF"].insert(0, f"{pf:.2f}")
            self.salary_entries["  ESI                  "].delete(0, tk.END)
            self.salary_entries["  ESI                  "].insert(0, f"{esi:.2f}")
            self.salary_entries["  Net Salary"].delete(0, tk.END)
            self.salary_entries["  Net Salary"].insert(0, f"{net_salary:.2f}")

        # Generating salary receipt
            self.receipt_text.delete(1.0, tk.END)
            self.receipt_text.insert(tk.END, f"Employee Name: {self.entries['Name'].get()}\n")
            self.receipt_text.insert(tk.END, f"Employee ID: {self.entries['Employee ID'].get()}\n")
            self.receipt_text.insert(tk.END, f"Department: {self.entries['Department'].get()}\n")
            self.receipt_text.insert(tk.END, f"Designation: {self.entries['Designation'].get()}\n")
            self.receipt_text.insert(tk.END, f"Month: {self.salary_entries['Month                '].get()}\n")
            self.receipt_text.insert(tk.END, f"Year: {self.salary_entries['Year'].get()}\n")
            self.receipt_text.insert(tk.END, f"Total Days: {total_days}\n")
            self.receipt_text.insert(tk.END, f"Absents: {absents}\n")
            self.receipt_text.insert(tk.END, f"DA (50%): {da:.2f}\n")
            self.receipt_text.insert(tk.END, f"PF Deduction (12%): {pf:.2f}\n")
            self.receipt_text.insert(tk.END, f"ESI (0.75%): {esi:.2f}\n")
            self.receipt_text.insert(tk.END, f"Net Salary: {net_salary:.2f}\n")

            self.receipt_text.config(state="disabled")

        except Exception as e:
            messagebox.showerror("Error", "Please enter valid input", parent=self.root)


    def save_data(self):
        try:
            # Get Employee Details
            employee_id = self.entries["Employee ID"].get()
            salary_data = {key: entry.get() for key, entry in self.salary_entries.items()}

            # Save Salary Details
            self.cursor.execute(
                "INSERT INTO payroll (Employee_Id, month, year, total_days, absents, medical, convence, pf, net_salary) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    employee_id, salary_data["Month                "], salary_data["Year"], salary_data["Total Days"],
                    salary_data["Absents"], salary_data["  ESI                  "], salary_data["  DA"],
                    salary_data["  PF"], salary_data["  Net Salary"]
                )
            )
            self.db.commit()
            messagebox.showinfo("Success", "Payroll data saved successfully!",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Please Enter Valid Input",parent=self.root)

    def view_data(self):
        try:
            self.receipt_text.config(state="normal")
            employee_id = self.entries["Employee ID"].get()

        # Fetching both employee and payroll data
            self.cursor.execute("SELECT Employee_Id, Name, Department, Designition, Email, dob, doj, phone, address,gender,city,salary FROM employee1 WHERE Employee_Id = %s", (employee_id,))
            employee_result = self.cursor.fetchone()

            self.cursor.execute("SELECT Month, Year, Total_Days, Absents, medical, Convence, pf, Net_Salary FROM payroll WHERE Employee_Id = %s", (employee_id,))
            payroll_result = self.cursor.fetchone()

            if employee_result and payroll_result:
            # Fill in the Employee Details
                employee_fields = [
                "Employee ID", "Name", "Department", "Designation", "Email", "D.O.B", "D.O.J",
                "Phone","Address","Gender","City","Basic Salary"
            ]

            # Mapping employee data
                employee_data = dict(zip(employee_fields, employee_result))
                for label, value in employee_data.items():
                    self.entries[label].delete(0, tk.END)
                    self.entries[label].insert(0, value)

            # Fill in the Payroll Details
                payroll_fields = [
                "Month                ", "Year", "Total Days", "Absents","  ESI                  ", "  DA", "  PF", "  Net Salary"
            ]
                payroll_data = dict(zip(payroll_fields, payroll_result))

                for label, value in payroll_data.items():
                    self.salary_entries[label].delete(0, tk.END)
                    self.salary_entries[label].insert(0, value)

            # Update the receipt with both Employee and Payroll details
                self.receipt_text.delete(1.0, tk.END)
                self.receipt_text.insert(tk.END, f"Employee Name: {self.entries['Name'].get()}\n")
                self.receipt_text.insert(tk.END, f"Employee ID: {self.entries['Employee ID'].get()}\n")
                self.receipt_text.insert(tk.END, f"Department: {self.entries['Department'].get()}\n")
                self.receipt_text.insert(tk.END, f"Designation: {self.entries['Designation'].get()}\n")
                self.receipt_text.insert(tk.END, f"Basic Salary: {self.entries['Basic Salary'].get()}\n")
                self.receipt_text.insert(tk.END, f"Month: {self.salary_entries['Month                '].get()}\n")
                self.receipt_text.insert(tk.END, f"Year: {self.salary_entries['Year'].get()}\n")
                self.receipt_text.insert(tk.END, f"Total Days: {self.salary_entries['Total Days'].get()}\n")
                self.receipt_text.insert(tk.END, f"Absents: {self.salary_entries['Absents'].get()}\n")
                self.receipt_text.insert(tk.END, f"ESI: {self.salary_entries['  ESI                  '].get()}\n")
                self.receipt_text.insert(tk.END, f"DA: {self.salary_entries['  DA'].get()}\n")
                self.receipt_text.insert(tk.END, f"PF: {self.salary_entries['  PF'].get()}\n")
                self.receipt_text.insert(tk.END, f"Net Salary: {self.salary_entries['  Net Salary'].get()}\n")
                self.receipt_text.config(state="disabled")
                messagebox.showinfo("Success", f"Employee and payroll details for Employee ID {employee_id} loaded successfully!",parent=self.root)
            elif employee_result:
                # Fill in the Employee Details
                employee_fields = [
                "Employee ID", "Name", "Department", "Designation", "Email", "D.O.B", "D.O.J",
                "Phone","Address","Gender","City","Basic Salary"
            ]

            # Mapping employee data
                employee_data = dict(zip(employee_fields, employee_result))
                for label, value in employee_data.items():
                    self.entries[label].delete(0, tk.END)
                    self.entries[label].insert(0, value)
                self.receipt_text.config(state="disabled")
                
            else:
                messagebox.showinfo("Error", " Please Enter valid Input",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Please Enter valid Input{e}",parent=self.root)

    def update_data(self):
        if self.entries["Employee ID"].get()=="":
            messagebox.showerror("Error", f"Enter employee id",parent=self.root)

        else:

            try:
                employee_id = self.entries["Employee ID"].get()
                salary_data = {key: entry.get() for key, entry in self.salary_entries.items()}

                self.cursor.execute(
                "UPDATE payroll SET month=%s, year=%s, total_days=%s, absents=%s, medical=%s, convence=%s, pf=%s, net_salary=%s "
                "WHERE Employee_Id=%s",
                (
                    salary_data["Month                "], salary_data["Year"], salary_data["Total Days"], salary_data["Absents"],
                    salary_data["  ESI                  "], salary_data["  DA"], salary_data["  PF"], salary_data["  Net Salary"],
                    employee_id
                )
            )
                self.db.commit()
                messagebox.showinfo("Success", "Payroll data updated successfully!",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Please Enter valid Input",parent=self.root)

    def delete_data(self):
        if self.entries["Employee ID"].get()=="":
            messagebox.showerror("Error", f"Enter employee id",parent=self.root)

        else:
            try:
                employee_id = self.entries["Employee ID"].get()
                self.cursor.execute("DELETE FROM payroll WHERE Employee_Id = %s", (employee_id,))
                self.db.commit()
                messagebox.showinfo("Success", f"Payroll data for Employee ID {employee_id} deleted successfully!",parent=self.root)
                self.clear_fields()
            except Exception as e:
                messagebox.showerror("Error", f"Please Enter valid Input",parent=self.root)

    def clear_fields(self):
        self.receipt_text.config(state="normal")
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        for entry in self.salary_entries.values():
            entry.delete(0, tk.END)
        self.receipt_text.delete(1.0, tk.END)
    

    def generate_salary_receipt(self):
        if self.entries["Employee ID"].get()=="":
            messagebox.showerror("Error", f"Please Enter valid Input",parent=self.root)

        else:
            try:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_auto_page_break(auto=True, margin=15)
        # Add Receipt Header
                pdf.set_font("Arial", size=16, style="B")
                pdf.cell(0, 10, "Employee Salary Receipt", ln=True, align="C")
                pdf.ln(10)  # Add extra spacing below the header
        # Draw Employee Details Box
                pdf.set_font("Arial", size=12, style="B")
                pdf.set_fill_color(240, 240, 240)  # Light gray fill
                pdf.cell(190, 10, "Employee Details", ln=True, align="L", fill=True, border=1)
        # Employee Details Content
                pdf.set_font("Arial", size=12)
                pdf.cell(50, 10, "Name:", border=1, align="L")
                pdf.cell(140, 10, self.entries['Name'].get(), border=1, ln=True, align="L")
                pdf.cell(50, 10, "Employee ID:", border=1, align="L")
                employee_id = self.entries['Employee ID'].get()
                pdf.cell(140, 10, employee_id, border=1, ln=True, align="L")
                pdf.cell(50, 10, "Department:", border=1, align="L")
                pdf.cell(140, 10, self.entries['Department'].get(), border=1, ln=True, align="L")
                pdf.cell(50, 10, "Designation:", border=1, align="L")
                pdf.cell(140, 10, self.entries['Designation'].get(), border=1, ln=True, align="L")
                pdf.cell(50, 10, "Basic Salary:", border=1, align="L")
                pdf.cell(140, 10, self.entries['Basic Salary'].get(), border=1, ln=True, align="L")
                pdf.ln(5)  # Add spacing after Employee Details section

        # Draw Salary Details Box
                pdf.set_font("Arial", size=12, style="B")
                pdf.set_fill_color(240, 240, 240)  # Light gray fill
                pdf.cell(190, 10, "Salary Details", ln=True, align="L", fill=True, border=1)

        # Salary Details Content
                pdf.set_font("Arial", size=12)
                pdf.cell(50, 10, "Month:", border=1, align="L")
                pdf.cell(140, 10, self.salary_entries['Month                '].get(), border=1, ln=True, align="L")
                pdf.cell(50, 10, "Year:", border=1, align="L")
                pdf.cell(140, 10, self.salary_entries['Year'].get(), border=1, ln=True, align="L")
                pdf.cell(50, 10, "Total Days:", border=1, align="L")
                pdf.cell(140, 10, self.salary_entries['Total Days'].get(), border=1, ln=True, align="L")
                pdf.cell(50, 10, "Absents:", border=1, align="L")
                pdf.cell(140, 10, self.salary_entries['Absents'].get(), border=1, ln=True, align="L")
                pdf.cell(50, 10, "ESI:", border=1, align="L")
                pdf.cell(140, 10, self.salary_entries['  ESI                  '].get(), border=1, ln=True, align="L")
                pdf.cell(50, 10, "DA:", border=1, align="L")
                pdf.cell(140, 10, self.salary_entries['  DA'].get(), border=1, ln=True, align="L")
                pdf.cell(50, 10, "PF Deduction:", border=1, align="L")
                pdf.cell(140, 10, self.salary_entries['  PF'].get(), border=1, ln=True, align="L")
                pdf.cell(50, 10, "Net Salary:", border=1, align="L")
                pdf.cell(140, 10, self.salary_entries['  Net Salary'].get(), border=1, ln=True, align="L")
                pdf.ln(10)  # Add spacing after Salary Details section
        # Footer
                pdf.set_font("Arial", size=10, style="I")
                pdf.cell(0, 10, "This is a system-generated document. No signature required.", ln=True, align="C")
        # Generate unique file name
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                file_name = f"salary_receipt_{employee_id}_{timestamp}.pdf"
        # Save the PDF
                save_path = fr"D:\project\ems\Receipt\{file_name}"
                pdf.output(save_path)
                messagebox.showinfo("Success", f"Salary receipt generated successfully!\nSaved as: {file_name}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Please Enter valid Input{e}",parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = PayrollSystem(root)
    root.mainloop()
