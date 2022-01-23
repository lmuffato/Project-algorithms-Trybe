def merge_sort(string):
    list_change = list(string)
    if len(list_change) <= 1:
        return list_change

    mid = len(list_change) // 2
    left, right = merge_sort(list_change[:mid]), merge_sort(list_change[mid:])

    return merge(left, right, list_change.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if merge_sort(first_string) == merge_sort(second_string):
        return True
    else:
        return False
