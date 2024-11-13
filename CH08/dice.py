import dice_util

def menu():
    print('Pick from the following options:')
    print('  1. Roll a D6')
    print('  2. Roll a DX')
    print('  3. Roll 2 D6')
    print('  4. Roll X D6')
    print('  5. Roll X DX')
    print()

def main():
    menu()
    user_choice = int(input('Which option do you want? '))

    if user_choice == 1:
        die_01 = dice_util.roll_D6()
        print(die_01)

    elif user_choice == 2:
        sides = int(input('How many sides on the die? '))
        die_01 = dice_util.roll_DX(sides)
        print(die_01)

    elif user_choice == 3:
        rolls = dice_util.roll_2_D6()
        print(f'Die 1 = {rolls[0]} and die 2 = {rolls[1]} for a sum of {rolls[0] + rolls[1]}')

    elif user_choice == 4:
        number_of_rolls = int(input('How many dice do you want to roll? '))
        rolls = dice_util.roll_X_D6(number_of_rolls)
        print(rolls)

    elif user_choice == 5:
        number_of_rolls = int(input('How many dice do you want to roll? '))
        number_of_sides = int(input('How many sides on the dice? '))
        rolls = dice_util.roll_X_DX(number_of_rolls, number_of_sides)
        print(rolls)

    else:
        print('Invalid choice.')











main()


