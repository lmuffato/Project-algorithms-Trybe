# Função retirada do course
# Bloco 35.2
# Algoritmos de ordenação - Merge sort

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

    first_string_ordened = merge_sort(list(first_string))
    second_string_ordened = merge_sort(list(second_string))

    pos = 0
    iguais = True

    while pos < len(first_string_ordened) and iguais:
        if first_string_ordened[pos] == second_string_ordened[pos]:
            pos += 1
        else:
            iguais = False

    return iguais
