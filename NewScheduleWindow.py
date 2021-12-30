from tkinter import *
from tkinter import ttk

import NewDay


# Class of the "new schedule" window that is created when a user presses the "add schedule" button from the main GUI
class NewScheduleWindow(Toplevel):
    # Constructor method creates the frame and GUI of the new window as well as initializes all the necessary variables
    def __init__(self, sched_list, master=None):
        super().__init__(master=master)
        self.title("Add New Schedule")

        self.newframe = ttk.Frame(self, padding="3 3 12 12")
        self.newframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.schedule_name = StringVar()  # Variable that holds the schedule name
        self.final_schedule = {}  # Dictionary that holds the final schedule containing all days and all tasks
        self.full_schedule = []  # List that holds each day-schedule and its task
        self.day_column = 0  # Variable used for grid positioning for the GUI

        ttk.Label(self.newframe, text="Schedule Name").grid(column=0, row=0, sticky=W)
        ttk.Entry(self.newframe, width=10, textvariable=self.schedule_name).grid(column=1, row=0, sticky=W)

        self.add_day()  # We add the first day because a schedule has to have at least one day (in this case Monday)

        ttk.Button(self.newframe, text="Add Day", command=self.add_day, width=7).grid(column=3, row=0, sticky=W)
        ttk.Button(self.newframe, text="Save", command=lambda: self.add_schedule(sched_list), width=7).grid(column=4, row=0, sticky=W)

        for child in self.newframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    # This method is triggered when the user presses the "Add Day" Button
    # It adds a new day object to the schedule list as well as adds a new day column in the GUI
    def add_day(self):
        self.full_schedule.append(NewDay.NewDay(self.newframe, self.day_column))
        self.day_column += 3

    # This method is triggered when the user presses the "Save" button
    # It adds the new schedule's name on the "schedule_names.txt" file, goes over the schedule list and adds all days
    # and tasks to the schedule dictionary and saves the dictionary on a file.
    def add_schedule(self, sched_list):
        name_file = open("Schedules/schedule_names.txt", "a")
        name_file.write(self.schedule_name.get() + "\n")
        name_file.close()
        names = open("Schedules/schedule_names.txt", "r")
        sched_list.set(names.read().splitlines())
        names.close()

        for day_schedule in self.full_schedule:
            schedule_tasks = {}
            for task in day_schedule.schedule:
                schedule_tasks[task.task_name.get()] = (task.task_start.get(), task.task_end.get())
            self.final_schedule[day_schedule.day_of_week] = schedule_tasks

        file = open("Schedules/"+self.schedule_name.get()+".txt", "w")
        file.write(repr(self.final_schedule))
        file.close()

        self.destroy()
