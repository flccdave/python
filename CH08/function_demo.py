import math

# number = None # Global Variable

def triangle():
    print('  *  ')
    print(' *** ')
    print('*****')

def triangle_demo():
    triangle()
    triangle()
    print('\nGAME OVER MAN!!!!!')

def number_doubler(num):
    num = num * 2
    # print(num)
    return num

def number_doubler_demo():
    print('Welcome to the Functionator2000')
    number = int(input('Enter a number to double: '))
    new_number = number_doubler(number)
    print(new_number)

def number_quader(four_times):
    if four_times == 0:
        return 0
    else:
        four_times = four_times * four_times * four_times * four_times
        # number_doubler(four_times) * number_doubler(four_times)
        return four_times



def number_quader_demo():
    print('Welcome to the Functionator4000')
    number = float(input('Enter a number to quadruple: '))
    new_number = number_quader(number)
    print(f'{number} to the fourth power is {new_number}')

def exponenter(base, exp):
    # return base ** exp
    # return pow(base, exp)
    # return math.pow(base, exp)

    if exp == 0:
        return 1
    
    result = 1

    for x in range(exp):
        result *= base

    return result


def exponenter_demo():
    print('Welcome the Exponenter5000')
    base = int(input('Enter the base: '))
    exp = int(input('Enter the exponent: '))
    result = exponenter(base, exp)
    print(f'The result of {base} to the {exp}th power is {result}.')








 



# triangle_demo()
# number_doubler_demo()
# number_quader_demo()
exponenter_demo()

















