def find_duplicate(nums):
    """ Faça o código aqui. """
    duplicate = 0
    array = []
    for num in nums:
        if type(num) == str or num < 0:
            return False
        if num in array:
            duplicate = num
        else:
            array.append(num)
    if duplicate == 0:
        return False
    return duplicate
