def sort_string(string):
    text = ''
    while len(string) > 0:
        # monta a string com a menor letra da palavra
        text += min(string)
        # remove a menor letra da palavra original (apenas uma vez)
        string = string.replace(min(string), '', 1)
    return text


def is_anagram(first_string, second_string):
    # no caso dos parametros não existirem
    if not first_string or not first_string:
        return False

    if len(first_string) != len(second_string):
        return False

    string_sorted_01 = sort_string(first_string)
    string_sorted_02 = sort_string(second_string)

    index = 0

    while index < len(string_sorted_01):
        if string_sorted_01[index] != string_sorted_02[index]:
            return False
        index += 1
    return True


# Teste manual
# print(is_anagram('pedrra', 'perrda'))


# Teste automatizado
# python3 -m pytest tests/test_anagrams.py
