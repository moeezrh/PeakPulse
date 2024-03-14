import socket
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os

current_dir = os.getcwd()
#parent_dir = os.path.dirname(current_dir)



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
# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
result = ""

# Format plot
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.30)
plt.title('Jump Acceleration over Time')
plt.ylabel('Acceleration (g)')
ax.set_ylim(-10, 10)
ax.set_xlim(0, 10)

my_line, = ax.plot([], [])

# Updating the live plot
def acc_animate(i, s_time, xs, ys):

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    decoded_data = data.decode("utf-8")
    #print("%s" % decoded_data)

    #acc_x = decoded_data[7:12]
    acc_y = decoded_data[20:25]
    #acc_z = decoded_data[33:38]

    vertical_acc = float(acc_y) - 1

    plot_time = float(round((time.time() - s_time), 1))

    linear_acc_list.append([plot_time, vertical_acc])
    
    # Add x and y to lists
    xs.append(plot_time)
    ys.append(vertical_acc)

    my_line.set_data(xs, ys)

    if plot_time >= 10:
        ani.event_source.stop()
        fig.savefig("graph.png")    
        plt.close()


# Receive and discard incoming data until the buffer is empty
clear = 0
while clear < 20:
    data, addr = sock.recvfrom(10240)
    clear += 1

# continuously plotting table
start_time = time.time()
ani = animation.FuncAnimation(fig, acc_animate, frames = 40 , fargs=(start_time, xs, ys), interval=10)
plt.show()


# maximum acceleration data
# Filtering out values where the absolute value is less than 0.2
filtered_acc = []
for value in linear_acc_list:
    if abs(value[1]) >= 0.5:
        filtered_acc.append([value[0], value[1]])



linear_acc_max = 0


# Counts jumps by finding the point where the graph is negative, and then ignoring values within 1 second of that to avoid counting impacts
total_jumps = 0
cool_down = 0
for row in filtered_acc:
    if row[1] < 0 and row[0] > cool_down:
        total_jumps += 1
        cool_down = row[0] + 1
    if row[1] > linear_acc_max and row[0] > cool_down:
        linear_acc_max = row[1]
        time_of_acc_max = row[0]

#Get the user weight
config_file = os.path.join(current_dir, "config.txt")
with open(config_file, 'r') as file:
    weight = file.read()

#Peak Force----------------------------

peak_force = linear_acc_max * 9.81 * int(weight) * 0.4535924

linear_acc_max = round(linear_acc_max, 2)
peak_force = round(peak_force, 2)

#Write the data to a text file

data_file = os.path.join(current_dir, "data.txt")
 
with open(data_file, "w") as file:
    file.write("Number of Jumps: " + str(total_jumps) + "\n")
    file.write("Peak Acceleration: " + str(linear_acc_max) + " Gs\n")
    file.write("Peak Force: " + str(peak_force) + " N\n")