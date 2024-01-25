import tkinter as tk
from tkinter import font as tkfont
import subprocess

def run_mpu6050():
    subprocess.run(["python", "Testing_User_Scripts/test_running.py"])

def jump_mpu6050():
    subprocess.run(["python", "User_Scripts/udp_receive_jumping.py"])
    
# Create the main window
root = tk.Tk()
root.title("Welcome to PeakPulse: Choose your exercise")
root.geometry("400x300")  # Set the window size to 400x300 pixels

# Define a custom font
TitleFont = tkfont.Font(family="Helvetica", size=20, weight="bold")
ButtonFont = tkfont.Font(family="Helvetica", size=12, weight="bold")

# Create a label widget
lbl_instruction = tk.Label(root, text="Select Your Exercise:", font=TitleFont, bg="#C2BCBA", fg="white")
lbl_instruction.pack(pady=10)  # Place the label on the window

# Create buttons to run scripts
btn_script1 = tk.Button(root, text="Running", command=run_mpu6050, font=ButtonFont, bg="#9B9391", fg="white")
btn_script2 = tk.Button(root, text="Jumping", command=jump_mpu6050, font=ButtonFont, bg="#9B9391", fg="white")  # Placeholder 

# Place the buttons on the window using pack
btn_script1.pack(pady=40)
btn_script2.pack(pady=10)

# Start the GUI event loop
root.mainloop()