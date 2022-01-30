def partition(word, low, high):
    center = (high - low) >> 1
    pivot = word[low + center]
    i = low
    j = high
    while True:
        while word[i] < pivot:
            i = i + 1
        while word[j] > pivot:
            j = j - 1
        if i >= j:
            break
        word[i], word[j] = word[j], word[i]
        i = i + 1
        j = j - 1
    word[i], word[high] = word[high], word[i]
    return i    


def quick_sort(word, low, high):
    if low < high:
        pivot = partition(word, low, high)
        quick_sort(word, low, pivot-1)
        quick_sort(word, pivot, high)


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first_string = [*first_string]
    second_string = [*second_string]
    quick_sort(first_string, 0, len(first_string) - 1)
    quick_sort(second_string, 0, len(second_string) - 1)
    return first_string == second_string