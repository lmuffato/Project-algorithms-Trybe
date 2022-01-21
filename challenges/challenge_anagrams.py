def selection_sort(word):
    array = list(word)
    for index in range(len(array)):
        minimum = index
        for x in range(index + 1, len(array)):
            if array[x] < array[minimum]:
                minimum = x
        array[minimum], array[index] = array[index], array[minimum]

    return array

def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if not first_string or not second_string:
        return False
    if len(first_string) != len(second_string):
        return False
    if selection_sort(first_string) == selection_sort(second_string):
        return True
    if selection_sort(first_string) != selection_sort(second_string):
        return False
