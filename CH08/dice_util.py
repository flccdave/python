import random

def roll_D6():
    die_01 = random.randint(1, 6)
    return die_01

def roll_DX(sides):
    return random.randint(1, sides)

def roll_2_D6():
    die_01 = roll_D6()
    die_02 = roll_D6()
    dice = [die_01, die_02]
    return dice

def roll_X_D6(number_of_rolls):
    dice = []

    for x in range(number_of_rolls):
        die_01 = roll_D6()
        dice.append(die_01)
        # print(f'DEBUG: {die_01}')

    return dice

def roll_X_DX(number_of_rolls, number_of_sides):
    dice_rolls = []

    for x in range(number_of_rolls):
        die_01 = roll_DX(number_of_sides)
        dice_rolls.append(die_01)

    return dice_rolls        
