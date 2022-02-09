def mergeSort(list):
    # https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html

    if len(list) > 1:
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i = i+1
            else:
                list[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            list[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            list[k] = righthalf[j]
            j = j+1
            k = k+1

    return list


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    if len(first_string) != len(second_string):
        return False

    first_string = mergeSort(list(first_string))
    second_string = mergeSort(list(second_string))

    return ''.join(first_string) == ''.join(second_string)
