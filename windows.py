from tkinter import ttk,Tk,dnd,Entry,Image,dialog,Frame,Label,Button,Menu,constants,Text
import requests
import sqlite3

class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x800")
        self.lbltitle = Label(text="post ")
        self.lbltitle.grid(row=2,column=3)
        self.mainmenu = Menu()
        self.config(menu=self.mainmenu)
        self.mainmenu.add_cascade(label="help",command=HelpWindow.mainloop)
        self.postxt = Text(self,width=50,height=30)
        self.postxt.grid(row=3, column=9)
        self.btnpost = ttk.Button(self,text="post",command=self.post)
        self.btnpost.grid(row=4,column=5)
    def post(self):
        self.txt = self.postxt.get("0.1")
        self.url = requests.post("https://iviv.hu/api/v1/posts",data={"body":self.txt})
        self.response = self.url.text
        print(self.response)


class HelpWindow(Tk):
    def __init__(self):
        """
        help for application
        """
        super(HelpWindow, self).__init__()
        self.title("help for desktop sid")
        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.geometry("400x200")
        self.resizable(0,0)
        self.msg = "this is a add for desktop for diaspora\n to use make usre you logged in.\n"
        self.lblhelp = Label(self,text=self.msg)
        self.lblhelp.grid(row=2,column=3,sticky=[constants.W,constants.N])

