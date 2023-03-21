import tkinter as tk
from tkinter import messagebox
import json

# Initialize the to-do list
tasks = []
# Define the function to add a task to the list
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append({"task": task, "completed": False})
        task_entry.delete(0, tk.END)
        update_listbox()

# Define the function to remove a task from the list
def remove_task():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        task = listbox.get(index)
        confirmed = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{task}'?")
        if confirmed:
            tasks.pop(index)
            update_listbox()

# Define the function to update the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        task_text = task["task"]
        if task["completed"]:
            task_text = "\u2713 " + task_text
        listbox.insert(tk.END, task_text)

# Define the function to save the to-do list to a file
def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

# Define the function to load the to-do list from a file
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            update_listbox()
    except FileNotFoundError:
        pass

# Define the function to toggle a task's completed status
def toggle_completed():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        tasks[index]["completed"] = not tasks[index]["completed"]
        update_listbox()

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set the background and foreground colors of the root window


# Create the task entry widget
task_entry = tk.Entry(root, width=50)
task_entry.pack()

# Create the add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Create the listbox widget
listbox = tk.Listbox(root, height=15, width=50)
listbox.pack()

# Create the remove task button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Create the save tasks button
save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack()

# Load the tasks from the file
load_tasks()

# Bind the toggle_completed function to the listbox
listbox.bind("<Double-Button-1>", lambda event: toggle_completed())

# Run the main loop
root.mainloop()
