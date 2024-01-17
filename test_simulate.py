import math
import time

# Define parameters
start_time = time.time()
interval = 0.25
duration = 10

# Simulate accelerometer data
data = []

for _ in range(int(2 / interval)):  # Linear values for the first 2 seconds
    data.append(1)

for _ in range(int(8 / interval)):  # Sine wave for the next 8 seconds
    data.append(5 * math.sin(2 * math.pi * ((time.time() - start_time - 2) % 8) / 8))

# Display the first 10 values of the generated data
print(data[:10])
