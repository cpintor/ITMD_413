import time
import random
random_list_of_nums = []
for i in range(0,70000): # create 10000 random numbers
    x = random.randint(1,70000) # ranges 1 to 10000
    random_list_of_nums.append(x)

def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


# Verify it works
quick_sort(random_list_of_nums)
print(random_list_of_nums)

start_time = time.time() # start the clock
quick_sort(random_list_of_nums) #  put your sorting method
stop_time = time.time() - start_time # stop the clock and calculate the time difference
print("--- the sort took %s seconds ---" % stop_time)