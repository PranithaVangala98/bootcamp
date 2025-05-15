import random
import time

nums = [random.randint(1, 100) for _ in range(100)]


# Bubble Sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Built-in sort function
def built_in_sort(arr):
    return sorted(arr)


start  =time.time()
bubble_sort(nums.copy())
print('bubble-sort',time.time()-start)

start  =time.time()
built_in_sort(nums.copy())
print('built_in_sort',time.time()-start)


