def word_count(words):
    #make word count dictionary
    word_count_dict = {}
    #break the string into a list of words
    word_list = words.split()
    #loop through each word and add it to a dictionary, advance word count
    for word in word_list:
        try:
            word_count_dict[word] += 1
        except KeyError:
            word_count_dict[word] = 1

    return word_count_dict

