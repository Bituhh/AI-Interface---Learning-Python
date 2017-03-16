import os
import datetime
import time
import winsound
import threading
from tkinter import *


#region loginWindowns

class Login:
    usr_0 = "Victor"
    passwd_0 = "usr"
    usr = usr_0
    passwd = passwd_0
    fileName = [usr, passwd]
    def __init__(self,master):

        self.passwd_Entry = self.passwordEntry.get()

        if self.usr_Entry == self.usr:
            self.unpack("username")
            self.password()
            if self.passwordEntry == self.passwd:
                print("It work's")
            else:
                self.unpack("password")
                self.unknownError("Password")
        else:
            self.unpack("username")
            self.unknownError("Username")
    def username(self, _master):
        self.usrFrame = Frame(_master, width=750, height=500).pack_propagate(False)
        self.usernameLabel = Label(self.usrFrame, text="Username:", side=LEFT)
        self.usernameEntry = Entry(self.usrFrame, side=LEFT)

    def password(self, _master):
        self.passwdFrame = Frame(_master, width=750, height=500).pack_propagate(False)
        self.passwordLabel = Label(self.usrFrame, text="Password", side=LEFT)
        self.passwordEntry = Entry(self.usrFrame, side=LEFT)

    def unknownError(self,text):
        Label(master, text=text + " Incorrect!")
    def unpack(self, item):
        if item == "username":
            self.usernameLabel.grid_forget()
            self.passwordLabel.grid_forget()
        elif item == "password":
            self.passwordLabel.grid_forget()
            self.passwordEntry.grid_forget()

rootLogin = Tk()
Login(rootLogin)
rootLogin.mainloop()

#endregion

#region interfaceWindows
# rootInterface = tk()
# print("Welcome Back, Victor.")
#
# class _runAlarm(threading.Thread):
#     def __init__(self, alarmTime):
#         threading.Thread.__init__(self)
#         self.alarmTime = alarmTime
#
#     def run(self):
#         while self.alarmTime > datetime.datetime.now():
#             time.sleep(0.5)
#         i = 0
#         while i < 3:
#             winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
#             i += 1
#         print("Alarm Stopped!\n")
#
# def options():
#     response = input("How can I help you?\n")
#     if response == "set alarm":
#         setAlarm()
#
# def setAlarm():
#     dt = datetime.datetime.now()
#     alarmResponse = input("When?\n")
#     if alarmResponse == "today":
#         errorLoop = True
#         while errorLoop:
#             hour, min = input("What time?:\n").split(":")
#             hour = int(hour)
#             min = int(min)
#
#             alarmTime = datetime.datetime(dt.year, dt.month, dt.day, hour, min, 0)
#             if alarmTime > dt:
#                 print("Alarm set to:\n", alarmTime)
#                 break
#             else:
#                 print("Alarm set in the pass, please try again!\n")
#     else:
#         print("Sorry, I don't know what \"" + alarmResponse + "\" is! Please try again.")
#         setAlarm()
#     _runAlarm(alarmTime).start()
#
#     returnResponce = input("Do you need any more help today?\n")
#     if returnResponce == "yes":
#         options()
#
# greetings = input()
# if greetings:
#     options()
# rootInterface.mainloop()
#endregion
