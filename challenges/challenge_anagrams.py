def combine(numbers, start, aux):
    for i in range(len(aux)):
        numbers[start + i] = aux[i]


def merge_sort(numbers, start, end):
    if start < end:
        middle = (start + end) // 2
        merge_sort(numbers, start, middle)
        merge_sort(numbers, middle + 1, end)
        combine(numbers, start, merge(numbers, start, middle, end))


def merge(numbers, start, middle, end):
    start1 = start
    start2 = middle + 1
    aux = []

    while ((start1 <= middle) and (start2 <= end)):
        if (numbers[start1] < numbers[start2]):
            aux.append(numbers[start1])
            start1 += 1
        else:
            aux.append(numbers[start2])
            start2 += 1

    while (start1 <= middle):
        aux.append(numbers[start1])
        start1 += 1
    while (start2 <= end):
        aux.append(numbers[start2])
        start2 += 1
    return aux


def order_string(string):
    string_array = list(string)
    start = 0
    end = len(string_array) - 1

    merge_sort(string_array, start, end)
    ordered = ''.join(string_array)

    return ordered.lower()


def is_anagram(first_string, second_string):
    first_ordered = order_string(first_string)
    second_ordered = order_string(second_string)
    if (first_ordered == second_ordered):
        return True
    return False

# REF
# https://github.com/samuelmmjr/Cross-Comerce-Challenge/blob/main/utils/orderNumbers.js
#
