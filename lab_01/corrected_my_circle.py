PI = 3.14159

radius = int(input("Please input a length for radius: "))
new_radius = radius * 2

circumference = radius * PI * 2
area = radius ** 2 * PI

new_circumference = new_radius * PI * 2
new_area = new_radius ** 2 * PI

comparing_two_circumference = new_circumference / circumference
comparing_two_area = new_area / area

print("The lengths of radius and new_radius are " + str(radius) + " and " + str(new_radius))
print("The circumferences of two radius are " + str(circumference) + " and " + str(new_circumference))
print("The areas of two radius are " + str(area) + " and " + str(new_area))
print("The new_circumference is " + str(comparing_two_circumference) + " larger than " + str(circumference))