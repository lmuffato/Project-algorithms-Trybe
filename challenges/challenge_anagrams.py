def is_anagram(first_string, second_string):
    counter = {}
    for c in first_string:
        try:
            counter[c] += 1
        except KeyError:
            counter[c] = 1
    for c in second_string:
        try:
            counter[c] -= 1
        except KeyError:
            return False
    for value in counter.values():
        if value != 0:
            return False
    return True
