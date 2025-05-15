def process_data(data):
    result = []
    for item in data:
        # Only process positive items because negative values are not relevant for this operation
        if item > 0:
            # Double even numbers to give them more weight in the final result
            if item % 2 == 0:
                result.append(item * 2)
            # Triple odd numbers to increase their contribution more than even numbers
            else:
                result.append(item * 3)
        else:
            # Set negative or zero items to 0, as they don't contribute to the final result
            result.append(0)
    return result
