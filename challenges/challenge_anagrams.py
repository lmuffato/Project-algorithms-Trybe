def sort_strings(string):
    string_list = []
    string_list[:0] = string

    for index1 in range(len(string_list) - 1):
        for index2 in range(index1 + 1, len(string_list)):
            if string_list[index1] > string_list[index2]:
                temp_list = string_list[index1]
                string_list[index1] = string_list[index2]
                string_list[index2] = temp_list

    return print(string_list)


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    return True
