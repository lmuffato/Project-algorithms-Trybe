def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):

        if array[j] <= pivot:

            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def quicksort(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)

        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_string = [*first_string]
    second_string = [*second_string]

    quicksort(first_string, 0, len(first_string) - 1)
    sorted_first_string = "".join(first_string)

    quicksort(second_string, 0, len(second_string) - 1)
    sorted_second_string = "".join(second_string)

    return sorted_first_string == sorted_second_string
