def sort_names():

    # Open the file for READING
    text_file = open("/workspaces/python/CH07/names.txt", "r")

    # Read the file into a LIST called `names`
    names = text_file.readlines()

    # Close the file
    text_file.close()

    # Sorted the names
    names.sort()

    # Open the file for WRITING (overwriting)
    text_file = open("/workspaces/python/CH07/names.txt", "w")

    # Loop through the list and, one by one, write each name
    for name in names:
        text_file.write(name)

    # Close the file
    text_file.close()

def show_names():
    # Open the file for READING
    text_file = open("/workspaces/python/CH07/names.txt", "r")

    file_contents = text_file.read()
    print()
    print(file_contents)