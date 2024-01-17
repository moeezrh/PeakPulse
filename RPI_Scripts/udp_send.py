import socket

# setting the target receiver of data (it will always be .1.2 since there are only 2 devices allowed on the network)
UDP_IP = "192.168.1.2"
UDP_PORT = 5006

# print("UDP target IP: %s" % UDP_IP)
# print("UDP target port: %s" % UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP

# protocol layer built on top of i2c protocol
import smbus
bus = smbus.SMBus(1)
Device_Address = 0x68

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47


# Writing the addresses to each register on the MPU
def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	
	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	
	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)
	
	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	
	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

# Reads the data from the MPU
def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    
    #concatenate higher and lower value
    value = ((high << 8) | low)
        
    #to get signed value from mpu6050
    if(value > 32768):
            value = value - 65536
    return value

# instantiates the addresses on the MPU
MPU_Init()

# continuously sends formatted accleerometer data
while True:
	acc_x = read_raw_data(ACCEL_XOUT_H)/16384.0
	acc_y = read_raw_data(ACCEL_YOUT_H)/16384.0
	acc_z = read_raw_data(ACCEL_ZOUT_H)/16384.0

	formatted_acc_x = "{:05.2f}".format(round(acc_x, 2))
	formatted_acc_y = "{:05.2f}".format(round(acc_y, 2))
	formatted_acc_z = "{:05.2f}".format(round(acc_z, 2))
	MESSAGE = ("Acc X: " + formatted_acc_x + "\tAcc Y: " + formatted_acc_y + "\tAcc Z: " + formatted_acc_z).encode()

	try:
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	except ConnectionRefusedError:
		print("No Receiver available")
		time.sleep(5)
