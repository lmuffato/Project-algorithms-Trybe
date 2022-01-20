def sortList(array):
    length = len(array)

    for i in range(length - 1):
        min_index = i

        for j in range(i + 1, length - 1):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]


def is_anagram(first_string, second_string):
    replaced_one = first_string.replace(' ', '')
    replaced_two = second_string.replace(' ', '')
    sorted_one = sortList(list(replaced_one))
    sorted_two = sortList(list(replaced_two))
    print(sorted_one)
    print(sorted_two)
    # if sorted_one == sorted_two:
    #     return True
    # else:
    #     return False
