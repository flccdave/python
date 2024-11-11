def menu():
    print('Welcome to the Mathenator2000')
    print()
    print('Please choose from the following menu:')
    print('  1. Compute area of a circle')
    print('  2. Compute area of a rectangle')    

def circle():
    radius = float(input('What is the radius of the circle? '))
    area = 3.14 * radius * radius
    print(f'The area of the circle is {area}')    

def rectangle():
    length = float(input('What is the length of the rectangle? '))
    width = float(input('What is the width of the rectangle? '))
    print(f'The area of the rectangle is {length * width}')    

def main():
    menu()
    print()
    
    choice = int(input('What is your choice? '))
    print()

    if choice == 1:
        circle()
    elif choice == 2:
        rectangle()
    else: 
        print('Invalid selection.')

    print('\nThank you for using the Mathinator2000')



main()