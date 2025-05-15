def connect_to_server():
    retries = 0
    while retries < 5:  # Magic number 5
        # try to connect
        retries += 1


MAX_RETRIES = 5


def connect_to_server2():
    retries = 0
    while retries < MAX_RETRIES:
        # try to connect
        retries += 1
