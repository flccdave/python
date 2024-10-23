import name_alpha as gandalf

# text_file = open("/workspaces/python/CH07/names.txt", "r")
# print(text_file)
# print('Writable? ', text_file.writable())
# print('Readable? ', text_file.readable())

# names = text_file.readlines()

with open("/workspaces/python/CH07/names.txt", "r") as text_file:
    names = [name.strip() for name in text_file.readlines()]


text_file.close() # DRY = don't repeat yourself

user_name = input("Enter a name: ")

# print()
# print()
# print(type(names[0].strip()))
# print(type(user_name))
# print(user_name.strip in names)
# print()
# print()

if user_name in names:
    print(f'\n"{user_name}" is already in the database')
    gandalf.show_names()    
else:
    text_file = open("/workspaces/python/CH07/names.txt", "a")
    text_file.write(user_name + '\n')
    text_file.close()
    print(f'\n"{user_name}" has been added to the database.')
    gandalf.sort_names()
    gandalf.show_names()
