# named two variable initially
pi = 3.14159
radius = 0

# variable radius is named, it holds an input from user
# the new_radius is the product of 2 times radius's input
radius = int(input("Please enter a number for the radius:"))
new_radius = radius * 2

print("The new-radius is: " + str(new_radius))

# two variables, circumference and circumference1, named for two different circumferences based two different radius
circumference1 = 2 * pi * radius
circumference = 2 * pi * new_radius
print("The value for the circumference is: " + str(circumference))
print("The value for the new circumference is " + str(circumference1))

# two variables, area_of_circle and area_of_circle1, named for two different area_of_circle based on
# two different radius
area_of_circle = pi * new_radius * new_radius
area_of_circle1 = pi * radius * radius
print("The value for the area of circle: " + str(area_of_circle))
print("The value for the area of circle: " + str(area_of_circle1))

# comparing two circumferences and areas and find out how big the new circumference and area compare to the old ones
circumference_compare = circumference1 - circumference
area_of_circle_compare = area_of_circle1 - area_of_circle

print("The updated circumference: " + str(circumference_compare))
print("The updated area_of_circle: " + str(area_of_circle_compare))