import bluetooth

# MAC address of the computer you are connected to
target_address = 'AC:12:03:78:DF:E2'  # Replace this with the computer's MAC address

port = 4  # The default port for Bluetooth RFCOMM communication

# Establish a connection to the computer
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_address, port))

# Data to be sent
message = "Hello from Raspberry Pi!"

# Send the data
sock.send(message)

# Close the socket
sock.close()
