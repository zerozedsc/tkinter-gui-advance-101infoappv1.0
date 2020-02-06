import sqlite3
from datetime import datetime
import sqlite3dbcmdlib
from tkinter import *
import tkinter.messagebox

db = sqlite3dbcmdlib


class logWindow():
    def login_verified(self):
        print("login path")
        self.username1 = self.username_verify.get()
        self.password1 = self.password_verify.get()
        if self.username1 == '' or self.password1 == '':
            tkinter.messagebox.showinfo("null", "BLANK ENTRY DETECTED!")
            print("Null Info")
        self.username_entry1.delete(0, END)
        self.password_entry1.delete(0, END)

        self.login_test = db.db_command4(command='SELECT ALL', database_name='reg_info.db', table_name='REG_DATA',
                                    column1='ID',
                                    column2='USERNAME', column3='PASSWORD', column4='TIME',
                                    WHERESELECT='PASSWORD', WHERE='USERNAME')

        # INDEX: (-1) ID (0) Username (1) Password (2) Timestamp
        self.username_catch = self.login_test[self.login_test.index(self.username1)]  # call as 0
        self.password_catch = self.login_test[self.login_test.index(self.username1) + 1]

        self.ID_take = self.login_test[self.login_test.index(self.username1) - 1]
        self.timestamp = self.login_test[self.login_test.index(self.username1) + 2]

        try:
            if self.password1 in self.password_catch:
                tkinter.messagebox.showinfo("DONE", "LOGIN SUCCESS")
                print(f"LOGIN SUCCESS CONNECTED TO THE SERVER")
                print(f"ID: ( {self.ID_take} ) connected")
                print("")
                print(f"Registered at {self.timestamp}")
                self.screen2.destroy()
                self.screen.quit()
                self.screen.destroy()
                self.destroyLoginPath()
            else:
                tkinter.messagebox.showinfo("WRONG INPUT", "WRONG PASSWORD OR USERNAME")
                print("Wrong Info")
                self.screen2.destroy()
                self.verified = False
        except:
            tkinter.messagebox.showinfo("WRONG INPUT ", "WRONG PASSWORD OR USERNAME")
            print("Wrong Info")
            self.screen2.destroy
            self.verified = False

    def goToLogin(self):
        print("login path")
        self.screen2 = Toplevel(self.screen)
        self.screen2.title("Login..")
        self.screen2.geometry(f"300x300+{self.positionRight}+200")
        Label(self.screen2, text="PLS ENTER DETAILS BELOW", bg='blue', fg='white', font=("calibri", 11)).pack()
        Label(self.screen2, text="").pack()

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        Label(self.screen2, text="USERNAME *").pack()
        self.username_entry1 = Entry(self.screen2, textvariable=self.username_verify, width=40)
        self.username_entry1.pack()
        Label(self.screen2, text="PASSWORD *").pack()
        self.password_entry1 = Entry(self.screen2, show='*', textvariable=self.password_verify, width=40)
        self.password_entry1.pack()
        Label(self.screen2, text="").pack()
        Button(self.screen2, text="Login", width=10, command=self.login_verified).pack()

    def destroyLoginPath(self):
        var = self.ID_take
        return str(var)

    def goToRegister(self):
        print("register path")
        self.screen1 = Toplevel(self.screen)
        self.screen1.title("Register")
        self.screen1.geometry(f"300x300+{self.positionRight}+{self.positionDown}")

        self.username = StringVar()
        self.password = StringVar()

        Label(self.screen1, text="PLS ENTER DETAILS BELOW", bg='red').pack()
        Label(self.screen1, text="").pack()
        Label(self.screen1, text="Username *").pack()
        self.username_entry = Entry(self.screen1, textvariable=self.username, width=40)
        self.username_entry.pack()
        Label(self.screen1, text="Password *").pack()
        self.password_entry = Entry(self.screen1, show='*', textvariable=self.password, width=40)
        self.password_entry.pack()
        Label(self.screen1, text="").pack()
        Button(self.screen1, text="Register", width=10, height=1, command=self.register_user).pack()

    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()
        timestamp = str(datetime.now())

        try:
            ID = str(db.ID())
            if username_info == '' or password_info == '':
                tkinter.messagebox.showerror("null", 'Please Put Username and password')
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
            elif username_info == password_info:
                tkinter.messagebox.showerror("password", "password can't same with username")
                self.password_entry.delete(0, END)
            elif len(password_info) < 4:
                tkinter.messagebox.showerror("password", 'Password not strong enough, Must more than 6')
                self.password_entry.delete(0, END)
            else:
                db.db_command4(command='INSERT', database_name='reg_info.db', table_name='REG_DATA', column1='ID',
                               column2='USERNAME', column3='PASSWORD', column4='TIME',
                               INSERT1=ID, INSERT2=username_info, INSERT3=password_info, INSERT4=timestamp)
                reg_success = Label(self.screen1, text="Registration Successful", fg='green',
                                    font=("Arial Narrow", 11,))
                reg_success.pack()
                print("Register success")
                tkinter.messagebox.showinfo('DONE', "Register Success")
                self.destroyRegisterPath()

        except sqlite3.Error as error:
            tkinter.messagebox.showerror(error, 'Username already exist')

    def destroyRegisterPath(self):
        print("register path end")
        self.screen1.destroy()

    def __init__(self, master):
        self.verified = False
        self.screen = master
        self.windowHeight = int(self.screen.winfo_reqheight())
        self.windowWidth = int(self.screen.winfo_reqwidth())
        self.positionRight = int(self.screen.winfo_screenwidth() / 2 - (self.windowWidth / 2))
        self.positionDown = int(self.screen.winfo_screenheight() / 2 - (self.windowHeight / 2))
        self.screen.geometry(f"300x300+{self.positionRight}+{self.positionDown}")
        self.screen.resizable(0, 0)

        self.ID_take = ""
        self.screen.title("INFO 101 ")
        Label(text="Welcome to INFO 101", bg="grey", width=300, height=5, font=("Comic Sans MS", 13)).pack()
        Label(text="").pack()
        Button(text='LOGIN', height=2, width=30, command=self.goToLogin, font=('calibri', 12, 'bold')).pack()
        Label(text="").pack()
        Button(text="REGISTER_", height=2, width=30, command=self.goToRegister, font=('calibri', 12, 'bold')).pack()




