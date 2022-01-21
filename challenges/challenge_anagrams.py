def sortList(array):
    length = len(array)

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length - 1):
            if ord(array[j]) < ord(array[min_index]):
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


def is_anagram(first_string, second_string):
    sorted_one = sortList(list(first_string))
    sorted_two = sortList(list(second_string))
    if sorted_one == sorted_two:
        return True
    else:
        return False
