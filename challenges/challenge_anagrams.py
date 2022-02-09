def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    for letter in first_string:
        count_first = first_string.count(letter)
        count_second = second_string.count(letter)
        if count_first != count_second:
            return False

    return True
