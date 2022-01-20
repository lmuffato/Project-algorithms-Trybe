def sort_array(param):
    array = list(param)
    for i in range(len(array)):
        minimo = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimo]:
                minimo = j
        array[minimo], array[i] = array[i], array[minimo]
    return "".join(array)

def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == "" or second_string == "":
        return False
    elif len(first_string) != len(second_string):
        return False
    return sort_array(first_string) == sort_array(second_string)