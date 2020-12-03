# importing thing
from tkinter import *
from  tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql


# creating register class or user interface
class Register:
    def __init__ (self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry('1350x700+0+0')

        self.left = ImageTk.PhotoImage (file = "back.png")
        left = Label (self.root, image = self.left).place (x = 80, y = 100, width = 400, height = 500)

        frame1 = Frame (self.root,bg = "white")
        frame1.place(x = 480, y = 100, width = 700, height = 500)

        title = Label (frame1,text = "Register Here",font = ("times ner roman",20,"bold"),bg = "white",fg = "green").place(x = 50, y = 30)

        name = Label(frame1, text="First Name", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=50, y=100)
        self.txt_name = Entry (frame1,font = ("times ner roman",15),bg = "lightgray")
        self.txt_name.place(x = 50, y = 130, width = 250)

        last = Label(frame1, text="Last Name", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=370, y=100)
        self.txt_last = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_last.place(x=370, y=130, width=250)

        con = Label(frame1, text="Contact No", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=50, y=170)
        self.txt_con = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_con.place(x=50, y=200, width=250)

        mail = Label(frame1, text="Email", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=370, y=170)
        self.txt_mail = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_mail.place(x=370, y=200, width=250)

        quan = Label(frame1, text="quantity", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=370, y=240)
        self.txt_quan = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_quan.place(x=370, y=270, width=250)

        truck = Label(frame1, text="truck", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=50, y=310)
        self.txt_truck = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_truck.place(x=50, y=340, width=250)

        price = Label(frame1, text="price", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=370,y=310)
        self.txt_price = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_price.place(x=370, y=340, width=250)

        btn_register = Button (frame1,text = "Register",height = 2, width = 20,cursor = "hand2",command = self.register_data).place (x = 50, y = 420)

# registring data in mysyql
    def register_data(self):
        if self.txt_name.get() == "" :
            messagebox.showerror("Error", "Pls fill your first name",parent = self.root)

        elif self.txt_last.get() == "" :
            messagebox.showerror("Error", "Pls fill your last name", parent=self.root)

        elif self.txt_con.get() == "" :
            messagebox.showerror("Error", "Pls fill your contact no ", parent=self.root)

        elif self.txt_mail.get() == "" :
            messagebox.showerror("Error", "Pls fill your email ", parent=self.root)

        elif self.txt_quan.get() == "":
            messagebox.showerror("Error", "Pls fill fill your answer", parent=self.root)

        elif self.txt_truck.get() == "":
            messagebox.showerror("Error", "Pls fill your password", parent=self.root)

        elif self.txt_price.get() == "" :
            messagebox.showerror("Error", "Pls fill your Confirm Password", parent=self.root)

        else:
            try:
                con = pymysql.connect (host = "localhost",user = "root",password = "",database = "uber")
                cur = con.cursor()
                cur.execute("select * from data where email = %s", self.txt_mail.get())
                row = cur.fetchone()

                if row!=None :
                    messagebox.showerror("Error", "User already exist try with diffrent account", parent=self.root)

                else:
                    cur.execute("insert into data (name,last,con,mail,quan,truck,price) values(%s,%s,%s,%s,%s,%s,%s)",
                                 (self.txt_name.get(),
                                  self.txt_last.get(),
                                  self.txt_con.get(),
                                  self.txt_mail.get(),
                                  self.txt_quan.get(),
                                  self.txt_truck.get(),
                                  self.txt_price.get()
                                ))

                    con.commit()
                    con.close()
                    messagebox.showerror("Error", "sended", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)} ", parent=self.root)



root = Tk()
obj = Register(root)
root.mainloop()