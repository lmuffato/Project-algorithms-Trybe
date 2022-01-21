# O algoritmo de ordenação usado no método sort_nums é o Bubble sort.
# Nele, comparamos o valor do elemento pelo elemento adjacente,
# realizando a troca de posição entre eles quando estão fora de ordem.
# A cada iteração o pŕoximo maior valor é colocado em sua posição correta,
# o que nos permite decrescer o número de iteração a cada vez que
# a lista ainda não estiver ordenada.
# Referência: course Trybe

# def sort_nums(nums):
#     is_not_ordened = True
#     num_of_iterations = 0

#     while is_not_ordened:
#         is_not_ordened = False

#         for i in range(len(nums) - num_of_iterations - 1):
#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]

#                 is_not_ordened = True
#         num_of_iterations += 1

#     return nums


# def find_duplicate(nums):
#     ordered_nums = sort_nums(nums)
#     try:
#         for index, num in enumerate(ordered_nums):
#             if type(num) != int or num < 0:
#                 return False

#             if num == ordered_nums[index + 1]:
#                 return num
#     except IndexError:
#         return False


# Mas assim... pode usar o count (ಠ_ಠ)
def find_duplicate(nums):

    for num in nums:
        if type(num) != int or num < 0:
            return False

        elif nums.count(num) > 1:
            return num

    return False


# print(find_duplicate([1, 5, 8, 5, 2, 8, 8]))
# print(duplicate_nuns([1, 2, 5, 5, 8]))
