def is_anagram(first_string, second_string):
    # go
    first_ordered = merge_and_sort(first_string)
    second_ordered = merge_and_sort(second_string)
    return first_ordered == second_ordered


def merge_and_sort(str):
    if len(str) <= 1:
        return str

    middle = len(str) // 2

    left, right = merge_and_sort(str[:middle]), merge_and_sort(str[middle:])
    new_str = list(str)
    return "".join(merge(left, right, new_str))


def merge(left, right, str):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            str[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            str[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        str[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        str[left_cursor + right_cursor] = right[right_cursor]

    return str
