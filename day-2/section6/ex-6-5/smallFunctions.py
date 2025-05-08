def is_positive(number):
    return number > 0


def is_even(number):
    return number % 2 == 0


def double(number):
    return number * 2


def triple(number):
    return number * 3


def process_item(item):
    if not is_positive(item):
        return 0
    if is_even(item):
        return double(item)
    return triple(item)


def calculate_sum(data):
    return sum(data)


def calculate_average(data):
    return calculate_sum(data) / len(data) if data else 0


def process_data(data):
    result = [process_item(item) for item in data]
    sum_result = calculate_sum(result)
    average_result = calculate_average(result)
    print(f"Total: {sum_result}, Average: {average_result}")
    return result
