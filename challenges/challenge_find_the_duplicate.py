def find_duplicate(nums):
    for num in nums:
        # verifica se o elemento do array é um número
        # ou se o elemnto é menor que 0
        if type(num) != int or num < 0:
            return False
        # array.count(elemento) -> retorna quantas vezes
        # o elemento consta no array
        if nums.count(num) > 1:
            return num
    return False


# Teste manual
# print(find_duplicate([1, 3, 4, 2, 2]))


# Teste automatizado
# python3 -m pytest tests/test_find_the_duplicate.py
