def sort_string(string):
    new_string = list(string)
    for i in range(len(string)):
        cur_value = string[i]
        cur_position = i
        while cur_position > 0 and new_string[cur_position - 1] > cur_value:
            new_string[cur_position] = new_string[cur_position - 1]
            cur_position = cur_position - 1

        new_string[cur_position] = cur_value
    return new_string


def is_anagram(first_string, second_string):
    """ Faça o código aqui. !!"""
    if len(first_string) != len(second_string):
        return False
    else:
        first_string = sort_string(first_string)
        second_string = sort_string(second_string)

    if first_string == second_string:
        return True
    else:
        return False
