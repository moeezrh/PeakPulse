import socket
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# print("Computer IP Address is: " + IPAddr)

UDP_IP = IPAddr
UDP_PORT = 5006

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


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

    # Add x and y to lists

    xs.append(float(round((time.time() - s_time), 1)))
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
    plt.title('Jump Force over Time')
    plt.ylabel('Acceleration (g)')

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
while True:
    start_time = time.time()
    ani = animation.FuncAnimation(fig, acc_animate, fargs=(start_time, xs, ys), interval=10)
    plt.show()


