import threading
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

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
    global acc
    # Initial setup
    fig, ax = plt.subplots()
    xs = []
    ys = []
    acc = [[1, 1],
           [2, 2],
           [3, 3],
           [4, 4],
           [5, 5],
           [6, 6],
           [7, 5],
           [8, 4],
           [9, 3],
           [10, 2],
           [11, 1],
           [12, 0],
           [13, 1],
           [14, 2],
           [15, 3],
           [16, 4],
           [17, 5],
           [18, 7],
           [19, 5],
           [20, 4],
           [21, 3],
           [22, 2],
           [23, 1],
           [24, 1],
           [25, 1],
           [26, 1],
           [27, 1],
           [28, 0],]
    start_time = time.time()
    # Create the animation object
    ani = animation.FuncAnimation(fig, acc_animate, fargs=(xs, ys, acc), frames=len(acc), interval=100)
    # To save the animation, use ani.save() here
    plt.show()
    fig.savefig("final.png")


def check_termination():
        global keep_running
        #example
        time.sleep(1.5)
        keep_running = False
# Start the animation in a separate thread


# Start the termination check in the main thread
animation_thread = threading.Thread(target=run_animation)
animation_thread.start()

check_termination()

# Wait for the termination condition to be met
while keep_running:
    time.sleep(0.1)  # Short sleep to reduce CPU usage

# After the termination condition is met, you can perform necessary cleanup
print("Termination condition met. Exiting...")
plt.close()
# Here you might want to close the plot or clean up resources.
# Note: closing the plot from a non-main thread might require special handling depending on the environment.

#Max Acceleration----------------------

# maximum acceleration data
linear_acc_values = [row[1] for row in acc]
linear_acc_max = max(linear_acc_values)

# Extract the row where the 2nd element matches the linear_acc_max
row_of_linear_acc_max = next(row for row in acc if row[1] == linear_acc_max)

#Extract the 1st element of that row which corresponds to the time

#Stride Time---------------------------May have to modify the extract rows code in case there is an error if the strides are uneven think it's fine tho

# Initialize variables
extracted_rows = []
looking_for_non_zero = True  # Start by looking for non-zero following a zero
previous_was_zero = True  # Initialize as True to capture the first non-zero
stride_time_list = []

for i, row in enumerate(acc):
    if looking_for_non_zero:
        # If the previous was zero and the current is non-zero, switch the condition
        if previous_was_zero and row[1] != 0:
            extracted_rows.append(row)
            looking_for_non_zero = False  # Next, look for a zero
    else:
        # If the previous was non-zero and the current is zero, switch the condition
        if not previous_was_zero and row[1] == 0:
            extracted_rows.append(row)
            looking_for_non_zero = True  # Next, look for a non-zero
    
    # Update the previous_was_zero based on the current row
    previous_was_zero = (row[1] == 0)

for i in range(0, len(extracted_rows) - 1, 2):
    # Subtract the first element of the i-th row from the (i+1)-th row
    stride_time_result = extracted_rows[i + 1][0] - extracted_rows[i][0]
    stride_time_list.append(stride_time_result)

#average stride time calc
average_stride_time = np.mean(stride_time_list)

#cadence calc is number of steps taken during the trial
cadence = len(extracted_rows) / 2

print(f"{cadence} is cadence")
print(f"{average_stride_time}is stride time")
print(f"{linear_acc_max} is max")