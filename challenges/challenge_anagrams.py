def sort_string(str):
    str_list = list(str)
    swapped = True
    num_of_iterations = 0

    while swapped:
        swapped = False

        for i in range(len(str_list) - num_of_iterations - 1):
            if str_list[i] > str_list[i + 1]:
                str_list[i], str_list[i + 1] = str_list[i + 1], str_list[i]
                swapped = True
        num_of_iterations += 1

    return ''.join(str_list)


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    first_string_sorted = sort_string(first_string)
    second_string_sorted = sort_string(second_string)

    return first_string_sorted == second_string_sorted
