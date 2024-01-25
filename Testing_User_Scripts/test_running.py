
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation



# This function is called periodically from FuncAnimation
def acc_animate(i, s_time, xs, ys, index):

    acc = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0]

    # Add x and y to lists

    xs.append(float(round((time.time() - s_time), 1)))
    ys.append(acc[index])


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



# continuously plotting table
index = 0
while True:
    start_time = time.time()
    ani = animation.FuncAnimation(fig, acc_animate, frames = 40 , fargs=(start_time, xs, ys, index), interval=100)
    index = index + 1
    plt.show()
    print("test")


