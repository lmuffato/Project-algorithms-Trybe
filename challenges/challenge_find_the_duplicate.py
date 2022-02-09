def find_duplicate(nums):
    """ Faça o código aqui. """
    for number in nums:
        if type(number) != int or number < 0:
            return False
        if nums.count(number) > 1:
            return number
    return False

# Ref:https://www.w3schools.com/python/ref_list_count.asp

