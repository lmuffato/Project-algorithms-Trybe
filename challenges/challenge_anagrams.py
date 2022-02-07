def is_anagram(first_string, second_string):

    if not first_string or not second_string:
        return False

    for letter in first_string:
        # print('letter', letter)
        counter_first = first_string.count(letter)
        counter_second = second_string.count(letter)
        # print('counter_first', counter_first)
        # print('counter_second', counter_second)

        if counter_first != counter_second:
            return False
    
    return True
