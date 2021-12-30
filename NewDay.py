from tkinter import *
from tkinter import ttk

import TaskEntry


# This is the new day class, which is used to add day-schedules in an overall weekly schedule
class NewDay:
    def __init__(self, root, day_column):
        days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        self.day = int(day_column/3)  # Day of the week as an integer (0-6)
        self.day_of_week = days[self.day]  # Day of the week as a string (Monday - Sunday)
        self.column = day_column  # Column used for positioning of elements within GUI
        self.newframe = root

        self.schedule = []  # List that holds the tasks for this day
        self.task_row = 2  # Row used for positioning elements within GUI

        ttk.Label(self.newframe, text=self.day_of_week).grid(column=self.column, row=1, sticky=W)
        ttk.Button(self.newframe, text="Add Task", command=self.add_task, width=7).grid(column=self.column+1, row=1, sticky=W)

        for child in self.newframe.winfo_children():
            child.grid_configure(padx=2, pady=2)

    # This method is executed when the user presses the "add task" button
    # It creates a new task object and appends it to the day-schedule list and increments the task-row
    def add_task(self):
        new_task = TaskEntry.TaskEntry(self.newframe, self.task_row, self.column)
        self.schedule.append(new_task)
        self.task_row += 2

