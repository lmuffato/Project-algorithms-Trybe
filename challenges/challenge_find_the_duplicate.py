def determine_duplicate(nums):
    ordered_nums = sorted(nums)
    for num in ordered_nums:
        if ordered_nums.count(num) > 1:
            duplicated = num
            return duplicated
    else:
        return False


def find_duplicate(nums):
    """ Faça o código aqui. """
    if not nums:
        return False
    if len(nums) == 1:
        return False
    if any(isinstance(num, str) for num in nums):
        return False
    if any(num < 0 for num in nums):
        return False
    else:
        return determine_duplicate(nums)
