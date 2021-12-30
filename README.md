# ScheduleTimer
Small program written in Python that lets the user create a weekly schedule and keeps track of the time allocated to each task in the schedule.

The GUI was created using **TKinter** while the rest of the application only needed Built-in python libraries such as **datetime**, **calendar** and **os**. 

## What does the app do and who is it for. 
The app allows the user to create a weekly schedule with as many tasks as the user wants within the 24h period of each day. 
The user selects the time that they want to start with the task and the time they want to stop. 
Multiple schedules can be created and saved and during the day the user can switch between schedules. 
The app will look at the schedule selected by the user and if a task is schedule for the current day/hour it will display the task name as well the the amount of time (hours:minutes) that the user has left to work on that task before switching to the next one.
The user is also able to delete schedules, if they are not needed. 
The app is especially useful for people that have an open schedule and have to organize their daily activities themselves (freelance professionals, individuals taking online courses, students in University with a switched classroom model, etc.)

## User Instructions
- The app can be launched through the terminal by navigating to the app directory and running the *ScheduleTimer.py*
### Adding a new Schedule
- To add a new schedule, press the *Add Schedule* button on the top-left corner of the main GUI, this should open a *New Schedule* Window
- Give your schedule a name by typing the name into the *Schedule Name* field on the top of the *New Schedule* window
- Add the day you want to add tasks for by pressing the *Add Day* button on the top of the *New Schedule* window. This should add a new column with the next day of the week (Monday is already present) (A day can have zero number of tasks, its not required to have tasks in all days)
- Add a task to a day by pressing the *Add Task* button, located next to the day you want to add tasks for. If you want to add multiple tasks, just press the button multiple times
- To save your new schedule, click on the *Save* button on the top of the *New Schedule* window. This should close the window and return you to the main GUI which now displays you new task in its listbox
### Deleting a schedule
- To delete one of your saved schedules, click on the delete schedule button on the top-right of the main GUI. This should open a new *Delete Schedule* window.
- In the *Delete Schedule* window, select the schedule you want to delete by single clicking on its name in the listbox, the press the *Delete* button on the bottom right corner of the window. This should remove the schedule from the listbox and delete it. If all schedules are delete the *Delete Schedule* window should close automatically. 
### Tracking a schedule
- To track a selected schedule just double click on its name from the listbox in the main GUI. If a task is scheduled for the current day and time the name of the task and the time remaining to work on it will be printed below the listbox. If no task is scheduled, this will be printed below until the time of a scheduled task comes.
- To switch between schedules, just double click on the schedule you want to switch from the listbox in the main GUI. 
