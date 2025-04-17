import tkinter as tk
from tkinter import messagebox

# Create the main application window
root=tk.Tk()
root.title("Greeting App")
root.geometry("300x200")  # set the size of the window
# Function to display the greeting
def greet():
    name = name_entry.get()
    if name:
        messagebox.showinfo("Grreting",f"Hello,{name}!")
    else:
        messagebox.showwarning("Input Error","Please enter your name.")

# Create a label
name_label = tk.Label(root, text="Enter your name:")
name_label.pack(pady=10)  # padding around the widget

# create an entry box for user input
name_entry = tk.Entry(root)
name_entry.pack(pady=10)

# create  a button that trigger the greet functions
greet_button = tk.Button(root, text="Grret",command=greet)
greet_button.pack(pady=10)

# Start the tkinter event lopp
root.mainloop()