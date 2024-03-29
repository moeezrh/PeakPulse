import socket
import time
from acc_functions import calc_linear_acc
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os

current_dir = os.getcwd()
#parent_dir = os.path.dirname(current_dir)


#Connecting to the RPI Wirelessly
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
UDP_IP = IPAddr
UDP_PORT = 5006
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# List to store data
linear_acc_list = []

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
result = ""

# Format plot
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.30)
plt.title('Linear Acceleration over Time')
plt.ylabel('Acceleration (g)')
ax.set_ylim(0, 10)
ax.set_xlim(0, 10)

my_line, = ax.plot([], [])

# Updating the live plot
def acc_animate(i, s_time, xs, ys):

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    decoded_data = data.decode("utf-8")
    #print("%s" % decoded_data)

    acc_x = decoded_data[7:12]
    #acc_y = decoded_data[20:25]
    acc_z = decoded_data[33:38]


    linear_acc_value = calc_linear_acc(float(acc_x), float(acc_z))
    if linear_acc_value < 0.5:
        linear_acc_value = 0

    plot_time = float(round((time.time() - s_time), 1))

    linear_acc_list.append([plot_time, linear_acc_value])
    
    # Add x and y to lists
    xs.append(plot_time)
    ys.append(linear_acc_value)
    
    my_line.set_data(xs, ys)

    if plot_time >= 10:
        ani.event_source.stop()
        fig.savefig("graph.png")
        plt.close()

# Receive and discard incoming data until the buffer is empty
clear = 0
while clear < 30:
    data, addr = sock.recvfrom(1024)
    clear += 1

# continuously plotting table
start_time = time.time()
ani = animation.FuncAnimation(fig, acc_animate, frames = 40 , fargs=(start_time, xs, ys), interval=0)
plt.show()
print("test")

#Max Acceleration----------------------

# maximum acceleration data
linear_acc_values = [row[1] for row in linear_acc_list]
linear_acc_max = max(linear_acc_values)

# Extract the row where the 2nd element matches the linear_acc_max
row_of_linear_acc_max = next(row for row in linear_acc_list if row[1] == linear_acc_max)

#Extract the 1st element of that row which corresponds to the time
time_of_acc_max = row_of_linear_acc_max[0]

#Stride Time---------------------------

# Initialize variables
extracted_rows = []
looking_for_non_zero = True  # Start by looking for non-zero following a zero
previous_was_zero = True  # Initialize as True to capture the first non-zero
stride_time_list = []

for i, row in enumerate(linear_acc_list):
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
    print(row[1])
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

print(f"{linear_acc_max} is max acceleration at {time_of_acc_max} seconds")
print(f"{average_stride_time}is stride time")
print(f"{cadence} is cadence")



#Write the data to a text file
data_file = os.path.join(current_dir, "data.txt")
with open(data_file, "w") as file:
        file.write("Maximum Acceleration: " + str(linear_acc_max) + "\n")
        file.write("Cadence: " + str(cadence) + "\n")
        file.write("Average Stride Time: " + str(average_stride_time) + "\n")
