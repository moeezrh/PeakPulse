import math

Ax = 0.5
Ay = 0.25
Az = 0.25

def calc_linear_acc(Ax, Ay, Az):
    xytotal = math.sqrt(Ax**2 + Ay**2)
    total = math.sqrt(xytotal**2 + Az**2)
    print("Net acceleration is ", total)
    return total

calc_total_acc(Ax, Ay, Az)
