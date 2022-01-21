def get_lowest(arr):
    lowest_num = arr[0]
    for i in range(len(arr)):
        if lowest_num > arr[i]:
            lowest_num = arr[i]
    return lowest_num


def sort_list(arr):
    arr_it = list(arr)
    new_arr = []
    while len(new_arr) != len(arr):
        lowest = get_lowest(arr_it)
        new_arr.append(lowest)
        arr_it.remove(lowest)
    return "".join(new_arr)


def is_anagram(first_string, second_string):
    first = sort_list(first_string)
    second = sort_list(second_string)
    if first == second:
        return True
    return False


"""
https://www.geeksforgeeks.org/python-program-to-sort-a-string/
foi usado a seguinte referência
"""
