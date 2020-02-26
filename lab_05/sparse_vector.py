def sparse_add(vector1: int, vector2: int) -> dict:
    list_of_sum = {}
    for index1 in vector1:
        for index2 in vector2:
            if index1 == 'length' or index2 == 'length':
                list_of_sum.update({'length': 5})
            else:
                sum_of_vectors = vector1[index1] + vector2[index1]
                list_of_sum.update({index1: sum_of_vectors})
    return list_of_sum

def sparse_dot_product(vector1: int, vector2: int) -> dict:
    list_of_product = {}
    for index1 in vector1:
        for index2 in vector2:
            if index1 == 'length' or index2 == 'length':
                list_of_product.update({'length': 5})
            else:
                mul_of_vectors = vector1[index1] * vector2[index1]
                list_of_product.update({index1: mul_of_vectors})
    return list_of_product

def main():
    vector_input1 = {'length': 5, 0: 6, 3: 9}
    vector_input2 = {'length': 5, 0: 8, 3: 3}
    print(sparse_add(vector_input1, vector_input2))
    print(sparse_dot_product(vector_input1, vector_input2))

if __name__ == '__main__':
    main()