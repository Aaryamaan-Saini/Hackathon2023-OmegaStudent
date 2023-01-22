# This is our Hackathon Project for AutoHacks 2023!
# For this project to function, you will need to have the modules installed.

import webbrowser
import tkinter as tk
import AppOpener as ap
import datetime
import time
import threading
import requests
from plyer import notification


# Checking for Reminders Function
def remcheck():
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        data = open("reminders.txt", "r")
        dat = data.readlines()
        for n in range (len(dat)):
            beb = dat[n]
            bob = beb.strip()
            if bob.endswith(current_time):
                title = str(bob[0])
                notification.notify(title="OmegaStudent Reminder", message=title, app_icon=None, timeout=20, toast=False)
                with open("reminders.txt", "r") as f:
                    lines = f.readlines()
                with open("reminders.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != beb:
                            f.write(line)
        time.sleep(1)

def startcheck():
    bgthread = threading.Thread(target=remcheck)
    bgthread.start()

# App Page
class OmegaStudent(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry("500x500")
        self.configure(bg="#010204")
        self.title("OmegaStudent")
        self.switch_frame(HomePage)


    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

# Home Page
class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="#010204")
        tk.Label(self, text="Hello there! Welcome to OmegaStudent!", fg="#591be6", bg="#010204",
                 font=("Roboto", 50)).grid(row=0, column=0,columnspan=2)
        tk.Button(self, text="Websites", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7",
                  command=lambda: master.switch_frame(WebPage), font=("Roboto", 30), width="10", height="5").grid(row=1,column=0)
        tk.Button(self, text="Reminders", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7",
                  command=lambda: master.switch_frame(RemPage), font=("Roboto", 30), width="10", height="5").grid(row=1,column=1)
        tk.Button(self, text="Apps", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7",
                  command=lambda: master.switch_frame(OpPage), font=("Roboto", 30), width="10", height="5").grid(row=3,column=0)
        tk.Button(self, text="Timer", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7",
                  command=lambda: master.switch_frame(TimerPage), font=("Roboto", 30), width="10", height="5").grid(row=3,column=1)



# Classroom Page
class WebPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="#010204")

        title_text = tk.Label(self, text="Open Websites", fg="#591be6", bg="#010204", font=("Roboto", 50))
        title_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        text1 = tk.Label(self, text="Enter Website URL:", fg="#ce1dd2", bg="#010204", font=("Roboto", 20))
        text1.grid(row=1, column=0, padx=10, pady=10)

        self.input_box1 = tk.Entry(self)
        self.input_box1.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self, text="Add Website", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7", command=self.add_site).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self, text="Remove Website", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7", command=self.remove_site).grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self, text="Open Websites", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7", command=self.launch_sites()).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self, text="Home", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7",
                  command=lambda: master.switch_frame(HomePage), font=("Roboto", 30), width="5", height="3").grid(row=5,
                                                                                                                  column=3)
    def add_site(self):
        site = open("siteopen.txt", "a")
        data = self.input_box1.get()
        site.write(data + "\n")
        site.close()

    def remove_site(self):
        site = open("siteopen.txt", "r")
        lines = site.readlines()
        site.close()
        site = open("siteopen.txt", "w")
        for line in lines:
            if line.strip("\n") != self.input_box1.get():
                site.write(line)
        site.close()

    def launch_sites(self):
        site = open("siteopen.txt", "r")
        lines = site.readlines()
        for line in lines:
            webbrowser.open(line.strip("\n"))
        site.close()


# Reminder Page
class RemPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="#010204")
        title_text = tk.Label(self, text="Reminders", fg="#591be6", bg="#010204", font=("Roboto", 50))
        title_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        text1 = tk.Label(self, text="Name of reminder:", fg="#ce1dd2", bg="#010204", font=("Roboto", 20))
        text1.grid(row=1, column=0, padx=10, pady=10)
        self.input_box1 = tk.Entry(self)
        self.input_box1.grid(row=1, column=1, padx=10, pady=10)

        text2 = tk.Label(self, text="Time For Reminder: (HH:MM:SS), 24 Hour Time", fg="#ce1dd2", bg="#010204", font=("Roboto", 20))
        text2.grid(row=2, column=0, padx=10, pady=10)
        self.input_box2 = tk.Entry(self)
        self.input_box2.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self, text="Add Reminder", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7", command=self.addrem).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self, text="Home", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7",
                  command=lambda: master.switch_frame(HomePage), font=("Roboto", 30), width="5", height="3").grid(row=4,
                                                                                                                  column=3)

    def addrem(self):
        title = self.input_box1.get()
        time = self.input_box2.get()
        rem = open("reminders.txt", "a")
        data = str("\n"+title+","+time)
        rem.write(data)
# Opening Page
class OpPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="#010204")
        title_text = tk.Label(self, text="App Opener", fg="#591be6", bg="#010204", font=("Roboto", 50))
        title_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        text1 = tk.Label(self, text="Enter app name:", fg="#ce1dd2", bg="#010204", font=("Roboto", 20))
        text1.grid(row=1, column=0, padx=10, pady=10)
        input_box = tk.Entry(self)
        input_box.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self, text="Add App", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7", command=lambda: self.add_app(input_box.get())).grid(row=2, column=1,
                                                                                                  padx=10, pady=10)
        tk.Button(self, text="Remove App", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7", command=lambda: self.remove_app(input_box.get())).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self, text="Launch Apps", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7", command=self.launch_apps).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self, text="Home", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7", command=lambda: master.switch_frame(HomePage)).grid(row=5, column=1,
                                                                                                  padx=10, pady=10)

    def add_app(self, app_name):
        with open("appopen.txt", "a") as file:
            file.write(app_name + "\n")

    def launch_apps(self):
        with open("appopen.txt", "r") as file:
            apps = file.readlines()
            for app in apps:
                app = app.strip()
                ap.open(app)

    def remove_app(self, app_name):
        app_to_remove = app_name
        with open("appopen.txt", "r") as f:
            lines = f.readlines()
        with open("appopen.txt", "w") as f:
            for line in lines:
                if line.strip() != app_to_remove:
                    f.write(line)


# Timer Page
class TimerPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="#010204")
        self.stats = tk.StringVar()
        self.stats.set("Session Not Started")
        self.limt = 0
        self.limtxt = tk.StringVar()
        limtxtt = "Time Remaining: "+str(self.limt)+" seconds"
        self.limtxt.set(limtxtt)
        tk.Label(self, textvariable=self.stats, fg="#591be6", bg="#010204",
                 font=("Roboto", 50)).grid(row=0, column=0,columnspan=2)
        tk.Button(self, text="Home", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7",
                  command=lambda: master.switch_frame(HomePage), font=("Roboto", 30), width="5", height="3").grid(row=4,column=3)
        tk.Label(self, textvariable=self.limtxt, fg="#591be6", bg="#010204",
                 font=("Roboto", 50)).grid(row=1,column=0,columnspan=2)
        tk.Button(self, text="Start Timer", fg="#ce1dd2", bg="#410d49", activebackground="#831a93",
                  activeforeground="#e454e7",
                  command=self.start_timer, font=("Roboto", 30), width="10", height="5").grid(row=2,column=0,columnspan=2)

    def start_timer(self):
        if self.stats.get() == "Working Time":
            return False
        elif self.stats.get() == "Break Time":
            return False
        else:
            self.stats.set("Working Time")
            self.limt = 2400
            limtxtt = "Time Remaining: " + str(self.limt) + " seconds"
            self.limtxt.set(limtxtt)
            self.update()
            for x in range(self.limt+1):
                self.limt -= 1
                limtxtt = "Time Remaining: " + str(self.limt) + " seconds"
                self.limtxt.set(limtxtt)
                self.update()
                time.sleep(1)
            self.stats.set("Break Time")
            self.limt = 600
            limtxtt = "Time Remaining: " + str(self.limt) + " seconds"
            self.limtxt.set(limtxtt)
            self.update()
            for y in range(self.limt + 1):
                self.limt -= 1
                limtxtt = "Time Remaining: " + str(self.limt) + " seconds"
                self.limtxt.set(limtxtt)
                self.update()
                time.sleep(1)
            self.stats.set("Sessions Have Ended")


startcheck()
app = OmegaStudent()
app.mainloop()
