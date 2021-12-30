from tkinter import *
from tkinter import ttk


# This is the new task class, which corresponds to a task in the schedule
class TaskEntry:
    def __init__(self, root, entry_row, day_column):
        self.task_name = StringVar()  # Variable that holds the task name
        self.task_start = StringVar()  # Variable that holds the time where the task is to start
        self.task_end = StringVar()  # Variable that holds the time where the task is to end
        self.task_row = entry_row  # Task row variable used for positioning the task entries within the GUI
        self.task_column = day_column  # Task column variable used for positioning the task entries within the GUI
        self.day = int(day_column/3)  # Variable that holds the day of the week as an integer (0-6)
        self.newframe = root

        ttk.Label(self.newframe, text="Task Name").grid(column=self.task_column, row=self.task_row, sticky=W)
        ttk.Entry(self.newframe, width=10, textvariable=self.task_name).grid(column=self.task_column, row=self.task_row+1, sticky=W)

        ttk.Label(self.newframe, text="Start Time").grid(column=self.task_column+1, row=self.task_row, sticky=W)
        ttk.Entry(self.newframe, width=10, textvariable=self.task_start).grid(column=self.task_column+1, row=self.task_row+1, sticky=W)

        ttk.Label(self.newframe, text="End Time").grid(column=self.task_column+2, row=self.task_row, sticky=W)
        ttk.Entry(self.newframe, width=10, textvariable=self.task_end).grid(column=self.task_column+2, row=self.task_row+1, sticky=W)

        for child in self.newframe.winfo_children():
            child.grid_configure(padx=2, pady=2)
