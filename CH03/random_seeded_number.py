import random

seed_from_user = int(input('Enter a seed for the random number generation: '))
random.seed(seed_from_user)

random_number = random.random()
print(random_number)