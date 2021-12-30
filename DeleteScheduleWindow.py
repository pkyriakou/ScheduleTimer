from tkinter import *
from tkinter import ttk
import os


# Class of the "delete schedule" window that is created when a user presses the "delete schedule" button
# from the main GUI
class DeleteScheduleWindow(Toplevel):
    # Constructor method that creates the frame and GUI of the new window
    # as well as initializes all the necessary variables
    def __init__(self, sched_list, master=None):
        super().__init__(master=master)

        self.title("Delete Schedules")

        self.newframe = ttk.Frame(self, padding="3 3 12 12")
        self.newframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # We extract all currently saved schedule's names in order to place them in the listbox for deletion
        names = open("Schedules/schedule_names.txt", "r")
        self.SCHEDULE_NAMES = names.read().splitlines()  # List of the schedules names, used for listbox
        self.schedule_var = StringVar(value=self.SCHEDULE_NAMES)
        names.close()

        ttk.Label(self.newframe, text="Current Schedules:").grid(column=0, row=0, sticky=N)
        self.listbox = Listbox(self.newframe, listvariable=self.schedule_var, selectmode='extended')
        self.listbox.grid(column=0, row=1, sticky=W)
        ttk.Button(self.newframe, text="Delete", command=lambda: self.delete_schedule(sched_list)).grid(column=2, row=3, sticky=W)

    # This method is called when the user clicks on the delete button
    # It gets the schedules that have been selected from the listbox and deletes the txt files that correspond to them
    # It additionally re-writes the "schedule_names.txt" file by exluding the deleted schedule names
    # It the re-sets the variable listed on the listbox so the listbox is updated
    def delete_schedule(self, og_list):
        for item in self.listbox.curselection():
            os.remove("Schedules/"+self.SCHEDULE_NAMES[item]+".txt")
            self.SCHEDULE_NAMES.pop(item)
        self.schedule_var.set(self.SCHEDULE_NAMES)
        og_list.set(self.SCHEDULE_NAMES)

        names = open("Schedules/schedule_names.txt", "w")
        for sched in self.SCHEDULE_NAMES:
            names.write(sched + '\n')
        names.close()

        # Close the delete schedule window automatically if no schedules exist
        if len(self.SCHEDULE_NAMES) == 0:
            self.destroy()
