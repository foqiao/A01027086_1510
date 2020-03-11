def eratosthenes(upperbound):
    is_prime = [True] * (2 * upperbound)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, upperbound + 1):
        if is_prime[i]:
            print(i)
            for j in range(i * 2, upperbound + 1, i):
                is_prime[j] = False

upperbound1 = 30
eratosthenes(upperbound1)