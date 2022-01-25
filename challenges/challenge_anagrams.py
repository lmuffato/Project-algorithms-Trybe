# https://realpython.com/python-enumerate/
# http://devfuria.com.br/python/built-in-enumerate/


def letters(first_string, second_string):
    position = []
    for letter_first_string in first_string:
        # A função enumarate() retorna um objeto iterável.

        for current_index, letter_second_string in enumerate(second_string):
            if (letter_first_string == letter_second_string) and (
                current_index not in position
            ):
                position.append(current_index)
                break
    if len(position) == len(first_string):
        return True
    return False


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False
    return letters(first_string, second_string)


is_anagram("abcde", "edcba")
