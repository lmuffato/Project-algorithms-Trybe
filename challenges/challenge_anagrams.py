# https://app.betrybe.com/course/computer-science/algoritmos/algoritmos
# -de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/
# 60672880-f607-40d3-92fc-e551b740a91f/algoritmos-de-ordenacao/fd503999
# -673b-443d-afb1-ffcc5d1718f4?use_case=side_bar
def insertion_sort(array):
    # itera sobre cada valor do array
    for i in range(len(array)):
        current_value = array[i]
        current_position = i
        # enquanto o valor da posição for menor que os elementos a sua esquerda
        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):
            # move as posições para a direita
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
        # colocamos o elemento em sua nova posição
        array[current_position] = current_value
    return array


# https://stackoverflow.com/questions/9833392/break-string-into-list-of-characters-in-python
def is_anagram(first_string, second_string):
    first_sorted = insertion_sort(list(first_string))
    second_sorted = insertion_sort(list(second_string))
    if len(first_sorted) == len(second_sorted):
        for i in range(0, len(first_string) - 1):
            if first_sorted[i] != second_sorted[2]:
                return False
        return True
    return False
