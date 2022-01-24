def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    if (first_string[:2] == second_string[:2]
            and first_string[-2:] == second_string[-2:]):
        return True
    inverse_first = (first_string[-3:-1][1], first_string[-3:-1][0])
    inverse_second = (second_string[-3:-1][0], second_string[-3:-1][1])

    if inverse_first != inverse_second:
        return False

    return True
