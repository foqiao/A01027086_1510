"""
#1 number of boxes package number of apples algorithm
def apples_vs_boxes(num_boxes, num_apples):
    if num_apples < 20:
        num_boxes = num_boxes + 1
        print(num_boxes)

    if num_apples < 10:
        num_boxes = num_boxes - 1
        print(num_boxes)

num_of_boxes = int(input("Please enter the amount of boxes: "))
num_of_apples = int(input("Please enter the amount of apples: "))
apples_vs_boxes(num_of_boxes, num_of_apples)

#2 multiple if statement(each condition is separate from each other rather than depending on)
def multiple_if_statement(user_age):
    if user_age >= 16:
        print('You are old enough to drive.')
    if user_age < 25:
        print('Enjoy your early years.')
    if user_age > 25:
        print('Most car rental companies will rent to you.')

user_age1 = int(input('Enter age: '))
multiple_if_statement(user_age1)

#3 if-else statement practice(indent practice)
def number_choice(user_choice, num_items):
    if user_choice == 1:
        print('user_choice is one')
    elif user_choice == 2:
        if num_items < 0:
            print('user_choice is 2 and num_items is less than zero')
        else:
            print('user_choice is 2 and num_items is greater and equal to 0')
    else:
        print('user_choice is neither 1 or 2')

user_choice1 = int(input('Please enter a number you currently think of: '))
num_items1 = int(input('Please enter the amount of items you want to process: '))
number_choice(user_choice1, num_items1)

#4 nested if-else statements
def sales(sales_type, sales_bonus):
    if sales_type == 2:
        if sales_bonus < 5:
            sales_bonus = 10
        else:
            sales_bonus = sales_bonus + 2
    else:
        sales_bonus = sales_bonus + 1

sales_type1 = int(input('Enter the sales_type in integer: '))
sales_bonus1 = float(input('Enter the sales_bonus in percentage: '))
sales(sales_type1, sales_bonus1)

#5 translate human logic into computational algorithms
def human_to_computer(year):
    #if year >= 2101, print distance future
    if year >= 2101:
        print('Distant future')
    #if year >= 2001, print 21st century
    elif year >= 2001:
        print('21st century')
    #if year >= 1901, print 20th century
    elif year >= 1901:
        print('20th century')
    #else(<= 1900), print long ago
    elif year <= 1900:
        print('long ago')

year1 = int(input('Please enter the year you currently think of: '))
human_to_computer(year1)
"""
#COMP1510 MIDTERM REVIEW QUESTIONS
def duck_typing(your_input):
    if your_input == "12":
        print("It's a duck type")

your_input1 = int(input("enter an integer: "))
duck_typing(your_input1)

j = [2, 3, 6, 6]
def my_function():
    i = [1, 2, 3, 4, 5]
    return i[0] * j[0]

my_function()