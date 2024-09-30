
# FILE NAME: cm_and_inch_converter.py
# AUTHOR: 
# DATE: 
# DESCRIPTION: 

def main():
    cm_and_inch_converter()

def cm_and_inch_converter():
    user_choice = int(input('''
Welcome to the converter. Please choose from the following menu:
    1. Convert from cm to in
    2. Convert from in to cm
          
Your choice: '''))

    if user_choice == 1:
        
        centimeters = int(input('Enter the number of centimeters: '))
        inches = centimeters / 2.54
        print(f'{centimeters} centimeters is {inches} inches.')

    # elif user_choice == 2:
    else:
        
        inches = int(input('Enter the number of inches: '))
        centimeters = inches * 2.54
        print(f'{inches} inches is {centimeters} centimeters.')

main()