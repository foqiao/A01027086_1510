def sparse_add(vector1: dict, vector3: dict) -> dict:
    """
    calculate addition between two vectors' items
    :param vector1: dictionary contains a string of items
    :param vector3: dictionary contains another string of items
    :return: the result dictionary which combines two dictionaries
    """
    list_of_sum = {}
    vector2 = {}
    vector2.update(vector3)
    for index1 in vector1:
        if index1 in vector2:
            sum_of_vectors = vector1[index1] + vector2[index1]
            list_of_sum.update({index1: sum_of_vectors})
            vector2.pop(index1)
        else:
            list_of_sum.update({index1: vector1[index1]})
    list_of_sum.update(vector2)
    return list_of_sum

def sparse_dot_product(vector1: dict, vector2: dict) -> dict:
    """
    calculate multiplication between two vectors' items
    :param vector1: dictionary contains a string of items
    :param vector2: dictionary contains another string of items
    :return: the result dictionary which combines two dictionaries
    """
    list_of_product = {}
    for index1 in vector1:
        if index1 in vector2:
            mul_of_vectors = vector1[index1] * vector2[index1]
            list_of_product.update({index1: mul_of_vectors})
    return list_of_product

def main():
    """
    enter inputs of two parameters by random
    :return: input being executed above
    """
    vector_input1 = {1: 5, 0: 6, 3: 9, 4: 8}
    vector_input2 = {1: 5, 0: 8, 3: 3, 5: 3}
    print(sparse_add(vector_input1, vector_input2))
    print(sparse_dot_product(vector_input1, vector_input2))

if __name__ == '__main__':
    main()