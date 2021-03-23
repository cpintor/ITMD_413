import time
import random
our_list = []
for i in range(0,50000): # create 10000 random numbers
    x = random.randint(1,50000) # ranges 1 to 10000
    our_list.append(x)

def bubble_sort(our_list):
    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]

bubble_sort(our_list)
print(our_list)

start_time = time.time() # start the clock
bubble_sort(our_list) #  put your sorting method
stop_time = time.time() - start_time # stop the clock and calculate the time difference
print("--- the sort took %s seconds ---" % stop_time)