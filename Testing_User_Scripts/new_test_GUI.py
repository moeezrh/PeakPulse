import tkinter as tk
from tkinter import font as tkfont
import subprocess


def run_mpu6050():
    subprocess.Popen(["python", "Testing_User_Scripts/test_running.py"])
    stop_button.pack(pady=20)  # Show the stop button

def jump_mpu6050():
    subprocess.Popen(["python", "Testing_User_Scripts/test_running.py"])

def stop_plotting():
    print("test")

# Create the main window
root = tk.Tk()
root.title("PeakPulse")
root.geometry("400x300")  # Set the window size to 400x300 pixels
root.configure(bg="#212121")

# Define a custom font
TitleFont = tkfont.Font(family="Roboto", size=20, weight="bold")
ButtonFont = tkfont.Font(family="Roboto", size=16, weight="normal")

# Create a label widget
lbl_instruction = tk.Label(root, text="Select Your Exercise", font=TitleFont, bg="#212121", fg="white")
lbl_instruction.pack(pady=10)  # Place the label on the window

# Create buttons to run scripts
btn_script1 = tk.Button(root, text="Running", command=run_mpu6050, font=ButtonFont, bg="#212121", fg="white")
btn_script2 = tk.Button(root, text="Jumping", command=jump_mpu6050, font=ButtonFont, bg="#212121", fg="white")  # Placeholder 
# Stop button - initially not displayed
stop_button = tk.Button(root, text="Stop Plotting", command=stop_plotting)

# Place the buttons on the window using pack
btn_script1.pack(pady=40)
btn_script2.pack(pady=10)

# Start the GUI event loop
root.mainloop()