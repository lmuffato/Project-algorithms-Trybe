def search_duplicated(nums):
    duplicated = False
    already_passed = set()

    for num in nums:
        if type(num) == str or num < 0:
            return False
        if num in already_passed:
            duplicated = num
        else:
            already_passed.add(num)

    return duplicated


def find_duplicate(nums):
    if len(nums) == 0:
        return False

    duplicated = search_duplicated(nums)

    return duplicated
