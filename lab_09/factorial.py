import time

"""
timer function store the procedures needed for time consumes during factorial calculations happened on two different
methods.
"""
def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        answer = f"{func.__name__!r} in {run_time:.4f}s"
        filename = 'result.txt'
        with open(filename, 'w') as project:
            project.write(answer)

    return wrapper_timer


@timer
def factorial_iterative(value):
    """
    plain loop to calculate the factorial
    :param value: input value from main function
    :return: result returned after calculations finished
    """
    global product
    for i in range(1, value + 1, 2):
        if i < value:
            product = i * (i + 1)
    result = product ** (value / 2)
    return result

def factorial_recursive(value):
    """
    recursive way to calculate factorial
    :param value: value from main function
    :return: result return after calculation finished
    """

def main():
    value = int(input("Please enter a positive number from 1 to 100: "))
    factorial_iterative(value)
    factorial_recursive(value)

if __name__ == '__main__':
    main()