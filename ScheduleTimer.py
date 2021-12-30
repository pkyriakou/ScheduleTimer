import ast
from tkinter import *
from tkinter import ttk
from datetime import datetime, date
import calendar

import DeleteScheduleWindow
import NewScheduleWindow


# This is the main class of the program which holds the GUI and the main functionality
class MainGUI:
    # Constructor method that creates the applications main frame / GUI and initializes variables
    def __init__(self, root):
        self.root = root
        self.root.title("Schedule Timer")

        # Here we extract the saved schedule names from their file to display in the listbox
        names = open("Schedules/schedule_names.txt", "r")
        self.SCHEDULE_NAMES = names.read().splitlines()
        self.schedule_var = Variable(value=self.SCHEDULE_NAMES)

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.timer = StringVar()
        self.current_sched_task = StringVar()

        ttk.Button(self.mainframe, text="Add Schedule", command=self.add_button_event).grid(column=0, row=0, sticky=W)
        ttk.Button(self.mainframe, text="Delete Schedule", command=self.delete_button_event).grid(column=1, row=0, sticky=E)

        ttk.Label(self.mainframe, text="Available schedules: ").grid(column=0, row=1, sticky=W)
        self.lbox = Listbox(self.mainframe, listvariable=self.schedule_var, selectmode='browse')
        self.lbox.grid(column=0, row=2, sticky=W)
        self.lbox.bind("<Double-1>", lambda e: self.begin_timing())  # exec timing function when schedule is clicked on

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    # The method below is the functionality of this small application
    # It extracts the schedule selected from the listbox and checks it against the current day of the week
    # The method checks the time of day and if a task is scheduled for that hour, the method displays the task and
    # time remaining to complete it
    def begin_timing(self):
        selected_sched = self.lbox.curselection()  # Get selected schedule from listbox

        # We use this if-statement to check whether there is actually selected schedule
        # because sometimes, double-clicking an unselected listbox item (the action which triggers this method) does not
        # immediately select that item
        if len(selected_sched) > 0:
            file = open("Schedules/" + self.schedule_var.get()[selected_sched[0]] + ".txt", "r")
            current_schedule = ast.literal_eval(file.read())  # Save the current schedule as a variable
            if calendar.day_name[date.today().weekday()] in current_schedule:
                current_day = current_schedule[calendar.day_name[date.today().weekday()]]  # Schedule's current day
            else:
                current_day = {}
        else:
            current_day = {}
            self.current_sched_task.set("No")
            self.timer.set("Schedule")

        # Here we set the label to print no task scheduled in the case that a schedule is selected but no task is
        # scheduled for this day/hour
        self.current_sched_task.set("No Task")
        self.timer.set("Scheduled")

        # Go through the items in the current day of the schedule and check whether any task is scheduled for the
        # current time of the day
        for task, time_range in current_day.items():
            start_time = datetime.strptime(time_range[0], '%H:%M').time()
            end_time = datetime.strptime(time_range[1], '%H:%M').time()

            # If a task is scheduled for the current time of the day, display the task name and the time remaining to
            # complete that task before going to the next one.
            if (start_time < datetime.now().time()) and (datetime.now().time() < end_time):
                time_diff = datetime.combine(date.min, end_time) - datetime.combine(date.min, datetime.now().time())
                secs = time_diff.total_seconds()
                hours = str(int(secs / 3600))
                minutes = str(int(secs / 60) % 60)
                self.current_sched_task.set(task)
                self.timer.set("Time Left: " + hours + ":" + minutes)

        task_widget = Label(self.mainframe, textvariable=self.current_sched_task, font=('Arial', 24))
        task_widget.grid(column=0, row=3, sticky=W)
        timing_widget = Label(self.mainframe, textvariable=self.timer, font=('Arial', 24))
        timing_widget.grid(column=0, row=4, sticky=W)
        self.root.after(10000, self.begin_timing)  # Here we tell the tkinter UI to re-run this method every 10 seconds

    # This method is triggered when the add schedule button is pressed and it creates a new "schedule" window
    def add_button_event(self):
        NewScheduleWindow.NewScheduleWindow(self.schedule_var, root)

    # This method is triggered when the delete schedule button is pressed and it creates a "delete schedule" window
    def delete_button_event(self):
        DeleteScheduleWindow.DeleteScheduleWindow(self.schedule_var, root)


root = Tk()  # TKinter root
MainGUI(root)
root.mainloop()  # start the mainloop which runs when the app is running
