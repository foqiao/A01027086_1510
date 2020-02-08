def Eratosthenes(upperBound):
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

upperBound_input = 30
prime_number1 = Eratosthenes(upperBound_input)
print(prime_number1)