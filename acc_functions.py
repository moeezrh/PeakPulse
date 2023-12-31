import math

def calc_linear_acc(axis1, axis2):
    total_acc_scalar = math.sqrt(axis1**2 + axis2**2)
    #print("Net acceleration in the x-y plane is ", total)
    if total_acc_scalar < 0.1:
        total_acc_scalar = 0

    return total_acc_scalar

def calc_acc_angle(axis1,axis2):
 # Calculate the angle in radians
    angle = math.atan2(axis1, axis2)

    # Convert angle from radians to degrees
    angle_deg = math.degrees(angle)
    return angle_deg