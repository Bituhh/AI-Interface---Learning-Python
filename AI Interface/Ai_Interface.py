import os
import datetime
import time
import winsound
import threading
from tkinter import *


#region loginWindowns

rootLogin = Tk()
class Login:
    usr_0 = "Victor"
    passwd_0 = "usr"
    usr = usr_0
    passwd = passwd_0
    fileName = [ usr , passwd]

    usernameLabel = Label(rootLogin, text="Username:")
    usernameEntry = Entry(rootLogin)
    usr_Entry = usernameEntry.get()
    passwordLabel = Label(rootLogin, text="Password")
    passwordEntry = Entry(rootLogin)
    passwd_Entry = passwordEntry.get()

    def __init__(self):
        self.username()
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
    def username(self):
        self.usernameLabel.grid(row=0, column=0)
        self.usernameEntry.grid(row=0, column=1)
        usernameEntry = self.usernameEntry.get()

    def password(self):
        self.passwordLabel.grid(row=0)
        self.passwordEntry.grid(column=1)

    def unknownError(self,text):
        Label(rootLogin, text=text + " Incorrect!")
    def unpack(self, item):
        if item == "username":
            self.usernameLabel.grid_forget()
            self.passwordLabel.grid_forget()
        elif item == "password":
            self.passwordLabel.grid_forget()
            self.passwordEntry.grid_forget()
Login()
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
