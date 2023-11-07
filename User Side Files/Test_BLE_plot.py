import matplotlib.pyplot as plt
import matplotlib.animation as animation
from acc_functions import calc_linear_acc

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
    

def acc_animate(i, s_time, xs, ys):

        data_str = read_from_bluetooth()

        ax = float(data_str.split('Ax g: ')[1].split('Ay')[0].strip())
        ay = float(data_str.split('Ay g: ')[1].split('Az')[0].strip())

        # Read data from MPU6050
        linear_acc_value = calc_linear_acc(ax, ay)

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


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
result = ""

start_time = time.time()

ani = animation.FuncAnimation(fig, acc_animate, fargs=(start_time, xs, ys), interval=100)
plt.show()