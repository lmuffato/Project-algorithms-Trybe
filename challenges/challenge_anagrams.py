# https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/60672880-f607-40d3-92fc-e551b740a91f/algoritmos-de-ordenacao/fd503999-673b-443d-afb1-ffcc5d1718f4?use_case=side_bar
# utilização do mergesort - conceito de divisão e conquista.
# a ideia nesse desafio é através do algoritmo de ordenação
# verificar se as duas palavras possuem as mesmas letras.

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right, array.copy())


def merge(left, right, merged):

    left_cursor = 0
    right_cursor = 0

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


print(merge_sort([100, 4, 6, 33, 56, 67]))


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False
    if merge_sort(list(first_string)) != merge_sort(list(second_string)):
        return False
    else:
        return True
