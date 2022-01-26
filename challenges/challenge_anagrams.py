def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    elif second_string[::-1] == first_string:
        return True
    return False
