# usada a estrutura de ordenação do course

def sort(word, low, high):
    if len(word) == 1:
        return word
    if low < high:
        partition_index = partition(word, low, high)
        sort(word, low, partition_index - 1)
        sort(word, partition_index + 1, high)


def partition(word, low, high):
    i = low - 1
    pivot = word[high]
    for j in range(low, high):
        if word[j] <= pivot:
            i = i + 1
            word[i], word[j] = word[j], word[i]
    word[i + 1], word[high] = word[high], word[i + 1]
    return i + 1


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    if len(first_string) != len(second_string):
        return False
    first_string = sort(first_string.split(), 0, len(first_string) - 1)
    second_string = sort(second_string.split(), 0, len(second_string) - 1)
    if first_string == second_string:
        return True
    else:
        return False
