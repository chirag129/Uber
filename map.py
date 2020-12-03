# importing thing
from tkinter import *
from  tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

class Register:
    def __init__ (self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry('1350x700+0+0')

        self.left = ImageTk.PhotoImage(file="back.png")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        btn_register = Button(frame1, text="Register", height=2, width=20, cursor="hand2",command = self.page).place(x=50, y=420)

    def page(self):
        self.root.destroy()
        import ask

root = Tk()
obj = Register(root)
root.mainloop()