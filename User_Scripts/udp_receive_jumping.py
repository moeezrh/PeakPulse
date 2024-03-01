import socket
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# print("Computer IP Address is: " + IPAddr)

UDP_IP = IPAddr
UDP_PORT = 5006

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# List to store data
linear_acc_list = []

# This function is called periodically from FuncAnimation
def acc_animate(i, s_time, xs, ys):

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    decoded_data = data.decode("utf-8")
    print("%s" % decoded_data)

    #acc_x = decoded_data[7:12]
    acc_y = decoded_data[20:25]
    #acc_z = decoded_data[33:38]

    vertical_acc = float(acc_y)

    print(vertical_acc)

    plot_time = float(round((time.time() - s_time), 1))

    linear_acc_list.append([plot_time, vertical_acc])
    # Add x and y to lists

    xs.append(plot_time)
    ys.append(vertical_acc)


    max_time = int(max(xs)) if xs else 0
    ax.set_xticks(range(0, max_time + 1, 5))

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)
    ax.set_ylim(0, 5)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Jump Acceleration over Time')
    plt.ylabel('Acceleration (g)')

    if plot_time >= 10:
        ani.event_source.stop()
        fig.savefig("User_Scripts/graph.png")
        plt.close()


# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
result = ""

# Receive and discard incoming data until the buffer is empty
clear = 0
while clear < 20:
    data, addr = sock.recvfrom(10240)
    clear += 1

# continuously plotting table
start_time = time.time()
ani = animation.FuncAnimation(fig, acc_animate, frames = 40 , fargs=(start_time, xs, ys), interval=10)
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

#Peak Force----------------------------

peak_force = linear_acc_max #* user_weight * 0.4535924

#Energy--------------------------------

# Initialize variables
non_zero_acc = []
extracted_rows = []
looking_for_non_zero = True  # Start by looking for non-zero following a zero
previous_was_zero = True  # Initialize as True to capture the first non-zero
looking_for_non_zero2 = True  # Start by looking for non-zero following a zero
previous_was_zero2 = True  # Initialize as True to capture the first non-zero

for i, row in enumerate(linear_acc_list):
    if looking_for_non_zero:
        # If the previous was zero and the current is non-zero, switch the condition
        if previous_was_zero and row[1] != 0:
            non_zero_acc.append(row)
            looking_for_non_zero = False  # Next, look for a zero
    else:
        # If the previous was non-zero and the current is zero, switch the condition
        if not previous_was_zero and row[1] != 0:
            non_zero_acc.append(row)
        elif not previous_was_zero and row[1] ==0:
            looking_for_non_zero = True # Next, look for a non-zero
               
    # Update the previous_was_zero based on the current row
    previous_was_zero = (row[1] == 0)

for i, row in enumerate(linear_acc_list):
    if looking_for_non_zero2:
        # If the previous was zero and the current is non-zero, switch the condition
        if previous_was_zero2 and row[1] != 0:
            extracted_rows.append(row)
            looking_for_non_zero2 = False  # Next, look for a zero
    else:
        # If the previous was non-zero and the current is zero, switch the condition
        if not previous_was_zero2 and row[1] == 0:
            extracted_rows.append(row)
            looking_for_non_zero2 = True  # Next, look for a non-zero
    
    # Update the previous_was_zero based on the current row
    previous_was_zero2 = (row[1] == 0)

#integration of extracted jumps
non_zero_sum = sum(non_zero_acc)
#integration of entire list
all_integration = sum(linear_acc_list[1])

#num_of_jumps calc is number of steps taken during the trial
num_of_jumps = len(extracted_rows) / 2

avg_energy_non_zero = non_zero_sum / num_of_jumps

avg_energy_all_integration = all_integration / num_of_jumps

print(f"You jumped {num_of_jumps} times")
print(f"Integration of extracted jumps was {non_zero_sum}")
print(f"Integration of whole graph was {all_integration}")
print(f"Avg energy of extracted jumps was {avg_energy_non_zero}")
print(f"Avg energy of whole graph was {avg_energy_all_integration}")


#Write the data to a text file
filename = "C:/Users/moeez/Documents/repos/PeakPulse/Testing_User_Scripts/TestEnvironment/data.txt"
with open(filename, "w") as file:
        file.write("Number of Jumps: " + str(num_of_jumps) + "\n")
        file.write("Integration of Jumps: " + str(non_zero_sum) + "\n")
        file.write("Integration of graph: " + str(all_integration) + "\n")
        file.write("Average energy of Jumps: " + str(avg_energy_non_zero) + "\n")
        file.write("Average energy of graph: " + str(avg_energy_all_integration) + "\n")


