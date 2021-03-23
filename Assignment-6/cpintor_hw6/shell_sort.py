import time
import random
data = []
for i in range(0,70000): # create 10000 random numbers
    x = random.randint(1,70000) # ranges 1 to 10000
    data.append(x)

def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


size = len(data)
shellSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

start_time = time.time() # start the clock
shellSort(data, size) #  put your sorting method
stop_time = time.time() - start_time # stop the clock and calculate the time difference
print("--- the sort took %s seconds ---" % stop_time)