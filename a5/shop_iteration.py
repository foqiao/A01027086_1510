import itertools

def shop_iteration(shop_dict, item_dict):
    it = itertools.cycle(shop_dict)
    for key, value in it:
        #key stores store's real-time specs
        #value represents the current crowd size of the Costco
        value = key['wait time']
        return f"{key}: {value}"
        return it[-1]

    item = itertools.cycle(item_dict)
    for key, value in item:
        #key represents the item
        #value represents the amount in stock
        print(f"{key}: {value}")
        if value == 0:
            return "out of stock"

def main():
    #add two parameter to the function before execute the main function
    shop_iteration(shop_dict, item_dict)

if __name__ == '__main__':
    main()