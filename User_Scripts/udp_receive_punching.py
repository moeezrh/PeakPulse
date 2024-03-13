import socket
import time
from acc_functions import calc_linear_acc
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

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
plt.title('G-Force over Time')
plt.ylabel('Acceleration (g)')
ax.set_ylim(0, 15)
ax.set_xlim(0, 10)

my_line, = ax.plot([], [])

# Updating the live plot
def acc_animate(i, s_time, xs, ys):

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    decoded_data = data.decode("utf-8")
    #print("%s" % decoded_data)

    acc_x = decoded_data[7:12]
    acc_y = decoded_data[20:25]
    #acc_z = decoded_data[33:38]


    linear_acc_value = calc_linear_acc(float(acc_x), float(acc_y))
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
linear_acc_values = []

for row in linear_acc_list:
     linear_acc_values.append(row[1])
linear_acc_max = max(linear_acc_values)

# Extract the row where the 2nd element matches the linear_acc_max
row_of_linear_acc_max = next(row for row in linear_acc_list if row[1] == linear_acc_max)

#Extract the 1st element of that row which corresponds to the time
time_of_acc_max = row_of_linear_acc_max[0]

print(f"{linear_acc_max} is max acceleration at {time_of_acc_max} seconds")

# Calculating human punch force
# Get the user weight
with open("C:/Users/moeez/Documents/repos/PeakPulse/config.txt", 'r') as file:
    weight = file.read()

if weight == "":
    weight = 1

# Convert to lbs
conv_weight = float(weight) * 0.453592
# Calculating impact force in newtons
force = conv_weight * float(linear_acc_max)
# converting to pounds-force
lb_force = force * 0.22481

linear_acc_max = round(linear_acc_max, 2)
lb_force = round(lb_force, 2)
force = round(force, 2)


#Write the data to a text file
filename = "C:/Users/moeez/Documents/repos/PeakPulse/data.txt"
with open(filename, "w") as file:
        file.write("Maximum Acceleration: " + str(linear_acc_max) + " Gs\n")
        file.write("Maximum Impact Force  (N): " + str(force) + " Ns\n")
        file.write("Maximum Impact Force (lbf): " + str(lb_force) + " lbf\n")

