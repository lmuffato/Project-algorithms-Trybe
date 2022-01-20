def is_anagram(first_string, second_string):
    ordened_first_str = order(list(first_string))
    ordened_second_str = order(list(second_string))
    if(ordened_first_str == ordened_second_str):
        return True
    return False


def order(string):
    if(len(string) <= 1):
        return string

    mid = len(string) // 2
    left = order(string[:mid])
    right = order(string[mid:])

    return merge(left, right, string)


def merge(left, right, arr_copy):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):

        if(left[left_cursor] <= right[right_cursor]):
            arr_copy[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            arr_copy[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        arr_copy[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        arr_copy[left_cursor + right_cursor] = right[right_cursor]

    return arr_copy
