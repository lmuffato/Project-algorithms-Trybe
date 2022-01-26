def found_string(string):
    list_str = list(string)

    for i in range(len(list_str)):
        position = i

        for j in range(i + 1, len(list_str)):
            if list_str[j] < list_str[position]:
                position = j
        list_str[position], list_str[i] = list_str[i], list_str[position]

    return "".join(list_str)


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    first_str_found = list(first_string)
    second_str_found = list(second_string)

    if first_str_found == second_str_found:
        return True

    return False
# Solução realizado com auxilio do André Barroso T10A
