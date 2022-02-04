# Solução encontrada no endereço
# https://stackoverflow.com/questions/48217471/is-it-possible-to-check-for-anagram-without-using-sorted-or-dictionary-that-pe


def build_counts(string):
    char = {}
    for c in string:
        char[c] = char.setdefault(c, 0) + 1

    return char


def is_anagram(first_string, second_string):
    first = build_counts(first_string)
    second = build_counts(second_string)

    return first == second
