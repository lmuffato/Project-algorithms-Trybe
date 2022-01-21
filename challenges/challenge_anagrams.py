# https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/118f97fe-3cc2-4468-a14c-ca8c341cadc2/algoritmos-de-ordenacao/a3ba0c1f-1835-4956-ba4a-42f376d3d555?use_case=side_bar

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


# https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/118f97fe-3cc2-4468-a14c-ca8c341cadc2/algoritmos-de-ordenacao/a3ba0c1f-1835-4956-ba4a-42f376d3d555?use_case=side_bar

def is_anagram(first_string, second_string):
    first_string_arr = [i for i in first_string]
    sorted = merge_sort(first_string_arr)
    second_string_arr = [i for i in second_string]
    sorted_2 = merge_sort(second_string_arr)
    if sorted == sorted_2:
        return True
    return False
