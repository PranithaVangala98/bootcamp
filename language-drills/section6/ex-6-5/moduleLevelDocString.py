"""
This module contains functions for processing numerical data,
including filtering, transforming, and calculating statistics.
"""


def process_data(data):
    result = []
    for item in data:
        if item > 0:
            if item % 2 == 0:
                result.append(item * 2)
            else:
                result.append(item * 3)
        else:
            result.append(0)
    return result
