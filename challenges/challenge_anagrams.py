def is_anagram(first_string, second_string):
    counter = {}
    loop1(first_string, counter)
    if not loop2(second_string, counter):
        return False
    return loop3(counter)


def loop1(first_string, counter):
    for c in first_string:
        try:
            counter[c] += 1
        except KeyError:
            counter[c] = 1


def loop2(second_string, counter):
    for c in second_string:
        try:
            counter[c] -= 1
        except KeyError:
            return False
    return True


def loop3(counter):
    for value in counter.values():
        if value != 0:
            return False
    return True
