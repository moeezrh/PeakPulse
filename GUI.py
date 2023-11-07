import tkinter as tk
import subprocess

def run_mpu6050():
    subprocess.run(["python", "mpu6050.py"])

# Create the main window
root = tk.Tk()
root.title("Welcome to PeakPulse: Choose your exercise")
root.geometry("400x300")  # Set the window size to 400x300 pixels

# Define a custom font
customFont = tkfont.Font(family="Helvetica", size=12, weight="bold")

# Create a label widget
lbl_instruction = tk.Label(root, text="Select the exercise to start:")
lbl_instruction.pack(pady=10)  # Place the label on the window

# Create buttons to run scripts
btn_script1 = tk.Button(root, text="Start Running", command=run_mpu6050)
btn_script2 = tk.Button(root, text="Start Cycling", command=run_mpu6050)  # Placeholder for cycling function

# Place the buttons on the window using pack
btn_script1.pack(pady=10)
btn_script2.pack(pady=10)

# Start the GUI event loop
root.mainloop()