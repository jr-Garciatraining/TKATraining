import time
#code to print out clock
curr_time = time.localtime
curr_clock = time.strftime("%H:%M:%S", curr_time)

#print result
print(curr_clock)

print(curr_time)
