import geometry_util as geo

print('Welcome to the Geometry Tool')

print('1. Compute area of a triangle')
print('2. Compute area of a circle')
print('3. Compute area of a rectangle')

print()

user_choice = int(input("Enter your selection: "))

if user_choice == 1:
    base = int(input("Length of base? "))
    height = int(input("Length of height? "))
    triangle_area = geo.triangle(base, height)
    print(f'The area is {triangle_area}!')

if user_choice == 2:
    radius = int(input("Length of radius? "))
    circle_area = geo.circle(radius)
    print(f'The area of the circle is {circle_area}!')

if user_choice == 3:
    base = int(input("Length of base? "))
    height = int(input("Length of height? "))
    rectangle_area = geo.rectangle(base, height)
    print(f'The area is {rectangle_area}!')
    