def find_duplicate(nums):
    """ Faça o código aqui. """
    """ url longa:
    https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    """
    if not nums:
        return False
    if len(nums) < 2:
        return False
    c = {}
    for number in nums:
        if type(number) != int or number < 0:
            return False
        c[number] = c.setdefault(number, 0) + 1
    result = False if (max(c.values()) == 1) else max(c, key=c.get)
    return result
