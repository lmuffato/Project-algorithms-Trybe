def sort_string(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left, right = sort_string(array[:mid]), sort_string(array[mid:])

    return order(left, right, array.copy())


def order(left, right, merged):
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
    firstArray = list(first_string.replace(" ", ""))
    secondArray = list(second_string.replace(" ", ""))
    firstWord = sort_string(firstArray)
    secondWord = sort_string(secondArray)

    return "".join(firstWord) == "".join(secondWord)
