import math

def calc_linear_acc(axis1, axis2):
    total = math.sqrt(axis1**2 + axis2**2)
    #print("Net acceleration in the x-y plane is ", total)
    return total



# This function is called periodically from FuncAnimation
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
