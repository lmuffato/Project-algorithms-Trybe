# def is_anagram(first_string, second_string):
#     if not first_string or second_string:
#         return False

#     caracters_list = list(second_string)
#     position_string_1 = 0
#     is_an_anagram = True

#     while position_string_1 < len(first_string) and is_an_anagram:
#         position_string_2 = 0
#         found = False
#         while position_string_2 < len(caracters_list) and not found:
#             if first_string[position_string_1] == caracters_list[position_string_2]:
#                 found = True
#             else:
#                 position_string_2 += 1

#         if found:
#             caracters_list[position_string_2] = None
#         else:
#             is_an_anagram = False

#         position_string_1 += 1

#     return is_an_anagram


# REF: https://github.com/tryber/sd-010-a-project-algorithms/pull/62/files
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right, array.copy())


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
    if not first_string or not second_string:
        return False
    word_1 = merge_sort(list(first_string))
    word_2 = merge_sort(list(second_string))
    return word_1 == word_2
