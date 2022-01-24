def reorder(word):
    listed = list(word)
    swaped = True
    num_of_iterations = 0
    while(swaped):
        swaped = False
        for i in range(len(listed) - num_of_iterations - 1):
            if listed[i] > listed[i + 1]:
                listed[i], listed[i + 1] = listed[i + 1], listed[i]
                swaped = True
        num_of_iterations += 1
    return "".join(listed)


def is_anagram(first_string, second_string):
    if (reorder(first_string) == reorder(second_string)):
        return True
    return False
