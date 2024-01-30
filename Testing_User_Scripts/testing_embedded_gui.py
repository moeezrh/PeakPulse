import tkinter as tk
from tkinter import font as tkfont
import subprocess

import threading
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


keep_running = True
start_time = time.time()
# This function is called periodically from FuncAnimation
def acc_animate(i, xs, ys, acc):
    current_time = float(round((time.time() - start_time), 1))
    xs.append(current_time)
    ys.append(acc[i % len(acc)])  # Cycle through the acc list

    max_time = int(max(xs)) if xs else 0
    ax.set_xticks(range(0, max_time + 1, 5))

    ax.clear()
    ax.plot(xs, ys)
    ax.set_ylim(0, 5)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Linear Acceleration over Time')
    plt.ylabel('Acceleration (g)')

def run_animation():
    global ani
    global ax
    # Initial setup
    fig, ax = plt.subplots()

    xs = []
    ys = []
    acc = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0]
    start_time = time.time()
    # Create the animation object
    ani = animation.FuncAnimation(fig, acc_animate, fargs=(xs, ys, acc), frames=len(acc), interval=100)
    # To save the animation, use ani.save() here
    plt.show()

def check_termination():
        global keep_running
        #example
        time.sleep(10)
        keep_running = False

# Start the animation in a separate thread
        

#Create a canvas


animation_thread = threading.Thread(target=run_animation)
#animation_thread.start()

# Start the termination check in the main thread
#check_termination()

# Wait for the termination condition to be met
#while keep_running:
    #time.sleep(0.1)  # Short sleep to reduce CPU usage

# After the termination condition is met, you can perform necessary cleanup
#print("Termination condition met. Exiting...")
#plt.close()
# Here you might want to close the plot or clean up resources.
# Note: closing the plot from a non-main thread might require special handling depending on the environment.


def run_mpu6050():
    animation_thread.start()
    stop_button.pack(pady=20)  # Show the stop button

def jump_mpu6050():
    subprocess.Popen(["python", "User_Scripts/udp_receive_jumping.py"])

def stop_plotting():
    print("test")

# Create the main window
root = tk.Tk()
root.title("Welcome to PeakPulse: Choose your exercise")
root.geometry("400x300")  # Set the window size to 400x300 pixels

# trying canvas
fig, ax = plt.subplots()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()


# Define a custom font
TitleFont = tkfont.Font(family="Helvetica", size=20, weight="bold")
ButtonFont = tkfont.Font(family="Helvetica", size=12, weight="bold")

# Create a label widget
lbl_instruction = tk.Label(root, text="Select Your Exercise:", font=TitleFont, bg="#C2BCBA", fg="white")
lbl_instruction.pack(pady=10)  # Place the label on the window

# Create buttons to run scripts
btn_script1 = tk.Button(root, text="Running", command=run_mpu6050, font=ButtonFont, bg="#9B9391", fg="white")
btn_script2 = tk.Button(root, text="Jumping", command=jump_mpu6050, font=ButtonFont, bg="#9B9391", fg="white")  # Placeholder 
# Stop button - initially not displayed
stop_button = tk.Button(root, text="Stop Plotting", command=stop_plotting)

# Place the buttons on the window using pack
btn_script1.pack(pady=40)
btn_script2.pack(pady=10)

# Start the GUI event loop
root.mainloop()