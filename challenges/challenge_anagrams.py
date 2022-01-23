def is_anagram(first_string, second_string):
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    elif len(first_string) != len(second_string):
        return False
