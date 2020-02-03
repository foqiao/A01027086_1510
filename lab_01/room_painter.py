# named two variable painter and coverage
painter = 4
coverage = 100 * painter

# receive inputs from a user
length = int(input("Please enter value for your room length:"))
width = int(input("Please enter value for your room width:"))
height = int(input("Please enter value for your room height:"))
coat = int(input("Please enter how many layers you want to paint for your room:"))

# the inputs inserted into the formulas below
surface_area = (length * height) * 4 + length * width
coverage_need = surface_area * coat
cans_of_paint_required = coverage_need / coverage

# print the final result with two strings of words on two sides
print("You will need " + str(cans_of_paint_required) + " cans.")