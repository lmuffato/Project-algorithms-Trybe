def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == "" or second_string == "":
        return False
    if len(first_string) != len(second_string):
        return False
    for first in first_string:
        if first not in second_string:
            return False
        else:
            second_string = second_string.replace(first, "")

    return True


# vqv
first_string = "pedrra"
second_string = "pedraaaaaaaa"

teste = is_anagram(first_string, second_string)
print(teste)
