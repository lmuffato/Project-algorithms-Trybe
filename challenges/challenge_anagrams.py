def quicksort(array_letters, low, high):

    if len(array_letters) == 1:
        return "".join(array_letters)

    if low < high:
        partition_index = partition(array_letters, low, high)

        quicksort(array_letters, low, partition_index - 1)
        quicksort(array_letters, partition_index + 1, high)


def partition(array_letters, low, high):
    i = low - 1
    pivot = array_letters[high]
    for j in range(low, high):

        if array_letters[j] <= pivot:
            i = i + 1
            array_letters[i], array_letters[j] = (
                array_letters[j], array_letters[i]
            )

    array_letters[i + 1], array_letters[high] = (
            array_letters[high], array_letters[i + 1]
        )
    return i + 1


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    first_string_list = list(first_string)
    second_string_list = list(second_string)

    quicksort(first_string_list, 0, len(first_string_list) - 1)
    quicksort(second_string_list, 0, len(second_string_list) - 1)

    if first_string_list == second_string_list:
        return True

    return False
