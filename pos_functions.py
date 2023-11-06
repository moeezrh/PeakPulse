import math

def calc_pos_scalar(firstvelocity1,firstvel2,secondaxis1,secondaxis2):

    #resultant x-axis component
    totalaxis1 = firstaxis1 + secondaxis1
    #resultant y-axis component
    totalaxis2 = secondaxis2 + secondaxis2
    #resultant velocity scalar after adding the two acceleration vectors together
    total_vel = math.sqrt(totalaxis1**2 + totalaxis2**2)
    return total_vel
