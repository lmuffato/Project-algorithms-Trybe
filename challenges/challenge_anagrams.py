# https://panda.ime.usp.br/panda/static/pythonds_pt/02-AnaliseDeAlgoritmos/ExemploDeDeteccaoDeAnagramas.html

def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    letters1 = [0]*26
    letters2 = [0]*26

    for i in range(len(first_string)):
        position = ord(first_string[i]) - ord('a')
        letters1[position] = letters1[position] + 1
        print('c1:', letters1)

    for i in range(len(second_string)):
        position = ord(second_string[i]) - ord('a')
        print('pos2:', position)
        letters2[position] = letters2[position] + 1
        print('c2:', letters2)

    j = 0
    comparador = True
    while j < 26 and comparador:
        if letters1[j] == letters2[j]:
            j = j + 1
        else:
            comparador = False

    return comparador
