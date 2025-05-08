def is_positive(number):
    return number > 0


def is_even(number):
    return number % 2 == 0


def process_item(item):
    if not is_positive(item):
        return 0
    if is_even(item):
        return item * 2
    return item * 3


def process_data(data):
    return [process_item(item) for item in data]
