def is_anagram(first_string, second_string):
    """ Faça o código aqui. """

    umalista1 = list(first_string)
    umalista2 = list(second_string)

    umalista1.sort()
    umalista2.sort()

    pos = 0
    iguais = True

    while pos < len(first_string) and iguais:
        if umalista1[pos] == umalista2[pos]:
            pos = pos + 1
        else:
            iguais = False

    return iguais


is_anagram("abcde", "edcba")
