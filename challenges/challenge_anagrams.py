def sort_strings(string):
    string_list = []
    string_list[:0] = string

    for index1 in range(len(string_list) - 1):
        for index2 in range(index1 + 1, len(string_list)):
            if string_list[index1] > string_list[index2]:
                temp_list = string_list[index1]
                string_list[index1] = string_list[index2]
                string_list[index2] = temp_list

    return string_list


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    sort_one = sort_strings(first_string)
    sort_two = sort_strings(second_string)

    if ''.join(map(str, sort_one)) == ''.join(map(str, sort_two)):
        return True
    else:
        return False

# Utilização da função map através do link:
# https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python

# Entendimento do Bubble Sort através do link:
# https://stackoverflow.com/questions/13101468/python-how-to-sort-the-alphabet-in-a-list-without-sorted-functions
