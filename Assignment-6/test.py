import time
import random
mylist = []
for i in range(0,10000): # create 10000 random numbers
    x = random.randint(1,10000) # ranges 1 to 10000
    mylist.append(x)
start_time = time.time() # start the clock
sorting_method_function(mylist) #  put your sorting method
stop_time = time.time() - start_time # stop the clock and calculate the time difference
print("--- the sort tool %s seconds ---" % stop_time)
