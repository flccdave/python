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
    
    print()
    
    print(list_of_numbers)
    list_of_numbers.pop(1)
    list_of_numbers.pop()
    print(list_of_numbers)


demo02()