def sum_of_prime(upper_bound, lower_bound):
    range_of_value = [True] * (upper_bound * 2)
    range_of_value[0] = False
    range_of_value[1] = False
    for i in range(lower_bound, upper_bound + 1):
        if range_of_value[i]:
            print(i)
            for j in range(i * 2, upper_bound + 1, i):
                range_of_value[j] = False

upper_bound_input = int(input("Please enter a maximum value for a range of prime numbers: "))
lower_bound_input = int(input("Please enter a minimum value for a range of prime numbers: "))
sum_of_prime(upper_bound_input, lower_bound_input)