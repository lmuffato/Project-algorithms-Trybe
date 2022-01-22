def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    if set(list(first_string)).issubset(set(list(second_string))):
        return True
    return False
