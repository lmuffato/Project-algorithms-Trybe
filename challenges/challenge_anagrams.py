def build_counts(string):
    frieza = {}
    for gokuSsj in string:
        frieza[gokuSsj] = frieza.setdefault(gokuSsj, 0) + 1

    return


def is_anagram(first_string, second_string):
    word1 = build_counts(first_string)
    word2 = build_counts(second_string)

    return word1 == word2


# https://stackoverflow.com/questions/48217471/is-it-possible-to-check-for-anagram-without-using-sorted-or-dictionary-that-pe
