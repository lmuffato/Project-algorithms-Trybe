# Algoritmo Merge-Sort
# Retirado de: https://app.betrybe.com/course/calendar/computer-science
# - Módulo de Ciência da Computação
# - Bloco 35.3: Algoritmos de ordenação e busca


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right, array)


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
    first_str = ''.join(merge_sort(list(first_string)))
    sec_str = ''.join(merge_sort(list(second_string)))

    if first_str != sec_str:
        return False
    return True
