import tkinter as tk
from tkinter import font as tkfont
import subprocess

def run_mpu6050():
    subprocess.Popen(["python", "Testing_User_Scripts/test_running.py"])

def jump_mpu6050():
    subprocess.Popen(["python", "Testing_User_Scripts/test_running.py"])

# Create the main window
root = tk.Tk()
root.title("PeakPulse")
# Set the window size to 400x300 pixels
root.geometry("400x300")  
# configures background color
root.configure(bg="#212121")

# Define a custom font
TitleFont = tkfont.Font(family="Roboto", size=20, weight="bold")
ButtonFont = tkfont.Font(family="Roboto", size=16, weight="normal")

# Create a label widget
lbl_instruction = tk.Label(root, text="Select Your Exercise", font=TitleFont, bg="#212121", fg="white")
lbl_instruction.pack(pady=10)  # Place the label on the window

# Create buttons to run scripts
btn_running = tk.Button(root, text="Running", command=run_mpu6050, font=ButtonFont, bg="#212121", fg="white")
btn_jumping = tk.Button(root, text="Jumping", command=jump_mpu6050, font=ButtonFont, bg="#212121", fg="white")  # Placeholder 

# Place the buttons on the window using pack
btn_running.pack(pady=40)
btn_jumping.pack(pady=10)

# Start the GUI event loop
root.mainloop()