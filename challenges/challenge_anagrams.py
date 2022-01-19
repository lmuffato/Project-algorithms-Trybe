def found_letters(first_string, second_string):
    letter_found_position = []
    for i in first_string:
        for j_index, j in enumerate(second_string):
            if (i == j) and (j_index not in letter_found_position):
                letter_found_position.append(j_index)
                break
    if len(letter_found_position) == len(first_string):
        return True
    return False


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    return found_letters(first_string, second_string)
