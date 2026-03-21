import tkinter as tk
from tkinter import messagebox
import time

def show_message():
    time.sleep(10)  # wait 10 seconds

    root = tk.Tk()
    root.withdraw()  # hide main window
    messagebox.showwarning("Warning", "You have been hacked!")
    root.destroy()

show_message()