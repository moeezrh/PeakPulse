import math

def calculate_acceleration_vector(ax, ay):
    # Assuming ax and ay are the x and y components of acceleration
    a_resultant = math.sqrt(ax**2 + ay**2)  # Magnitude of the resultant acceleration

    # Calculate the angle in radians
    angle = math.atan2(ay, ax)

    # Convert angle from radians to degrees
    angle_deg = math.degrees(angle)

    return a_resultant, angle_deg

# Example readings from accelerometer
acceleration_x = -1  # Replace with your x-component acceleration
acceleration_y = -1  # Replace with your y-component acceleration

resultant_acceleration, direction = calculate_acceleration_vector(acceleration_x, acceleration_y)
print("Resultant Acceleration:", resultant_acceleration)
print("Direction (in degrees):", direction)
