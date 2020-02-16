# define a function with two arguments
def format_name(first_name, last_name):
    # specify what the two parameters gonna do
    full_name = first_name + last_name
    return full_name

# enter the values needed to process within the function above
first_name1 = "Ted"
last_name1 = "Yuan"
format_name1 = format_name(first_name1, last_name1)
print(format_name1)

# define a function with one arguments
def tripler(string):
    # specify what the parameter gonna do
    return str(string) * 3

# enter the values for the function above
string = "How are you!"
print(tripler(string))

# define a function with two arguments
def this_year():
    # specify what two parameter gonna do
    # enter the input value for the function above
    a = 2000
    b = 20
    formula = a + b
    return formula

this_year()