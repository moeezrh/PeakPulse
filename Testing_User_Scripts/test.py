linear_acc_list = [[0.5, 1], [1, 1], [1.5, 1], [2, 2], [2, 2], [2, 2], [2.5, 3], [2.5, 3], [2.5, 3]]


# maximum acceleration data
linear_acc_values = [row[1] for row in linear_acc_list]
linear_acc_max = max(linear_acc_values)
max_addr = linear_acc_values.index(linear_acc_max)
print(max_addr)
time_max = linear_acc_list[max_addr][0]
print(linear_acc_max)
print(time_max)