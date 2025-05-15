import random
import time

def generate_large_list(n):
    return [random.randint(1, 1000) for _ in range(n)]

def sum_list(lst):
    total = 0
    for val in lst:
        total += val
    return total

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def count_frequencies(lst):
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

def sim():
    for _ in range(10):  
        data = generate_large_list(10000)
        sum = sum_list(data)
        evens = filter_even_numbers(data)
        freqs = count_frequencies(evens)

sim()