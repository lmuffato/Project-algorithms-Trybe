def sort(array):
    for index in range(len(array)):
        minimum = index
        for index2 in range(index + 1, len(array)):
            if array[index2] < array[minimum]:
                minimum = index2
                array[minimum], array[index] = (
                    array[index],
                    array[minimum],
                )
    return array


def insertion_sort(array):
    for i in range(len(array)):
        current_value = array[i]
        current_position = i

        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):

            array[current_position] = array[current_position - 1]
            current_position = current_position - 1

        array[current_position] = current_value
    return array


def is_anagram(first_string, second_string):
    if first_string == "":
        return False
    if second_string == "":
        return False
    first_string_list = list(first_string)
    second_string_list = list(second_string)

    if insertion_sort(first_string_list) == insertion_sort(second_string_list):
        return True
    else:
        return False


print(is_anagram("amor", "roma"))
