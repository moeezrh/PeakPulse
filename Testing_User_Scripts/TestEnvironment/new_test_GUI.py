import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import subprocess


#Using subprocess.run instead makes the page open once the process is finished
def run_mpu6050():
    subprocess.run(["python", "Testing_User_Scripts/TestEnvironment/new_test_running.py"])
    running_output_page()

def jump_mpu6050():
    subprocess.Popen(["python", "Testing_User_Scripts/TestEnvironment/new_test_running.py"])


# function to open a new window 
# on a button click
def running_output_page():
	
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(root)
    newWindow.title("Running Data Output")
    newWindow.geometry("800x800")
    newWindow.configure(bg="#212121")
    # A Label widget to show in toplevel
    running_title = tk.Label(newWindow, text="Running Data Analysis", font=TitleFont, bg="#212121", fg="white")
    running_title.pack(pady=10)

    # To show the image of plot
    pathToImage="C:/Users/moeez/Documents/repos/PeakPulse/graph.png"
    im = Image.open(pathToImage)
    ph = ImageTk.PhotoImage(im)
    running_image = tk.Label(newWindow, image=ph)
    running_image.image=ph
    running_image.pack(pady=10)

    #To show the data analysis
    with open("C:/Users/moeez/Documents/repos/PeakPulse/data.txt", 'r') as file:
        data = file.read()
    
    running_data = tk.Label(newWindow, text=data, font=TextFont, justify="left", bg="#212121", fg="white")
    running_data.pack(pady=10)



# Create the main window
root = tk.Tk()
root.title("PeakPulse")
# Set the window size to 400x300 pixels
root.geometry("400x400")  
# configures background color
root.configure(bg="#212121")

# Define a custom font
TitleFont = tkfont.Font(family="Roboto", size=20, weight="bold")
TextFont = tkfont.Font(family="Roboto", size=16, weight="normal")
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