import random

print('''
Welcome to the CyberMenu
      1. Generate a password
      2. Test a password
      3. Get a compliment from me!
      4. Quit
      '''
      )

user_choice = int(input('Please make a selection: '))

if user_choice == 1:
    print('You chose to generate a password. ')
    print('Your secret password is \'b@tm@n\'')
elif user_choice == 2:
    user_password = input('Enter your password: ')
    print(f'Your password {user_password} sucks.')
elif user_choice == 3:
    print(random.choice(["You have nice ears 👂.", "You have nice zygomatic arches 😊.", "You have sublime mandibles 😃."]))
elif user_choice == 4:
    print('You are logged out.')
else:
    print('Invalid choice.')



print('\n\n\nGAME OVER MAN!!!!!')





















# magic_number = 33

# user_guess = int(input('Enter a number'))

# if user_guess > magic_number:
#     print('You guessed too high!')
# elif user_guess < magic_number:
#     print('You guessed too low!')
# else:
#     print('You guessed right!')




























# proper_password = '123456'

# user_password = input('Enter your password: ')

# # The `==` operator is used to test equality
# if user_password == proper_password:
#     print('ACCESS GRANTED!')
#     print('Secret files for you to look at!')
# else:
#     print('INCORRECT PASSWORD!')

# print('\n\nGAME OVER MAN!!!!!!')















