# Anotações para referências futuras --
# Duas abordagens para resolver esse problema:

# --> Abordagem 1 - usando um algoritmo de ordenação e algoritmo de recursão:
# Transformar as duas strings em duas listas ordenada em ordem alfabética

#  Funcionamento do quicksort:
# Se não for passado o parâmetro lista, retorna um array vazio.
#  continua: retornando o item para cada item na lista,
# Se há retorna o item para cada item na lista,
# excluído o primeiro elemento da lista, chama o quicksort se o item for menor
# que o primeiro elemento.
#  Adiciona-se novamente o primeiro item da lista.
# Depois, excluído o primeiro elemento da lista, chama novamente o quicksort
#  se o item for >= ao que está no índice zero do array


def quicksort(lista_or_str):
    if not lista_or_str:
        return []
    return (
        quicksort(
            [item for item in lista_or_str[1:] if item < lista_or_str[0]])
        + [lista_or_str[0]] +
        quicksort(
            [item for item in lista_or_str[1:] if item >= lista_or_str[0]]))
# Source - algoritmo quicksort:
# https://www.delftstack.com/pt/howto/python/sort-list-alphabetically/

# Depois iterar sobre a lista e verificar se todas as posições
# do array possuem valores iguais.
# E se tiverem o mesmo tamanho é porque são anagramas.
# Se tiver alguma letra diferente é false


def is_anagram(first_string, second_string):
    if first_string and second_string:
        if len(first_string) == len(second_string):
            if quicksort(first_string) == quicksort(second_string):
                return True
            return False
        return False
    return False
