from tkinter import *
import random
from tkinter.ttk import *

import sqlite3dbcmdlib
import time


class admin():
    def __init__(self, master):
        self.root = master
        self.root.resizable(0, 0)
        self.windowHeight = int(self.root.winfo_reqheight())
        self.windowWidth = int(self.root.winfo_reqwidth())
        self.positionRight = int(self.root.winfo_screenwidth() / 2 - (self.windowWidth / 2))
        self.positionDown = int(self.root.winfo_screenheight() / 2 - (self.windowHeight / 2))
        self.root.geometry(f"600x400")
        self.root.title("Admin")
        style = Style()
        style.configure('Fun.TButton', font=('Arial', 8, 'normal', 'italic'), foreground='black')
        style1 = 'Fun.TButton'
        self.call = StringVar(self.root)
        self.conn = False
        # connect DB button
        self.commit = Button(self.root, text='connectDB', style=style1, command=self.connectDB)
        self.commit.place(relx=0.2, rely=0.9, anchor='e')

        # show Table
        self.show = Label(self.root, text='WAITING FOR CONNECTION', font=('Comic sans ms', 15, 'bold'),
                          background='silver', textvariable=self.call)
        self.show.place(relx=0, rely=0, height=320, width=600)
        self.show.after(1, self.showVar)

        # connect Info button
        self.connect = Button(self.root, text='ShowInfo', style=style1, state='disabled', command=self.showInfo)
        self.connect.place(relx=0.2, rely=0.9, anchor='w')

        # Exit Button
        self.exit = Button(self.root, text='Exit', style=style1, command=self.root.destroy)
        self.exit.place(relx=0.9, rely=0.9, anchor='center')

        # Edit Button
        self.edit_button = Button(self.root, text='db not connect', style=style1, command=self.edit, state='disabled')
        self.edit_button.place(relx=0.4, rely=0.9, anchor='w')

        # Delete Button
        self.del_button = Button(self.root, text='db not connect', style=style1, command=self.delete, state='disabled')
        self.del_button.place(relx=0.54, rely=0.9, anchor='w')

    def connectDB(self):
        print("DB CONNECTED")
        self.connect.config(state='enabled')
        self.edit_button.config(state='enabled', text='edit')
        self.del_button.config(state='enabled', text='delete')
        self.conn = True

    def showVar(self):
        if self.conn:
            self.call.set("database called")

        elif self.conn is not True :
            self.dot = ['Waiting for connection', 'Waiting for connection.', 'Waiting for connection..',
                        'Waiting for connection...', 'Waiting for connection....', 'Waiting for connection.....']
            self.pick = str(random.shuffle(self.dot))
            self.call.set(self.dot[0])
            self.show.after(500, self.showVar)

    def edit(self):
        print("edit press")

    def delete(self):
        print("delete press")

    def showInfo(self):
        print("Info showing..")


# tk = Tk()
# admin_call = admin(tk)
# admin_call.root.mainloop()
