import threading
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

keep_running = threading.Event()
keep_running.set()
start_time = time.time()
# This function is called periodically from FuncAnimation
def acc_animate(i, xs, ys, acc):
    current_time = float(round((time.time() - start_time), 1))
    xs.append(current_time)
    ys.append(acc[i % len(acc)])  # Cycle through the acc list

    max_time = int(max(xs)) if xs else 0
    ax.set_xticks(range(0, max_time + 1, 5))

    ax.clear()
    ax.plot(xs, ys)
    ax.set_ylim(0, 5)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Linear Acceleration over Time')
    plt.ylabel('Acceleration (g)')

def run_animation():
    global ani
    global ax
    # Initial setup
    fig, ax = plt.subplots()
    xs = []
    ys = []
    acc = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0]
    start_time = time.time()
    # Create the animation object
    ani = animation.FuncAnimation(fig, acc_animate, fargs=(xs, ys, acc), frames=len(acc), interval=100)
    # To save the animation, use ani.save() here
    plt.show()

def check_termination():
        global keep_running
        #example
        time.sleep(10)
        keep_running.clear()
# Start the animation in a separate thread
run_animation()

# Start the termination check in the main thread
termination_thread = threading.Thread(target=check_termination)
termination_thread.start()

# Wait for the termination condition to be met
while keep_running:
    time.sleep(0.1)  # Short sleep to reduce CPU usage

# After the termination condition is met, you can perform necessary cleanup
print("Termination condition met. Exiting...")
plt.close()
# Here you might want to close the plot or clean up resources.
# Note: closing the plot from a non-main thread might require special handling depending on the environment.
