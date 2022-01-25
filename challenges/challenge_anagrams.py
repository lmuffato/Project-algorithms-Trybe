def is_anagram(first_string, second_string):
    if (
        not(first_string and second_string)
        or (len(first_string) != len(second_string))
    ):
        return False
    return True
