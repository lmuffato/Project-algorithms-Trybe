def letter_counter(string):
    dict = {}
    for letter in string:
        dict[letter] = dict.setdefault(letter, 0) + 1
    return dict


def is_anagram(first_string, second_string):
    if (first_string or second_string) == '':
        return False
    else:
        str1 = letter_counter(first_string)
        str2 = letter_counter(second_string)
        return str1 == str2
