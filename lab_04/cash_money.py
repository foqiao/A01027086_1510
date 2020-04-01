from numpy import NaN


def cash_money(input_amount):
    currency = [100, 50, 10, 5, 2, 1, 0.1, 0.05, 0.01]
    convert_amount = []
    if input_amount < 0.01 or input_amount < 0:
        return None
    elif input_amount == NaN:
        return None
    else:
        for i in currency:
            if input_amount >= i:
                quotient = input_amount // i
                input_amount -= quotient * i
                convert_amount.append(quotient)
            else:
                convert_amount.append(0)
        return convert_amount

def main():
    input_money = int(input("How many cash do you want to convert? Please enter: "))
    result = cash_money(input_money)
    print(result)

if __name__ == '__main__':
    main()