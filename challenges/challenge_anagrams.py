# Quick Sort https://www.geeksforgeeks.org/quick-sort/?ref=lbp
# partition
def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:

        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if(start < end):
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end

# The main function that implements QuickSort


def quick(start, end, array):
    if (start < end):
        p = partition(start, end, array)
        quick(start, p - 1, array)
        quick(p + 1, end, array)


# selection sort
def selection(str):
    for i in range(len(str)):
        min = i
        for j in range(i + 1, len(str)):
            if str[j] < str[min]:
                min = j

        str[min], str[i] = str[i], str[min]

    return str


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    fst_li = list(first_string)
    quick(0, len(first_string) - 1, fst_li)
    snd_li = list(second_string)
    quick(0, len(second_string) - 1, snd_li)

    if fst_li == snd_li:
        return True

    if len(fst_li) != len(snd_li) or len(fst_li) > 0 or len(snd_li) > 0:
        return False
