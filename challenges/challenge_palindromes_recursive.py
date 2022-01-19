def is_palindrome_recursive(word, low_index, high_index):
    test = []
    word_reversed = ''
    if word:
        word_test = list(word)
        for char in word_test:
            if char == word_test[high_index] and high_index != -1:
                test.append(char)
                low_index += 1
                high_index -= 1
                is_palindrome_recursive(word, low_index, high_index)
        word_reversed = "".join(test)
        if word == word_reversed:
            return True
        return False
    return False

# Source:
# sobre recursão e algoritmos (conceito de algoritmos recursivos):
# https://www.ic.unicamp.br/~ripolito/peds/mc102z/material/Recursividade.PDF
