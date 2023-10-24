import math

Ax = 0.5
Ay = 0.25
Az = 0.25

def calc_linear_acc(Ax, Ay):
    total = math.sqrt(Ax**2 + Ay**2)
    print("Net acceleration in the x-y plane is ", total)
    return total

calc_linear_acc(Ax, Ay)