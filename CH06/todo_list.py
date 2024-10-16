def display_menu():
    print('TASKMASTER 2000')
    print('  1. Add a task')
    print('  2. Remove task')
    print('  3. Edit a task')
    print('  4. View tasks')
    print('  5. Quit')
    print()

def main():
    
    task_list = ["1. ABC", "2. DEF", "3. GHI"]
    print(task_list)
    # print(type(task_list))

    user_choice = None

    while user_choice != 5:

        display_menu()
        user_choice = int(input('Enter your choice: '))

        if user_choice == 1:
            task = input('Enter task: ')
            task_list.append(f'{len(task_list)+1}. {task}')
            # task_list.insert(0, task)
            print(task_list)
        elif user_choice == 2:
            task = input('Enter task to remove: ')
            task_list.remove(task)
            # task_number = int(input('Task number to remove: '))
            # task_list.pop(task_number - 1)
            # print(task_list)
        elif user_choice == 3:
            print('STUB CODE for "EDIT A TASK"')
        elif user_choice == 4:
            for task in task_list:
                print(task)
        elif user_choice == 5:
            print('Thank you for using TaskMaster 2000')
        else:
            print('ERROR! Pick a valid choice!')




main()

print('\n\nGAME OVER MAN!!!!!')

