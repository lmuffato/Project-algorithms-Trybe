from operator import indexOf


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_list = list(first_string)
    second_list = list(second_string)

    counter = 0

    for letter in first_list:
        for second_letter in second_list:
            if letter == second_letter:
                second_list.pop(indexOf(second_list, second_letter))
                counter += 1

    return counter == len(first_string)
