def find_duplicate(nums):
    if len(nums) == 0:
        return False

    duplicated = None
    already_passed = set()

    for num in nums:
        if num in already_passed:
            duplicated = num
        else:
            already_passed.add(num)

    if not duplicated:
        return False

    return duplicated
