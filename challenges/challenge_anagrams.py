# O algoritmo de ordenação usado no método sort_string é o Quick sort.
# Nele, determinamos um pivô e separamos todos os elementos
#  maiores e menores que ele.
# Assim, obtemos a quantidade exata de elementos maiores e menores que o pivô,
# o que determina a sua posição correta.
# A partir daí, seguimos a mesma lógica e aplicamos a recursividade
# nas subpartes maior e menor para aplicar o mesmo oredenamento,
# até não haver mais elementos nessas subpartes.
# https://www.delftstack.com/pt/howto/python/quicksort-python/

def sort_string(string):
    left = []
    equal = []
    greater = []

    if len(string) < 1:
        return string

    pivot = string[0]

    for char in string:
        if char < pivot:
            left.append(char)

        elif char > pivot:
            greater.append(char)

        else:
            equal.append(char)

    return sort_string(left) + equal + sort_string(greater)


def is_anagram(first_string, second_string):
    if len(second_string) == 0 or len(first_string) == 0:
        return False
    elif sort_string(first_string) == sort_string(second_string):
        return True
    else:
        return False


# print(is_anagram("amora", "amaro"))
# print(sort_string("orar"))
