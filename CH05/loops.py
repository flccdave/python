import random

def while_loop_01():

    number = 1

    while number < 10:
        print(number)
        number = number + 1

def while_loop_02():
    
    yes_or_no = 'yes'
    
    while yes_or_no.lower() == 'yes':
        print(random.random())
        yes_or_no = input('Would you like another random number (yes/no)? ')

def for_loop_01():

    number = 1

    for number in range(1, 11, -1):
        print(number)

def coin_flip():
    
    number_of_heads = 0
    

    for flip in range(1, 101):
        coin_flip = random.randint(1, 2)
        if coin_flip == 1:
            number_of_heads = number_of_heads + 1
        
    print(f'Number of heads: {number_of_heads}')





# while_loop_01()
# while_loop_02()
# for_loop_01()
coin_flip()


print('\n\nGAME OVER MAN!!!!')