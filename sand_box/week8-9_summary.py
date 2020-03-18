import string
from random import randint

number = set()
number.add(1)
number.add(2)
number.add(2)
number.add(3)
number.add(1)
print(number)

alpha = set()
a = 'b'
alpha.add(a)
a = 'c'
alpha.add(a)
alpha.remove(a)
print(alpha)

alphabet = string.ascii_letters
for i in range(0, len(alphabet)):
    print(alphabet[i])

#positional argument

def positional_argument(name):
    print("Hello, %s" % name)

name1 = str(input("Please enter your name: "))
positional_argument(name1)

#keyword argument
num_list = [1, 2, 4, 5, 8, 90]
num_list.sort(reverse=True)
print(num_list)

def validate(name, take_a_number):
    name_list = {}
    if take_a_number % 2 == 0:
        name_list.update({take_a_number: name})
        print(name_list)

def main():
    name_input = str(input("Please enter your name: "))
    take_a_number_input = int(input("Please enter your number: "))
    validate(name=name_input, take_a_number=take_a_number_input)

if __name__ == '__main__':
    main()

#default value indication
def format_name(first, last, middle=''):
    if middle:
        print("(%s,%s,%s)" % (first, middle, last))
    else:
        print("(%s,%s)" % (first, last))

format_name('Donald', 'Trump', 'J')

#arbitary num example
def build_profile(first, last, **user_info):
    profile = {}
    profile.update({'first_name': first})
    profile['first_name'] = first
    profile.update({'last_name': last})
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

build_profile('albert', 'einstein', location='princeton', field='physics')