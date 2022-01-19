# me baseei na seguinte discussão do stack overflow:
# https://stackoverflow.com/questions/13101468/python-how-to-sort-the-alphabet-in-a-list-without-sorted-functions
def quicksort(lst):
    return (quicksort([letter for letter in lst[1:] if letter < lst[0]])
            + [lst[0]] +
            quicksort([letter for letter in lst[1:] if letter >= lst[0]]))


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first_list = quicksort(list(first_string))
    second_list = quicksort(list(second_string))
    return first_list == second_list
