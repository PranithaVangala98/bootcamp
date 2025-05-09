import multiprocessing
import time


# Define a function to perform a computational task
def compute_square(number):
    result = number * number
    print(f"Square of {number}: {result}")
    time.sleep(1)  # Simulate a time-consuming task


def compute_cube(number):
    result = number * number * number
    print(f"Cube of {number}: {result}")
    time.sleep(1)  # Simulate a time-consuming task


if __name__ == "__main__":
    # Create two processes to run the functions concurrently
    process1 = multiprocessing.Process(target=compute_square, args=(5,))
    process2 = multiprocessing.Process(target=compute_cube, args=(3,))

    # Start both processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    print("Both processes have finished.")
