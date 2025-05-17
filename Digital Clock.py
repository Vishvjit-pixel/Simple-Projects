"""
Setup Instructions:
1. Install a Python IDE (e.g., PyCharm, VS Code, or IDLE).
2. Ensure that the Tkinter library is available. Tkinter usually comes pre-installed with standard Python distributions.
   If not, install it using your package manager or ensure your Python installation includes it.
"""


import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.configure(bg="black")

# Create label to display time
label = tk.Label(root, font=("Arial", 60), background="black", foreground="lime")
label.pack(anchor="center", pady=20)

# Function to update time
def update_time():
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    root.after(1000, update_time)  # Update every 1000 ms (1 second)

# Start the clock
update_time()

# Run the application
root.mainloop()
