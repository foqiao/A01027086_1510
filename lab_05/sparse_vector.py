def sparse_add(vector1: dict, vector2: dict) -> dict:
    """

    Calculate addition between two vectors' items
    :param vector1: dictionary contains a string of items
    :param vector2: dictionary contains another string of items
    :return: the result dictionary which combines two dictionaries
    """
    sum_of_list = 0
    list_of_sum = {}
    for index1 in vector1:
        if index1 in vector2:
            if index1 == index1:
                sum_of_vectors = vector1[index1] + vector2[index1]
                sum_of_list += sum_of_vectors
                list_of_sum.update({index1: sum_of_list})
            else:
                pass

    return list_of_sum


def sparse_dot_product(vector1: dict, vector2: dict) -> int:
    """

    Calculate multiplication between two vectors' items
    :param vector1: dictionary contains a string of items
    :param vector2: dictionary contains another string of items
    :return: the result dictionary which combines two dictionaries
    """
    product_of_list = 0
    list_of_product = {}
    for index1 in vector1:
        if index1 in vector2:
            if index1 == index1:
                product_of_vectors = vector1[index1] * vector1[index1]
                product_of_list *= product_of_vectors
                list_of_product.update({index1: product_of_list})
            else:
                pass

    return list_of_product


def main():
    vector_input1 = {1: 5, 0: 6, 3: 9, 4: 8}
    vector_input2 = {1: 5, 0: 8, 3: 3, 5: 3}
    print(sparse_add(vector_input1, vector_input2))
    print(sparse_dot_product(vector_input1, vector_input2))


if __name__ == '__main__':
    main()

# { 0:1, 2:4, 10:5}
# { 0:4, 2:-1, 11:-6}
# { 0:5, 2:3, 1-:5, 11:-6}