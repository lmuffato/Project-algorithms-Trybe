def selection_sort(word):
    arr = list(word)
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    if len(first_string) != len(second_string):
        return False
    if selection_sort(first_string) == selection_sort(second_string):
        return True
    if selection_sort(first_string) != selection_sort(second_string):
        return False
