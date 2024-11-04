import random

def welcome():
    print("=======================================")
    print("Welcome to the Fortune Telling Machine!")
    print("=======================================")
    print()
    print()

def goodbye():
    print()
    print()
    print("Thank you for using the Fortune Telling Machine!")
    print("Smash that LIKE and Subscribe button and tell your friends!")


def main():
    welcome()

    print('Enter some fortunes. Type "DONE" when you are through.')

    user_input = None
    fortune_list = []

    while user_input != 'DONE':
        user_input = input('Enter a fortune: ')
        fortune_list.append(user_input)

    print()

    fortune_list.pop()
    # print(fortune_list)




    user_choice = None

    while user_choice != 'n':
        print(random.choice(fortune_list))
        print()
        user_choice = input('Would you like to play again (y/n)? ')












    goodbye()




main()