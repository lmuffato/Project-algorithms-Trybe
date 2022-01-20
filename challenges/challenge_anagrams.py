from string import ascii_lowercase as letters

# Source:
# https://educacao.uol.com.br/disciplinas/matematica/numeros-primos-veja-algoritmo-para-encontra-los.htm

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
# do array possuem valores iguais
# e tiverem o mesmo tamanho, é porque são anagramas
# Se tiver alguma letra diferente é false

# def is_anagram(first_string, second_string):
#     if first_string and second_string:
#         if len(first_string) == len(second_string):
#               if quicksort(first_string) == quicksort(second_string):
#                   return True
#               return False
#         return False
#     return False

# --> Abordagem 2 - utilizando fórmula matemática para números primos:
    # Ter uma string ou array contendo todas as letras
    # do alfabeto já ordenadas
    #  (aqui usamos o módulo string.ascii_lowercase)
    # Verificar se as strings possuem o mesmo número de caracteres
    # Então, para cada índice na lista de letras e para cada letra
    # na string testada,
    # quando a letra coincidir com a sua correspondente na
    # lista de letras do alfabeto,
    # convertemos o índice daquela letra em número primo e
    # colocamos este número primo dentro
    # de uma lista de números.
    # Iteramos a lista de números primos gerada e
    # toda vez que o número da lista de números não for None,
    # vamos multiplicar este número pelo valor atual guardado
    # nas variáveis de soma
    # (sum_one para a primeira string e sum_two para a segunda)
    # se os valores de sum_one e sum_two forem iguais,
    # as strings são anagramas (retorna True),
    # se o valor não for o mesmo é porque
    # as strings não são anagramas (retorna False)


def get_num_prime(num):
    if num:
        return num**2 + num + 42


def convert_letter_to_prime(letter):
    primes_nums = []
    num = 0

    for index in range(0, len(letters)):
        for char in letter:
            if char == letters[index]:
                num = get_num_prime(index)
                primes_nums.append(num)
    return primes_nums


def iterate_primes_arr(lista):
    sum_nums = 1
    if lista:
        for num in lista:
            if num is not None:
                sum_nums *= num
    return sum_nums


def is_anagram(first_string, second_string):
    sum_one = 1
    sum_two = 1
    if first_string and second_string:
        if len(first_string) == len(second_string):
            str_one_to_prime = convert_letter_to_prime(first_string)
            str_two_to_prime = convert_letter_to_prime(second_string)
            sum_one = iterate_primes_arr(str_one_to_prime)
            sum_two = iterate_primes_arr(str_two_to_prime)
            if sum_one == sum_two:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

#  Para essa segunda abordagem, foram consultadas as fontes a seguir:
# https://medium.com/@omadson/um-algoritmo-inteligente-para-descobrir-se-duas-palavras-são-ou-não-anagramas-9f4a108a63e
# https://en.wikipedia.org/wiki/Formula_for_primes
