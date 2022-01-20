# Também funciona, mas leva um pouco mais de tempo para executar
def is_palindrome_recursive_vsbeta(word, low_index, high_index):
    test = []
    word_reversed = ''
    if word:
        word_test = list(word)
        for char in word:
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
# sobre estrutura lógica de algoritmos de palindromos:
# https://www.mygreatlearning.com/blog/palindrome-in-python/


def is_palindrome_recursive(word, low_index, high_index):
    if word:
        if word[low_index] != word[high_index]:
            return False
        elif (low_index - high_index) > -1:
            return True
        else:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False
