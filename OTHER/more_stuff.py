import random

def inches_to_feet():
    number_of_inches = int(input('Enter the number of inches: '))

    feet = number_of_inches // 12
    leftover_inches = number_of_inches % 12

    print(f'That is {feet} feet and {leftover_inches} inches.')

def random_demo():
    print(random.random())
    print(random.randint(-1, 0))

    user_seed = int(input('Enter a seed for the RNG: '))
    random.seed(user_seed)

    print(random.random())


def rec_redux():
    height = int(input('How tall would you like the rectangle? '))
    width = int(input('How wide would you like the rectangle? '))

    print('*' * width)

    for x in range(height):
        print('*' + ' ' * (width-2) + '*')

    print('*' * width)

    # print('*****')
    
    # for x in range(height):
    #     print('*   *')
    
    # print('*' * 5, end='')
    # print('\n*   *' * height)

    # print('*****')


def join_demo():
    my_list = ['a', 'b', 'c']
    print(my_list)

    new_string = ''.join(my_list,)
    print(new_string)

















# rec_redux()
# random_demo()
join_demo()

