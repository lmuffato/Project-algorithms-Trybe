def sorted_by_hand(string):
    word_list = list(string)
    for index_1 in range(len(word_list)):
        minimum = index_1
        for index_2 in range(index_1 + 1, len(word_list)):
            if word_list[index_2] < word_list[minimum]:
                minimum = index_2
        word_list[minimum], word_list[index_1] = word_list[index_1], word_list[minimum]

    return word_list


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    if len(first_string) != len(second_string):
        return False
    if sorted_by_hand(first_string) == sorted_by_hand(second_string):
        return True
    if sorted_by_hand(first_string) != sorted_by_hand(second_string):
        return False

# https://www.youtube.com/watch?v=t18nWQW8Hbc
# https://stackoverflow.com/questions/48217471/is-it-possible-to-check-for-anagram-without-using-sorted-or-dictionary-that-pe