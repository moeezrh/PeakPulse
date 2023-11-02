import tkinter as tk
import subprocess

def run_mpu6050():
    subprocess.run(["python", "mpu6050.py"])

# Create the main window
root = tk.Tk()
root.title("Welcome to PeakPulse: Choose your exercise")

# Create buttons to run scripts
btn_script1 = tk.Button(root, text="Running", command=run_mpu6050)

# Place the buttons on the window
btn_script1.pack(pady=20)

# Start the GUI event loop
root.mainloop()