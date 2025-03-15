from tkinter import *
from PIL import Image, ImageTk

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")  # Full screen resolution
        self.root.title("Employee Management System")

        # Title Label
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        # Top Image
        img_top = Image.open("images/help.png") 
        img_top = img_top.resize((1366, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1366, height=720)
        dev_label = Label(f_lbl, text="Email us: helpdesk@email.com", font=("times new roman", 30, "bold"), bg="white")
        contanct_label = Label(f_lbl, text="Contact us: +91 63123 67849", font=("times new roman", 30, "bold"), bg="white")
        dev_label.place(x=500, y=300)
        contanct_label.place(x=500,y=370)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()