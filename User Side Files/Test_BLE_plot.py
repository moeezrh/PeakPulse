import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize lists to store the time, Ax, and Ay values
times = []
ax_values = []
ay_values = []
products = []


import bluetooth
import time

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
                            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE],
                            # protocols=[bluetooth.OBEX_UUID]
                            )

print("Waiting for connection on RFCOMM channel", port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

time.sleep(5)

# This function simulates reading from a Bluetooth device
def read_from_bluetooth():
    data = client_sock.recv(1024)
    return data.decode('utf-8')
    
start_time = time.time()

def acc_animate(i, s_time, xs, ys):

        # Read data from MPU6050
        linear_acc_value = calc_linear_acc(read_raw_data(ACCEL_XOUT_H)/16384.0, read_raw_data(ACCEL_ZOUT_H)/16384.0)

        # Add x and y to lists

        xs.append(str(round((time.time() - s_time), 1)))
        ys.append(linear_acc_value)

        # Limit x and y lists to 20 items
        # xs = xs[-20:]
        # ys = ys[-20:]

        # Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)
        ax.set_ylim(0, 5)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Linear Acceleration over Time')
        plt.ylabel('Acceleration (g)')

# This function is called periodically from FuncAnimation
def update_plot(frame):
    # Read the next line of data from Bluetooth
    data_str = read_from_bluetooth()

    # Parse the data
    if data_str:
        try:
            # Find the Ax and Ay values in the data string
            ax = float(data_str.split('Ax g: ')[1].split('Ay')[0].strip())
            ay = float(data_str.split('Ay g: ')[1].split('Az')[0].strip())
            
            # Get the current time or an appropriate time stamp
            current_time = ... # You need to define how to get this

            # Append the data to the lists
            times.append(current_time)
            ax_values.append(ax)
            ay_values.append(ay)
            products.append(ax * ay)

            # Update the plot
            ax_line.set_data(times, ax_values)
            ay_line.set_data(times, ay_values)
            product_line.set_data(times, products)

            # Adjust the plot to make all data visible
            plt.xlim([min(times), max(times) + 1])
            plt.ylim([min(products + ax_values + ay_values), max(products + ax_values + ay_values) + 1])

            plt.draw()
        except Exception as e:
            print(f"Error parsing data: {e}")

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
result = ""

start_time = time.time()
ani = animation.FuncAnimation(fig, acc_animate, fargs=(start_time, xs, ys), interval=100)
plt.show()