def letter_counter(string):
    dict = {}
    for letter in string:
        dict[letter] = dict.setdefault(letter, 0) + 1
    return dict


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    strOne = letter_counter(first_string)
    strTwo = letter_counter(second_string)
    return strOne == strTwo
