from string import ascii_lowercase as letters

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
# vamos somar (ou multiplicar, os dois jeitos funcionam)
# este número pelo valor atual guardado
# nas variáveis de soma
# (sum_one para a primeira string e sum_two para a segunda).
# Se os valores de sum_one e sum_two forem iguais,
# as strings são anagramas (retorna True),
# se o valor não for o mesmo é porque
# as strings não são anagramas (retorna False)


def get_num_prime(num):
    if num:
        return num**2 + num + 42


# Source (binary_search):
#  Conteúdo do course, bloco 35
def binary_search(lista, low_index, high_index, target):
    if high_index < low_index:
        return False
    average_index = (high_index + low_index) // 2

    if lista[average_index] == target:
        return average_index
    elif lista[average_index] > target:
        return binary_search(lista, low_index, average_index - 1, target)
    else:
        return binary_search(lista, average_index + 1, high_index, target)


def convert_letter_to_prime(letter):
    primes_nums = []
    num = 0
    for char in letter:
        num = binary_search(letters, 0, len(letters) - 1, char)
        primes_nums.append(num)
    return primes_nums


def iterate_primes_arr(lista):
    sum_nums = 1
    if lista:
        for num in lista:
            if num is not None:
                sum_nums += num
    return sum_nums


def is_anagram(first_string, second_string):
    sum_one = 0
    sum_two = 0
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
# https://educacao.uol.com.br/disciplinas/matematica/numeros-primos-veja-algoritmo-para-encontra-los.htm
