# https://www.delftstack.com/pt/howto/python/quicksort-python/

def sort_string(string):
    left = []
    equal = []
    greater = []

    if len(string) <= 1:
        return string

    pivot = string[0]

    for char in string:
        if char < pivot:
            left.append(char)
        elif char > pivot:
            greater.append(char)
        else:
            equal.append(char)
    return sort_string(left) + equal + sort_string(greater)

def is_anagram(first_string, second_string):
    if len(second_string) == 0 or len(first_string) == 0:
        return False
    elif sort_string(first_string) == sort_string(second_string):
        return True
    else:
        return False
