results_list = [] # global variable

def menu():
    print('Please choose from the following menu:')
    print('  1. Compute area of a circle')
    print('  2. Compute area of a rectangle')    

def circle():
    radius = float(input('What is the radius of the circle? '))
    area = 3.14 * radius * radius
    area_result = f'The area of the circle is {area}'
    print(area_result)
    results_list.append(area_result)

def rectangle():
    length = float(input('What is the length of the rectangle? '))
    width = float(input('What is the width of the rectangle? '))
    print(f'The area of the rectangle is {length * width}')
    results_list.append(f'The area of the rectangle is {length * width}')    

def main():
    
    print('Welcome to the Mathenator2000')
    print()
    
    play_again = None

    while play_again != 'n':
        # print('temp code')

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

        print()
        play_again = input('Would you like to play again (y/n)? ')
        print()

    
    print('-------------------------')
    print('A record of your results: ')
    print(results_list)

    print('\nThank you for using the Mathinator2000')





main()