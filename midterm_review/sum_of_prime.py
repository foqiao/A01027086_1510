def sum_of_prime(upper_bound, lower_bound):
    if upper_bound > 0 and lower_bound > 0:
        if upper_bound >= lower_bound:
            for i in range(lower_bound, upper_bound + 1):
                for j in range(2, upper_bound + 1):
                    if i % j != 0:
                        print(i)
                    else:
                        pass

upper_bound_input = int(input("Please enter a maximum value for a range of prime numbers: "))
lower_bound_input = int(input("Please enter a minimum value for a range of prime numbers: "))