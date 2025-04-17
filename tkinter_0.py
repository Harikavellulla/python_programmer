import tkinter as tk
# create the main application window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("200x300")   # set window size

# Function to print "hello, world!" in the console
def say_hello():
    print("Hello, World!")
    print('good bye')
    
# create about triggers the say_hello functions
hello_button = tk.Button(root, text="Click Me",command=say_hello)
hello_button.pack(pady=20)  # pack the button into the window

# Start the Tkinter event loop
root.mainloop()