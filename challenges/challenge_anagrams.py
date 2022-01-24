def sort_str(_str):
    str = list(_str)

    for anterior in range(len(str)):
        index = anterior

        for proximo in range(anterior + 1, len(str)):
            if str[proximo] < str[index]:
                index = proximo

        str[anterior], str[index] = str[index], str[anterior]

    return "".join(str)


def is_anagram(first_string, second_string):
    if (
        first_string == ""
        or second_string == ""
        or len(first_string) != len(second_string)
    ):
        return False

    return sort_str(first_string) == sort_str(second_string)
