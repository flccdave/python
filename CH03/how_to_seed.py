import random

# Get the seed from the user
user_seed = int(input("Enter a seed: "))

# Seed the random module with the input:
random.seed(user_seed)

# Generate random numbers
print(random.random())       # Random number [0.000 to 0.999999]
print(random.randint(1, 10)) # Random number [1, 10]
















