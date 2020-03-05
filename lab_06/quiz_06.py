import math
import time

def timer(func):
    """Print the runtime of the decorated function"""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return run_time
    return wrapper_timer

@timer
def Ted_Eratosthenes(upperBound):
    prime_number = []
    number = list(range(upperBound + 1))
    while len(number) > 0:
        i = number.pop(0)
        if i >= 2:
            prime_number.append(i)
            j = 1
            multiplied_num = i * j
            while multiplied_num <= upperBound:
                if multiplied_num in number:
                    number.remove(multiplied_num)
                j += 1
                multiplied_num = i * j

    return prime_number

# upperBound_input = 30
# prime_number1 = Ted_Eratosthenes(upperBound_input)
# print(prime_number1)

@timer
def zenen_eratosthenes(positive_integer):

    nums_list = list(range(2, positive_integer + 1))  # end non inclusive

    for i in nums_list:
        if zenen_is_prime(i):
            for j in range(2 * i, positive_integer + 1, i):
                if j in nums_list:
                    nums_list.remove(j)

    return nums_list  # chop off the off by one error

def zenen_is_prime(n):
    if n == 1:
        return False

    return math.factorial(n - 1) % n == n - 1  # Wilsons theory... gotta love

@timer
def trevor_eratosthenes(upperbound):
    primes_under_10 = [2, 3, 5, 7]
    non_primes = []
    primes = []
    list_of_nums = list(range(2, upperbound + 1))
    for item in primes_under_10:
        for i in range(2, int(upperbound)):
            if item * i <= upperbound:
                non_primes.append(item * i)
    for j in list_of_nums:
        if j not in non_primes:
            primes.append(j)
    return primes


def main():
    time_dictionary = {
        "Teds method": Ted_Eratosthenes(1000),
        "Trevors method": trevor_eratosthenes(1000),
        "Zenens method": zenen_eratosthenes(1000)
    }
    print(f"The fastest time is {min(time_dictionary)} with a time of {time_dictionary.get(min(time_dictionary))}")




if __name__ == "__main__":
    main()