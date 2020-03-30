import time


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
    global product
    for i in range(1, value + 1, 2):
        if i < value:
            product = i * (i + 1)
    result = product ** (value / 2)
    return result



def main():
    value = int(input("Please enter a positive number from 1 to 100: "))
    factorial_iterative(value)
    factorial_recursive(value)

if __name__ == '__main__':
    main()