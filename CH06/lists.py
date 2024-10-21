def demo01():
    grocery_list = ["potatoes", "cereal", "bagels"]
    # grocery_list = [10, 2000, 30]
    # grocery_list = [["gold potatoes", "salt potatoes", "sweet potatoes"], ["Reese's", "Wheatabix", "Captain Crunch"]]

    print(grocery_list)
    # print(grocery_list[0])
    # print(grocery_list[1][2]) 

    for grocery_item in grocery_list:
        print(f'Don\'t forget the {grocery_item} please!')

def demo02():
    print(len('THIS IS A TEST'))
    list_of_numbers = [2, 4, 6, 10]
    print(f'[-1]: {list_of_numbers[-1]}')
    print(list_of_numbers)
    print(len(list_of_numbers)) #length
    list_of_numbers.insert(3, 8)
    print(list_of_numbers)
    print(len(list_of_numbers))
    
    print()
    
    print(f'First: {list_of_numbers[0]}') # get the FIRST value

    print(f'Last: {list_of_numbers[len(list_of_numbers) - 1]}') # get the LAST value
    print(f'Last: {list_of_numbers[-1]}')
    
    print()
    
    print(list_of_numbers)
    list_of_numbers.pop(1)
    list_of_numbers.pop()
    print(list_of_numbers)


def demo03():
    list_of_words = []
    list_of_words.append(['a', 'b', 'c'])
    print(list_of_words)
    list_of_words.append(['d', 'e', 'f'])
    print(list_of_words)


def demo04():
    my_list = ["Yogi", "Maggie", "Quinnie", "BB-8"]

    # for item in my_list:
    #     print(f'{item}')
    
    for index, item in enumerate(my_list):
        print(f'{index+1}. {item}')

    # my_list.remove("Maggie")
    print()

    item_number_to_remove = int(input('Enter the number of the item to remove: '))
    my_list.pop(item_number_to_remove-1)

    for index, item in enumerate(my_list):
        print(f'{index+1}. {item}')    





# demo01()
# demo02()
# demo03()
demo04()