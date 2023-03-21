# To-do-list
A simple To-do list 

This code is a Python script that creates a graphical user interface (GUI) to manage a to-do list using the Tkinter library.

The script defines several functions to add, remove, and toggle the completion status of tasks, as well as to load and save the tasks to a JSON file.

The script then creates the main window and various widgets to interact with the to-do list.

The add_task() function adds a new task to the tasks list when the user clicks the "Add Task" button. The remove_task() function removes a selected task from the tasks list when the user clicks the "Remove Task" button after confirming the deletion. The toggle_completed() function toggles the completion status of a selected task when the user double-clicks on the task in the listbox. The update_listbox() function updates the listbox widget to display the current tasks in the tasks list. The save_tasks() and load_tasks() functions respectively save and load the tasks to and from a JSON file named "tasks.json".

The main window is created using the Tk() function and given a title "To-Do List". The task_entry widget is an entry box where the user can enter a new task. The add_button widget is a button that triggers the add_task() function when clicked. The listbox widget is a box that displays the current tasks in the tasks list. The remove_button widget is a button that triggers the remove_task() function when clicked. The save_button widget is a button that triggers the save_tasks() function when clicked. The load_tasks() function is called to load the tasks from the "tasks.json" file when the script is run. Finally, the toggle_completed() function is bound to the listbox widget using the bind() method, so that the user can toggle the completion status of a task by double-clicking on it.

The script runs the main loop using the mainloop() function, which waits for events to occur and handles them accordingly until the window is closed.
