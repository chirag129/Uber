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

        f_name = Label(frame1, text="First Name", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=50, y=100)
        self.txt_fname = Entry (frame1,font = ("times ner roman",15),bg = "lightgray")
        self.txt_fname.place(x = 50, y = 130, width = 250)

        l_name = Label(frame1, text="Last Name", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        contact = Label(frame1, text="Contact No", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        Email = Label(frame1, text="Email", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=370, y=170)
        self.txt_Email = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_Email.place(x=370, y=200, width=250)

        question = Label(frame1, text="Security Question", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(frame1, font=("times ner roman", 13))
        self.cmb_quest ['values'] = ("Select" , "Your pet name", "your birth place", "Your best freind")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        Password = Label(frame1, text="Password", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=50, y=310)
        self.txt_Password = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_Password.place(x=50, y=340, width=250)

        ConfirmPassword = Label(frame1, text="ConfirmPassword", font=("times ner roman", 15, "bold"), bg="white", fg="grey").place(x=370,y=310)
        self.txt_ConfirmPassword = Entry(frame1, font=("times ner roman", 15), bg="lightgray")
        self.txt_ConfirmPassword.place(x=370, y=340, width=250)

        self.var_chk = IntVar()
        chk = Checkbutton(frame1,text = "I agree the Term and Condition",variable = self.var_chk,onvalue = 1, offvalue = 0 ,bg = "white",font = ("times new roman",12)).place (x = 50 , y = 380)

        btn_register = Button (frame1,text = "Register",height = 2, width = 20,cursor = "hand2",command = self.register_data).place (x = 50, y = 420)

        btn_login = Button(self.root, text=" Login ", height=2, width=20, cursor="hand2",command = self.data).place(x= 180, y=480, width = 180)

# clearing data
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0, END)
        self.txt_Email.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_Password.delete(0, END)
        self.cmb_quest.delete(0, END)
        self.txt_ConfirmPassword.delete(0, END)

    def data(self):
        self.root.destroy()
        import New

# registring data in mysyql
    def register_data(self):
        if self.txt_fname.get() == "" :
            messagebox.showerror("Error", "Pls fill your first name",parent = self.root)

        elif self.txt_lname.get() == "" :
            messagebox.showerror("Error", "Pls fill your last name", parent=self.root)

        elif self.txt_contact.get() == "" :
            messagebox.showerror("Error", "Pls fill your contact no ", parent=self.root)

        elif self.txt_Email.get() == "" :
            messagebox.showerror("Error", "Pls fill your email ", parent=self.root)

        elif self.cmb_quest.get() == "Select" :
            messagebox.showerror("Error", "Pls Select any question", parent=self.root)

        elif self.txt_answer.get() == "":
            messagebox.showerror("Error", "Pls fill fill your answer", parent=self.root)

        elif self.txt_Password.get() == "":
            messagebox.showerror("Error", "Pls fill your password", parent=self.root)

        elif self.txt_ConfirmPassword.get() == "" :
            messagebox.showerror("Error", "Pls fill your Confirm Password", parent=self.root)

        elif self.txt_ConfirmPassword.get()!= self.txt_Password.get():
            messagebox.showerror("Error", "Passwrd and confirm password not match", parent=self.root)

        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "please Agree our terms and condition", parent=self.root)

        else:
            try:
                con = pymysql.connect (host = "localhost",user = "root",password = "",database = "uber")
                cur = con.cursor()
                cur.execute("select * from data where email = %s", self.txt_Email.get())
                row = cur.fetchone()

                if row!=None :
                    messagebox.showerror("Error", "User already exist try with diffrent account", parent=self.root)
                    self.clear()

                else:
                    cur.execute("insert into data (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_Email.get(),
                                 self.cmb_quest.get(),
                                 self.txt_answer.get(),
                                 self.txt_Password.get()
                                ))

                    con.commit()
                    con.close()
                    messagebox.showerror("Error", "Register Sucessful", parent=self.root)
                    self.clear()
                    self.root.destroy()
                    import map

            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)} ", parent=self.root)



root = Tk()
obj = Register(root)
root.mainloop()