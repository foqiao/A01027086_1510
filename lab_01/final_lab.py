def base_conversion():
    base = int(input("Enter a base from 2 to 9: "))
    original_value = int(input("Enter a number below 624: "))
    print("This is the number " + str(original_value))
    reminder = original_value % base
    reminder1 = (original_value / base - original_value % base / base) % base
    reminder2 = ((original_value / base - original_value % base / base) / base
    - (original_value / base - original_value % base / base) % base / base) % base
    reminder3 = (((original_value / base - original_value % base / base) / base
    - (original_value / base - original_value % base / base) % base / base) /base -
    ((original_value / base - original_value % base / base) / base
     - (original_value / base - original_value % base / base) % base / base) % base / base) % base
    final_result = str(int(reminder3)) + str(int(reminder2)) + str(int(reminder1)) + str(int(reminder))
    print("The result from the conversion is " + str(final_result))

print(base_conversion())