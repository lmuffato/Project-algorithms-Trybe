# Tentativa #1 - Passando somente 2/4 dos testes

def is_anagram(first_string, second_string):
    if (not first_string or not second_string):
        return False

    f_string = list(first_string)
    s_string = list(second_string)
    result = ''

    for index in range(len(f_string)):
        if (s_string[index] in f_string):
            result = 'v'

    if (result != 'v'):
        return False

    return True
