restaurant = 'Krusty Krabs'

def sponged_words(word):
    length_of_word = len(word)
    # new_list = ['this', 'is', 'a']
    # print('LEN' , len(new_list))
    # print(length_of_word)
    sponged_word = ''

    for x in range(0, length_of_word):
        # print(x)
        # print(word[x].upper())
        # word = word[x].upper()
        
        if x % 2 == 0:
            sponged_word += word[x].upper()
        else:
            sponged_word += word[x].lower()


    return sponged_word