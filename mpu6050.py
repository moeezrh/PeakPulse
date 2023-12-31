
import smbus			#import SMBus module of I2C
import time        
from time import sleep
import math
from acc_functions import calc_linear_acc
from queue import Queue


import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation

     

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

# This function is called periodically from FuncAnimation
def acc_animate(i, s_time, xs, ys):

        # Read data from MPU6050
        acc_x = read_raw_data(ACCEL_XOUT_H)/16384.0
        acc_z = read_raw_data(ACCEL_ZOUT_H)/16384.0
        linear_acc_value = calc_linear_acc(acc_x, acc_z)

        # Add x and y to lists

        xs.append(float(round((time.time() - s_time), 1)))
        ys.append(linear_acc_value)

        # Limit x and y lists to 20 items
        # xs = xs[-20:]
        # ys = ys[-20:]

        max_time = int(max(xs)) if xs else 0
        ax.set_xticks(range(0, max_time + 1, 5))

        # Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)
        ax.set_ylim(0, 5)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Linear Acceleration over Time')
        plt.ylabel('Acceleration (g)')

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
result = ""

bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address


MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")


while True:


        #Read Accelerometer raw value
        acc_x = read_raw_data(ACCEL_XOUT_H)
        acc_y = read_raw_data(ACCEL_YOUT_H)
        acc_z = read_raw_data(ACCEL_ZOUT_H)
        
        #Read Gyroscope raw value
        #gyro_x = read_raw_data(GYRO_XOUT_H)
        #gyro_y = read_raw_data(GYRO_YOUT_H)
#	gyro_z = read_raw_data(GYRO_ZOUT_H)
        
        #Full scale range +/- 250 degree/C as per sensitivity scale factor
        Ax = acc_x/16384.0
        Ay = acc_y/16384.0
        Az = acc_z/16384.0

        
#	Gx = gyro_x/131.0
#	Gy = gyro_y/131.0
#	Gz = gyro_z/131.0

        start_time = time.time()
        ani = animation.FuncAnimation(fig, acc_animate, fargs=(start_time, xs, ys), interval=100)
        plt.show()

#	print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
        print ("\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az)                                                                 
        sleep(0.01)


   