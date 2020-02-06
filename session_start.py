from tkinter import *
import sqlite3dbcmdlib
import time
import random
import sesion_log as log
import main_win as win
import admin_win as admin


class sessionStart():
    def pushStart(self):
        start_log = Tk()
        start_log.protocol("WM_DELETE_WINDOW", exit)
        self.log = log.logWindow(start_log)
        self.log.screen.mainloop()
        self.ID_GET = self.log.ID_take
        temp = open("temp", 'w+')
        temp.write(self.ID_GET)
        temp.close()
        admin = 'aDmInTesT1'
        if self.ID_GET == admin:
            adminWin()
        elif self.log.screen.destroy:
            openWin()

class adminWin():
    def __init__(self):
        start_admin = Tk()
        start_admin.protocol("WM_DELETE_WINDOW", exit)
        self.admin = admin.admin(start_admin)
        self.admin.root.mainloop()
        if self.admin.root.destroy:
            openWin()


class openWin():
    def __init__(self):
        start_win = Tk()
        start_win.protocol("WM_DELETE_WINDOW", exit)
        self.main = win.mainWIN(start_win)
        self.main.screenMain.mainloop()

        if self.main.screenMain.destroy:
            self.start = sessionStart().pushStart()

start = sessionStart().pushStart()






