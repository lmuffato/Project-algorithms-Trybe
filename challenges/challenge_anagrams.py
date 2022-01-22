def string_sort(string):
    array = list(string)

    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[minimum], array[i] = array[i], array[minimum]

    return "".join(array)


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    first_string_sorted = list(first_string)
    second_string_sorted = list(second_string)

    if first_string_sorted == second_string_sorted:
        return True

    return False
