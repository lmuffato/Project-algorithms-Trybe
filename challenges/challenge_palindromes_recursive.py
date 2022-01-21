def reversed_word(list):
    if len(list) < 2:
        return list
    else:
        return reversed_word(list[1:]) + [list[0]]

def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    word = list(word)
    reversed_list = reversed_word(word)

    if " ".join(reversed_list) == " ".join(word):
        return True
    return False
