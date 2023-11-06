def peak_acc(given_acc):
    
    peak_value = float('-inf')  # Initialize peak value to negative infinity

    while True:
            value = float(given_acc)
            if value == 1000:
                 break
            if value > peak_value:
                peak_value = value
            
    return(peak_value)
    


