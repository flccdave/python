import random


def shifty_lists():
    names = []
    input_name = None

    while input_name != "EOF":
        input_name = input("Enter the name of the guest: ")
        names.append(input_name)

    names.pop()

    print(names)

    # last_name = names.pop()
    # names.insert(0, last_name)

    # names.insert(0, names.pop())

    first_name = names.pop(0)
    names.append(first_name)

    print(names)


def average_values():
    number_list = []
    number = None

    while True:
        number = input("Enter a number: ")

        if number != 'DONE':
            number_list.append(int(number))
        else:
            break
    
    print('\n---END OF INPUT---\n')

    print(f'NUMBERS = {number_list}')

    # sum_of_numbers = sum(number_list)

    sum_of_numbers = 0

    # for num in range(0, len(number_list)-1):

    for num in number_list:
        sum_of_numbers += num
    
    print(f'SUM = {sum_of_numbers}')

    # print(f'AVERAGE = {sum_of_numbers / len(number_list)}')

    average_of_numbers = sum_of_numbers / len(number_list)

    rounded_average = round(average_of_numbers)


    # print(f'AVERAGE = {average_of_numbers}')
    print(f'AVERAGE = {rounded_average}')


def fortune_machine():
    print('''=======================================
Welcome to the Fortune Telling Machine!
=======================================''')
    
    print('Enter some fortunes. Type "DONE" when you are through.')

    fortunes = []
    user_fortune = None

    while user_fortune != 'DONE':
        user_fortune = input('Enter a fortune: ')
        fortunes.append(user_fortune)
    
    fortunes.pop()

    # print(random.choice(fortunes))
    # yes_no = input('Another fortune (y/n)? ')

    yes_no = 'y'

    while yes_no == 'y':
        print(random.choice(fortunes))
        yes_no = input('Another fortune (y/n)? ')










    print('''
          
          
          
Thank you for using the Fortune Telling Machine!
Smash that LIKE and Subscribe button and tell your friends!''')






        


# average_values()
fortune_machine()