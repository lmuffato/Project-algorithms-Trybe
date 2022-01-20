# Para referências futuras, outras formas de estruturar o algoritmo


def is_palindrome_vsbeta(word, low_index, high_index):
    test = []
    word_reversed = ''
    if word:
        word_test = list(word)
        for char in word:
            if char == word_test[high_index] and high_index != -1:
                test.append(char)
                low_index += 1
                high_index -= 1
        word_reversed = "".join(test)
        if word == word_reversed:
            return True
        return False
    return False


def is_palindrome_iterative_vsbeta(word):
    key = len(word) - 1
    reverse_word = []
    if key < 0:
        return False
    while key > -1:
        reverse_word.append(word[key])
        key = key - 1
    return word == ''.join(reverse_word)


def is_palindrome_iterative(word):
    low_index = 0
    high_index = len(word) - 1
    word_rev = ''
    if word:
        if word[low_index] != word[high_index]:
            return False
        elif (low_index - high_index) > -1:
            return True
        while high_index > -1:
            word_rev += word[high_index]
            high_index -= 1
        return word == word_rev
    return False
