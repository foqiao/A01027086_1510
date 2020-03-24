COVERAGE = 100

length = int(input("Please enter the length of the room: "))
width = int(input("Please enter the width of the room: "))
height = int(input("Please enter the height of the room: "))
layer = int(input("Please enter how many layer you want to coat with the paint: "))

surface_area = length * width + 2 * height * width + 2 * height * length

painted_area = surface_area * layer

paint_needs = painted_area / COVERAGE

print("The surface_area needs to paint is " + str(surface_area))
print("The area needs to paint is " + str(painted_area))
print("The litres of paint requires to satisfy the demand are " + str(paint_needs))