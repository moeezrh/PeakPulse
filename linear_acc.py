import math


def calc_linear_acc(axis1, axis2):
    total = math.sqrt(axis1**2 + axis2**2)
    print("Net acceleration in the x-y plane is ", total)
    return total
