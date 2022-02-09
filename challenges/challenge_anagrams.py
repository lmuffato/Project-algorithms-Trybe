def sort_string(list):
    for index in range(1, len(list)):
        current_char = list[index]
        i = index - 1

        while i >= 0 and current_char < list[i]:
            list[i + 1] = list[i]
            i -= 1

        list[i + 1] = current_char

    return list


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    if len(first_string) != len(second_string):
        return False

    first_string = sort_string(list(first_string))
    second_string = sort_string(list(second_string))

    return ''.join(first_string) == ''.join(second_string)
