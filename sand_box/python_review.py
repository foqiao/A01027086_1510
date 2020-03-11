# dictionary
student = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'phone': '555-5555'}

# change value
# student['phone'] = 555-5555
student.update({'key1': 'Jenny', 'key2': 22, 'key3': 'undergrad'})

# pop-out value
student.pop('key3')
print(len(student))
print(student.keys())
print(student.items())

for key in student.items():
    print(key)

# if-else
if True:
    print('conditional was true')

if False:
    print("condition was false")

lang = 'python'
if lang == 'python':
    print(lang)
elif lang == 'java':
    print(lang)
else:
    print('No match')

# object identity in python:
# is, not, and, or

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please log in')
else:
    print('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(id(a) is id(b))
print(a == b)

condition = True

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 10

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# loops and iteration
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1


# infinite loop below!!!
# while True:
#    print(x)
#    x += 1

# Function
# instruction for specific tasks
def hello_func(greeting):
    return '{} Hello Function.'.format(greeting)


hello_func('Hi')
hello_func('Hi')
hello_func('Hi')
hello_func('Hi')


# keep your code dry or stop repeating, common in computer programming
# * for unpack the value stored in variables
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)

# let's start a function
print('imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    for j, value in enumerate(to_search):
        if value == target:
            return j
    return -1


# variable scope
# local, enclosing, global, built-in or abbreviation LEGB
x = 'global x'


def test1():
    y = 'local x'
    print(y)


test1()

import builtins

print(dir(builtins))
