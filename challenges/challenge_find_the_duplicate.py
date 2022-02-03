def find_duplicate(nums):
    duplicated = None
    passed = set()

    for num in nums:
        if num in passed:
            duplicated = num
        else:
            passed.add(num)

    return duplicated
