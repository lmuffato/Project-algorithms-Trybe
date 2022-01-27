def find_duplicate(nums):
    """ Faça o código aqui. """
    # percorra o array até o ultimo índice e dentro do mesmo
    for i in range(len(nums)):
        for j in range(len(nums)):
            # verifica se não esta comparando mesmo indice
            # verifica se são iguais
            if i != j and nums[i] == nums[j]:
                # verifica se é positivo
                if nums[i] > 0:
                    return nums[i]
    return False
