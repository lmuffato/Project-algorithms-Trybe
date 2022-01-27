def find_duplicate(nums):
    """ Faça o código aqui. """
    has_duplicated = False

    # armazena o número de iterações para evitar
    # a iteração sobre índices já ordenados
    num_of_iterations = 0

    # Enquanto ainda não está ordenado (ocorreram trocas na iteração)
    while not has_duplicated:
        has_duplicated = False

        # percorra o array até o ultimo índice
        for i in range(len(nums) - num_of_iterations - 1):
            if int(all(nums)) or nums[i] < 0:

                # caso a posição corrente seja maior que a posterior
                if nums[i] == nums[i + 1]:
                    has_duplicated = True
                    return nums[i]
            else:
                return False

        num_of_iterations += 1

        return has_duplicated
