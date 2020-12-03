from tkinter import *
from  tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

def screen(root):
    root.title("Main Screen")
    root.geometry('1350x700+0+0')

def run():
    root = Tk()
    screen(root)
    root.mainloop()