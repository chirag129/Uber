# importing thing
from tkinter import *
from  tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

# creating register class or user interface
class Register:
    def __init__ (self,root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry('1350x700+0+0')

        self.left = ImageTk.PhotoImage (file = "back.png")
        left = Label (self.root, image = self.left).place (x = 80, y = 100, width = 400, height = 500)

        frame1 = Frame (self.root,bg = "white")
        frame1.place(x = 480, y = 100, width = 700, height = 500)

        title = Label (frame1,text = "Login Here",font = ("times ner roman",20,"bold"),bg = "white",fg = "green").place(x = 50, y = 30)

        Email = Label(frame1, text="Email", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=50, y=100)
        self.txt_Email = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_Email.place(x = 50, y = 130, width = 250)

        Password = Label(frame1, text="Password", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=50, y=170)
        self.txt_Password = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_Password.place(x=50, y=200, width=250)

        btn_login = Button(frame1, text="Login", height=2, width=20, cursor="hand2", command=self.Login).place(x=50, y=260)

        btn_register = Button(self.root, text=" Register ", height=2, width=20, cursor="hand2", command=self.op).place(x=180, y=480, width=180)

    def op(self):
        self.root.destroy()
        import main

# registring data in mysyql
    def Login(self):

        if self.txt_Email.get() == "" :
            messagebox.showerror("Error", "Pls fill your first name",parent = self.root)

        elif self.txt_Password.get() == "":
            messagebox.showerror("Error", "Pls fill your password", parent=self.root)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="uber")
                cur = con.cursor()
                cur.execute("select * from data where email = %s and password=%s",(self.txt_Email.get(),self.txt_Password.get()))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "Envalid username or password", parent=self.root)

                else:
                    messagebox.showinfo("Succes", "Login Succesful", parent=self.root)
                    self.root.destroy()
                    import map

            except  Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)

root = Tk()
obj = Register(root)
root.mainloop()